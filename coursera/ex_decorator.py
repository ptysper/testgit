#!/usr/bin/env python3

def identity(ob):
    return ob

@identity
def myfunc():
    print ('my function')

myfunc()
print(myfunc)
