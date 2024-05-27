from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    description = f.read()

setup(
    name='krezi',
    version='1.0',
    author="Aadil Zikre",
    author_email="aadilzikre@gmail.com",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.23.0',
        'pandas>=1.4.2',
        'itables>=1.5.2',
        'tqdm'
    ],
    long_description=description,
    long_description_content_type='text/markdown'
)