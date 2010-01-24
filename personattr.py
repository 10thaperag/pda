#!/usr/bin/env python3
# personattr.py
# vim:expandtab:sw=4:sts=4
# 
# Written by Nathaniel Gephart <nate.gephart@gmail.com>
# 2010-01-23
#
# [license]
#
# $Id$
#

class Attribute:
    def __init__ (self, type, value):
        self.type = type
        self.value = value

    def __str__ (self):
        return "{0}: {1}".format(self.type, self.value)
