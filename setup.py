#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
from django_auth_jwt_tenant import __version__

try:
    long_description = open('README.rst').read()
except:
    long_description = "Tenant Django Authentication using JWT from parent Django project."

try:
    license = open('LICENSE.txt').read()
except:
    license = "MIT License"


REQUIREMENTS = [
    'django>=1.8.0',
]

tests_require = [
    'pytest>=2.7.2',
    'pytest-cov',
    'coveralls',
    'coverage==4.4.2',
    'mock',
    'pytz',
    'django-filter',
    'pytest-django==3.1.2',
    'PyJWT==1.5.3'
]

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup(
    name='django-auth-jwt-tenant',
    version=__version__,
    description='Tenant Django Authentication using JWT from parent Django project',
    author='Carlos Martínez',
    author_email='me@carlosmart.co',
    url='https://github.com/CarlosMart626/django_auth_jwt_tenant',
    packages=find_packages(),
    package_data={'': ['README.md']},
    install_requires=REQUIREMENTS,
    license=license,
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=long_description,
    include_package_data=True,
    zip_safe=False,
    test_suite='tests.settings.run',
    keywords='django auth jwt tenant',
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
)
