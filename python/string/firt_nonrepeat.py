#!/usr/bin/env python
def first_nonrepeat(test):
    table = {}
    for c in test:
        if c in table:
            table[c] += 1
        else:
            table[c] = 1
    for c in test:
        if table[c] == 1:
            print c 
            break

if __name__ == '__main__':
    test = 'total'
    first_nonrepeat(test.lower())
