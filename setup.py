#!/usr/bin/env python

from setuptools import setup

install_requires = [
    'boto3==1.4.4',
    'Flask-Bcrypt==0.7.1',
    'Flask-Cache==0.13.1',
    'Flask-Login==0.4.0',
    'Flask-Migrate==2.0.2',
    'Flask-Script==2.0.5',
    'Flask-SQLAlchemy==2.1',
    'Flask-SSLify==0.1.5',
    'Flask==0.12',
    'gunicorn==19.6.0',
    'psycopg2==2.6.2',
    'pytz==2016.10',
    'raven[flask]==5.32.0',
    'redis==2.10.5',
    'wand==0.4.4',
]

tests_requires = [
    'pytest==3.0.6',
]

docs_requires = [
    'Sphinx==1.5.2',
    'sphinxcontrib-httpdomain==1.5.0',
    'sphinx-rtd-theme==0.1.9',
]

setup(name='Graygram',
      version='0.1.0',
      description='Graygram',
      author='Suyeol Jeon',
      author_email='devxoul@gmail.com',
      url='https://github.com/devxoul/graygram-web',
      packages=['graygram'],
      install_requires=install_requires + tests_requires + docs_requires,
      tests_requires=tests_requires)
