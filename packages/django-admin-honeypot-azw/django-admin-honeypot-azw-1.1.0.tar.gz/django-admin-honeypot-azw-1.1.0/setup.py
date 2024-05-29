#!/usr/bin/env python
import sys
from admin_honeypot import __version__, __description__, __license__

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='django-admin-honeypot-azw',
    version=__version__,
    description=__description__,
    long_description=open('./README.rst', 'r').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    keywords='django admin honeypot trap',
    maintainer='azwdevops',
    maintainer_email='',
    url='https://github.com/azwdevops/django-admin-honeypot-azw',
    download_url='https://github.com/azwdevops/django-admin-honeypot-azw.git',
    license=__license__,
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'django-ipware',
    ]
)
