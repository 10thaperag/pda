#!/usr/bin/env python3
# contact.py
# vim:expandtab:sw=4:sts=4
# 
# Written by Nathaniel Gephart <nate.gephart@gmail.com>
# 2010-01-23
#
# [license]
#
# $Id$
#

import phone
import date

class Contact:
    def __init__ (self, fn, ln, m, b):
        # boolean: True if person, False if company
        # TODO: unused at present
        self.person = True

        self.firstname = fn
        self.lastname = ln
        self.phones = [phone.Phone('mobile', m)]
        self.dates = [date.Date('birthday', b)]

    def __str__ (self):
        out = "Name: {0} {1}\n".format(self.firstname, self.lastname)
        for p in self.phones:
            out += str(p) + '\n'
        for d in self.dates:
            out += str(d)
        return out


if __name__ == "__main__":
    PEOPLE = open("birthdays.txt",'r')
    entries = PEOPLE.readlines()
    PEOPLE.close()

    for e in entries:
        if e.startswith('#'): continue
        (n,c,b) = e.split(',')
        (fn,ln) = n.split(' ',1)
        print(Contact(fn,ln,c,b))

