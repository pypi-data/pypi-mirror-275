from setuptools import setup

name = 'sqlime3'
version = '1.0.0'
author = 'GooseG4G'
email = 'danilnegusev@inbox.ru'
desc = 'The package provides a wrapper for working with SQLite databases.'
url = 'https://github.com/GooseG4G/sqlime3'
packages = ['sqlime3']
requires = []

setup(
    name=name,
    version=version,
    author=author,
    author_email=email,
    description=desc,
    url=url,
    packages=packages,
    install_requires=requires
)
