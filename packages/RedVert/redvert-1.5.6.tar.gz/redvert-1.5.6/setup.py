from setuptools import setup, find_packages

with open('README.md', 'r') as file:
    description = file.read()

setup(
    name='RedVert',
    version='1.5.6',
    packages=find_packages(),
    install_requires = [
        # nothing is required
    ],
    entry_points={
        "console_scripts": [
            'redvert = redvert:Initalize',
        ],
    },
    long_description=description,
    long_description_content_type='text/markdown'
)