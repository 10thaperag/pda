#!/usr/bin/env python3
# phone.py
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

class Phone(personattr.Attribute):
    def __init__ (self, type, phone):
        super().__init__(type,phone)
    
    def __str__ (self):
        return super().__str__()
