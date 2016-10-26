import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-clinic',
    version='0.1',
    packages=['clinic'],
    include_package_data=True,
    license='BSD License',  # example license
    description='A Django app to display waiting times in clinics.',
    long_description=README,
    url='https://github.com/kvoss/optiwait',
    author='K. Voss',
    author_email='k.voss@usask.ca',
    install_requires=[
        'Django',
        'twitter',
        'pytz',
        'python-dateutil',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

