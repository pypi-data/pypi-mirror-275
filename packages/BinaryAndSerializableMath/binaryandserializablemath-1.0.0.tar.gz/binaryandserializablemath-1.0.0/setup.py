from setuptools import setup, find_packages

with open('README.md', 'r') as file:
    description = file.read()

setup(
    name="BinaryAndSerializableMath",
    version="1.0.0",
    packages=find_packages(),
    install_requires = [
        # nothing is required
    ],
    long_description=description,
    long_description_content_type='text/markdown'
)