import unittest

# import the actual test files
import some_test

def get_suite():
    ''' Sets up and returns a unittest.TestSuite '''
    import somepackage.tests

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(somepackage.tests)
    return suite
