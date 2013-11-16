import unittest

def main():
    '''
    Runs the tests

    # or
    $ nosetests
    '''
    suite = somepackage.tests.get_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    main()
