from setuptools import setup

from somepackage import __version__

setup(
    name='SomePackage',
    version=__version__.string,
    author='C. Titus Brown, Austin G. Davis-Richardson',
    author_email='titus@idyll.org, harekrishna@gmail.com',
    packages=['somepackage', 'somepackage.tests'],
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
