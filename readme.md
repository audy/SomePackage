# SomePackage

A simple example of my proposed "how to package tests" standard.  What do
you think? --titus

I'm turning this into a boilerplate for future Python projects. --austin

--

## Installing

```sh
# you need setuptools
$ python setup.py install

# there is a default executable with logging
# and argument parsing. See `somepackage/__main__.py`
$ spackage
INFO:root:Hello, World!
```

## Testing

```sh
$ python -m somepackage.tests.__main__

# Python > 2.5 w/ setuptools
$ python setup.py tests # > python 2.5

# like nose?
$ nosetests
```
