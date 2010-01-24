#!/usr/bin/env python3
# pdaconfig.py
# vim:expandtab:sw=4:sts=4
# 
# Written by Nathaniel Gephart <10thaperag@gmail.com>
# 2010-01-23
#
# [license]
#

import os
import configparser
import pdadefaults

class PDAConfig:
    def __init__ (self, c=None):
        self.configfile = ""
        self.parser = None

        if c is not None:
            self.configfile = os.path.expanduser(c)
        else:
            self.configfile = os.path.expanduser(pdadefaults.configfile)

        self.parser = configparser.ConfigParser()
        self.parser.read(self.configfile)

