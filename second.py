x#!/usr/bin/python3

import sys

def moyenne(a,b):
    "Fonction moyenne"
    c = ( a + b ) / 2
    return(c)


a = int(sys.argv[1])
b = int(sys.argv[2])


print(moyenne(a,b))
