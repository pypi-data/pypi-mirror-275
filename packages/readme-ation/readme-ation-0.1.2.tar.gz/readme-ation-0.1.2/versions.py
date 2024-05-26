import subprocess
import sys
import re
import atexit
import importlib
import ast
import os
import pkgutil
import importlib.metadata

# List of standard library modules to ignore
IGNORED_LIB_MODULES = {'os', 'enum', 'random', 'readme_version_logger'}

def get_python_version():
    return sys.version.split()[0]

def run_subprocess(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"Error running command {' '.join(command)}: {result.stderr}")
            return []
        return result.stdout.splitlines()
    except Exception as e:
        print(f"Exception running command {' '.join(command)}: {e}")
        return []

def get_installed_packages():
    packages = {}

    # Get packages from mamba
    mamba_lines = run_subprocess(['mamba', 'list'])
    for line in mamba_lines:
        if line.startswith('#'):
            continue
        parts = re.split(r'\s+', line)
        if len(parts) >= 2:
            package = parts[0]
            version = parts[1]
            packages[package] = version

    # Get packages from pip
    pip_lines = run_subprocess([sys.executable, '-m', 'pip', 'freeze'])
    for line in pip_lines:
        if '==' in line:
            pkg, version = line.split('==')
            if pkg not in packages:  # Do not overwrite mamba-installed packages
                packages[pkg] = version

    return packages

def get_imported_packages(script_path):
    with open(script_path, 'r') as file:
        tree = ast.parse(file.read(), filename=script_path)
    
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            imports.add(node.module.split('.')[0])
    return list(imports)

def get_specific_packages_versions(imported_packages, installed_packages):
    specific_versions = {}
    for package in imported_packages:
        if package in IGNORED_LIB_MODULES:
            continue
        if package in installed_packages:
            specific_versions[package] = installed_packages[package]
        else:
            try:
                version = importlib.metadata.version(package)
                specific_versions[package] = f"standard library ({version})"
            except importlib.metadata.PackageNotFoundError:
                specific_versions[package] = "version not found"
    return specific_versions

def update_readme(script_path):
    python_version = get_python_version()
    installed_packages = get_installed_packages()
    imported_packages = get_imported_packages(script_path)
    specific_versions = get_specific_packages_versions(imported_packages, installed_packages)

    with open('README.md', 'r') as file:
        readme_content = file.read()

    # Define the start and end markers
    python_version_start_marker = "## Python Version:"
    python_version_end_marker = "  - END Python Version -\n"
    packages_start_marker = "## Packages:"
    packages_end_marker = "  - END Packages -\n"

    new_python_version_section = f"{python_version_start_marker}\n{python_version}\n{python_version_end_marker}"
    new_packages_section = f"{packages_start_marker}\n" + '\n'.join([f"{pkg}: {ver}" for pkg, ver in specific_versions.items()]) + f"\n{packages_end_marker}"

    # Replace the existing Python version section
    python_version_pattern = re.compile(rf"{re.escape(python_version_start_marker)}.*?{re.escape(python_version_end_marker)}", re.DOTALL)
    if python_version_pattern.search(readme_content):
        readme_content = python_version_pattern.sub(new_python_version_section, readme_content)
    else:
        readme_content += '\n' + new_python_version_section

    # Replace the existing packages section
    packages_pattern = re.compile(rf"{re.escape(packages_start_marker)}.*?{re.escape(packages_end_marker)}", re.DOTALL)
    if packages_pattern.search(readme_content):
        readme_content = packages_pattern.sub(new_packages_section, readme_content)
    else:
        readme_content += '\n' + new_packages_section

    with open('README.md', 'w') as file:
        file.write(readme_content)

def log_versions_to_readme_on_successful_exit(script_path):
    atexit.register(update_readme, script_path)

# Example usage
# log_versions_to_readme_on_successful_exit('your_script.py')
