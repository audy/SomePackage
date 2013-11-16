from setuptools import setup

from somepackage import __version__

setup(
    name='SomePackage',
    version=__version__.string,
    author='C. Titus Brown',
    author_email='titus@idyll.org',
    packages=['somepackage', 'somepackage.tests'],
    url='http://pypi.python.org/pypi/SomePackage/',
    license='LICENSE.txt',
    description='Useful package-test-related stuff.',
    test_suite='somepackage.tests.get_suite'
)
