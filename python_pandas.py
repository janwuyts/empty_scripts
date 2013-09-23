#!/usr/bin/env python
"""Change this docstring of this empty script

For analysis scripts I prefer to have everything running in
the main namespace. This plays nicer with ipython.

- Run unittests if called with "test" as first and only argument
- Call main() if there are other command line arguments
"""
__author__ = "Jan Wuyts"
__copyright__ = "Copyright 2013"
__credits__ = ["Jan Wuyts", ]
__version__ = "0.0.1"
__maintainer__ = "Jan Wuyts"
__email__ = "Jan.Wuyts@gmail.com"
__status__ = "Development"
import sys
## UNIT TESTS ##############################################
import unittest
class UnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_whatever(self):
        self.assertEquals(True, True)

if (len(sys.argv) == 2) and ("test" in sys.argv[1].lower()):
    sys.argv = sys.argv[:1]
    unittest.main()
    sys.exit()
## COMMAND LINE OPTIONS ####################################
import optparse
parser = optparse.OptionParser(usage = "usage: python %prog [options]", description=__doc__)
parser.add_option('-v',
        '--verbose',
        dest="verbose",
        action="store_true",
        default=False,
        help="be more verbose")
if len(sys.argv) > 1:
    options, remainder = parser.parse_args(sys.argv)
else:
    try:
        options
    except:
        options, remainder = parser.parse_args(list())
## LOGGING #################################################
import logging
if options.verbose:
    logging.basicConfig(level=logging.INFO)
else:
    logging.basicConfig(level=logging.ERROR)

error = lambda x: logging.error(x)
warn  = lambda x: logging.warning(x)
info  = lambda x: logging.info(x)
#######
## Do something useful here ################################
##############
#import os
#import re
#import numpy as np
#import matplotlib as plt
#import pandas as pd
#from pandas import ExcelFile
#from pandas import ExcelWriter

