#!/usr/bin/env python
# encoding: utf8

import argparse
import logging

def parse_args():
    ''' return arguments
        >>> args = parse_args()
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('--log', default='/dev/stderr', help='log file (default=stderr)')
    parser.add_argument('--verbose', default=False, action='store_true')
    return parser.parse_args()


def setup_logging(logfile='/dev/stderr', verbose=False):
    ''' Sets up logging with verbosity.

        >>> setup_logging(logfile='/dev/stdout', verbose=True)
        >>> logging.debug('howdy')
    '''

    if verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO

    return logging.basicConfig(filename=logfile, level=level)


def main():
    '''
    This is the default entry point if you are building an
    executable. If you aren't, remove it and the entry point
    defined in setup.py

    >>> main() # returns None
    '''

    args = parse_args()

    setup_logging(logfile=args.log, verbose=args.verbose)

    logging.info('Hello, World!')

if __name__ == '__main__':
    main()
