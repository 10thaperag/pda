#!/usr/bin/env python3
# date.py
# vim:expandtab:sw=4:sts=4
# 
# Written by Nathaniel Gephart <nate.gephart@gmail.com>
# 2010-01-23
#
# [license]
#
# $Id$
#

import personattr

class Date (personattr.Attribute):
    def __init__ (self, type, date):
        super().__init__(type,date)

    def __str__ (self):
        return super().__str__()
