#!/usr/bin/python
__author__ = 'thovo'

import sys


def ibm1():

    #Check for arguments
    args_length = len(sys.argv)
    print "The number of arguments: "+str(args_length)
    i = 0
    while i < args_length:
        print "The argument number " + str(i) + " is " + str(sys.argv[i])
        i += 1

ibm1()