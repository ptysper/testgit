#!/usr/bin/env python3

# A simple generator function
def my_gen():
    for i in range(5):
        print('Output: \n' + str(i))
        yield i

x = my_gen()
while True:
    next(x)
