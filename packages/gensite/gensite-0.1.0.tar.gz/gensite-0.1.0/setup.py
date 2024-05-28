from setuptools import find_packages, setup

setup(
    name='gensite',
    version=open('version.txt').read().strip(),
    author='Evan Raw',
    author_email='evanraw.ca@gmail.com',
    description='Static site generator',
    license='MIT',
    install_requires=[],
    packages=find_packages()
)
