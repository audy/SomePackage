import unittest
import somepackage.tests

def main():
    '''
    Runs the tests

    # using python -m
    $ python -m somepackage.tests

    # or
    >>> import somepackage.tests.main
    >>> main()

    # or
    $ nosetests
    '''
    suite = somepackage.tests.get_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    main()
