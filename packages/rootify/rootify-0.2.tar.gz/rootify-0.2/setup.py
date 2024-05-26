from setuptools import setup, find_packages

setup(
    name='rootify',
    version='0.2',
    packages=find_packages(),
    description='A simple package to change the working directory to the project root based on a marker.',
    author='Jimmys-Code',
    author_email='jazcogames@gmail.com',
    url='https://github.com/jimmys-code/rootify',  # Replace with your GitHub URL or project page
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

