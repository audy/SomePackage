import unittest

from somepackage import SomeClass

class TestSomething(unittest.TestCase):
    ''' Example of a test '''

    def test_some_method(self):
        ''' You should write a test '''

        the_answer = SomeClass.some_method()
        self.assertEqual(the_answer, 42)

def get_suite():
    ''' Sets up and returns a unittest.TestSuite '''
    import somepackage.tests

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(somepackage.tests)
    return suite
