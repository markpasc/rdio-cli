from setuptools import setup

setup(
    name='rdio-cli',
    version='1.2',
    packages=[],
    include_package_data=True,
    scripts=['bin/rdio'],

    requires=['termtool', 'Rdio'],
    install_requires=['termtool', 'Rdio'],
)
