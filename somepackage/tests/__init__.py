import unittest

class TestSomething(unittest.TestCase):
    ''' Example of a test '''

    def test_something_else(self):
        ''' You should write a test '''
        self.assertEqual(True, True)

def get_suite():
    ''' Sets up and returns a unittest.TestSuite '''
    import somepackage.tests

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(somepackage.tests)
    return suite
