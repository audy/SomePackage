# SomePackage

A simple example of my proposed "how to package tests" standard.  What do
you think? --titus

--

## Installing

```sh
# you need setuptools
$ python setup.py install
```

## Testing

```sh
$ python -m somepackage.tests.__main__

# Python > 2.5 w/ setuptools
$ python setup.py tests # > python 2.5

# like nose?
$ nosetests
```
