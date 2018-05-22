# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import os
import io
from setuptools import setup


def read(fname):
    return io.open(
        os.path.join(os.path.dirname(__file__), fname),
        'r', encoding='utf-8').read()

setup(name='tryton-account-csv2xml',
    version='0.1.0',
    author='gcoop',
    author_email='info@gcoop.coop',
    url='https://github.com/tryton-ar/tryton-account-csv2xml',
    description='Store Tryton files on S3 AWS Storage.',
    long_description=read('README'),
    py_modules=['tryton_account_csv2xml'],
    zip_safe=False,
    platforms='Posix; MacOS X; Windows',
    keywords='tryton account chart csv xml',
    classifiers=[
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet'
        ],
    license='GPL-3',
    use_2to3=True,
    )
