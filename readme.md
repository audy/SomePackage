# SomePackage

A simple example of my proposed "how to package tests" standard.  What do
you think? --titus

--

To run the tests, you can do:

    % python -m somepackage.tests.__main__

Under Python 2.5 or above, and:

    % python setup.py test

if you have setuptools or Distribute installed.  This mechanism will also
be supported under distutils2, or distutils under 3.3 and above.

You can also run:

    % nosetests

with nose.

How about py.test?  Other test runners?

---

Rules, in brief:
----------------

 - for a given package, 'python -m somepackage.tests.__main__' should run
   its tests, if any.

 - no code outside of 'somepackage.tests' should depend on
   'somepackage.tests'.  This is so that distrib packagers (debian,
   redhat) can omit the sub-package from the non-devel install.
