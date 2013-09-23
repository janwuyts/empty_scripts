#!/usr/bin/env python
"""Change this docstring of this empty script

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
import logging
import optparse
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
## LOGGING #################################################
error = lambda x: logging.error(x)
warn  = lambda x: logging.warning(x)
info  = lambda x: logging.info(x)
def main(argv=None):
    if argv is None:
        argv = sys.argv
    ## COMMAND LINE OPTIONS ####################################
    parser = optparse.OptionParser(usage = "usage: python %prog [options]", description=__doc__)
    parser.add_option('-v', '--verbose',
            dest="verbose",
            action="store_true",
            default=False,
            help="be more verbose")
    options, remainder = parser.parse_args(sys.argv)
    if options.verbose:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.ERROR)
    #######
    ## Do something useful here ################################
    ##############
#    import os
#    import re








if __name__=="__main__":
    sys.exit(main())
