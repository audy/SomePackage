# SomePackage

A simple example of my proposed "how to package tests" standard.  What do
you think? --titus

--

To run tests:

```sh
$ python -m somepackage.tests.__main__

# Python > 2.5 w/ setuptools or Distribute
$ python setup.py tests # > python 2.5

# like nose?

$ nosetests
```