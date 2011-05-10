from setuptools import setup

setup(
    name='rdio-cli',
    version='1.0',
    packages=[],
    include_package_data=True,
    scripts=['bin/rdio'],

    requires=['argparse', 'Rdio'],
    install_requires=['argparse', 'Rdio'],
)
