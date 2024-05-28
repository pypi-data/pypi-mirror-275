from setuptools import setup, find_packages

setup(
    name="readme-ation",
    version="0.1.6",
    packages=find_packages(),
    install_requires=[
        # List dependencies here, e.g. 'requests>=2.25.1'
    ],
    entry_points={
        # 'console_scripts': [
        #     'main = main:log_versions_to_readme_on_successful_exit',  # Assuming you have a main function in my_script.py
        # ],
    },
    author='Charles Feinn',
    email='chuckfinca@gmail.com',
    description='A README.md generation tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your-repo',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    license_files = ('LICENSE.txt',),
)