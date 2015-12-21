import unittest

# import the actual test files
def get_suite():
    ''' Sets up and returns a unittest.TestSuite '''
    from .somepackage import tests

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(tests)
    return suite
