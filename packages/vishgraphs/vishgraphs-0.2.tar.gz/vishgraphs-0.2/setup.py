from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='vishgraphs',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'networkx',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',  # Assuming your README is in Markdown format
)
