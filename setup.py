from setuptools import setup

from somepackage import __version__

setup(
    name='SomePackage',
    version=__version__.string,
    packages=['somepackage'],
    url='http://pypi.python.org/pypi/SomePackage/',
    license='LICENSE.txt',
    description='Useful package-test-related stuff.',
    test_suite='somepackage.tests.get_suite',
    entry_points = {
        'console_scripts': [
            'spackage = somepackage.__main__:main'
        ]
    }
)
