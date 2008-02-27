"""pyrtf-ng - The next generation in Rich Text Format documents for Python.

pyrtf-ng is a pure python module for the efficient creation and parsing of rich
text format documents. Supports styles, tables, cell merging, jpg and png
images and tries to maintain compatibility with as many RTF readers as
possible. """

from distutils.core import setup

doclines = __doc__.split("\n")

setup(name = 'pyrtf-ng',
    version = open('VERSION').read().strip(),
    author = 'Duncan McGreggor',
    author_email = 'oubiwann@adytum.us',
    url = 'http://code.google.com/p/pyrtf-ng/',
    license = 'MIT',
    platforms = ['Any'],
    description = doclines[0],
    long_description = '\n'.join( doclines[2:]),
    keywords = ('RTF', 'Rich Text', 'Rich Text Format', 'documents',
        'word'),
    packages = [
        'rtfng',
        'rtfng.parser',
        'rtfng.writer',
        ],
    package_dir = {
        'rtfng': 'rtfng'
        },
    classifiers = [f.strip() for f in """
        Development Status :: 4 - Beta
        Topic :: Text Editors :: Text Processing
        Topic :: Software Development :: Libraries :: Python Modules
        Intended Audience :: Developers
        Programming Language :: Python
        License :: OSI Approved :: MIT
        """]
    )