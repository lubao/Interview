#!/usr/bin/env python
def atoi(test):
    tmp = [c for c in test]
    is_nag = False
    if tmp[0] == '-':
        is_nag = True
        tmp.pop(0)
    tmp.reverse()
    base, ret = 1, 0
    for c in tmp:
        if c == '1': val=1
        elif c == '2': val=2
        elif c == '3': val=3
        elif c == '4': val=4
        elif c == '5': val=5
        elif c == '6': val=6
        elif c == '7': val=7
        elif c == '8': val=8
        elif c == '9': val=9
        else: val=0
        ret += val * base
        base *= 10
    if is_nag: ret *= -1
    print ret

def itoa(test):
    if test == 0: 
        print '0'
        return
    elif test < 0 : ret= ['-',] 
    else : ret = []
    base = 10
    while test != 0:
        res = test % base
        test /= 10 
        if res == 0 : tmp = '0'
        elif res == 1 : tmp = '1'
        elif res == 2 : tmp = '2'
        elif res == 3 : tmp = '3'
        elif res == 4 : tmp = '4'
        elif res == 5 : tmp = '5'
        elif res == 6 : tmp = '6'
        elif res == 7 : tmp = '7'
        elif res == 8 : tmp = '8'
        else : tmp = '9'
        ret.insert(0,tmp)
    print ''.join(ret)


if __name__ == '__main__':
    test_str = '-22345'
    test_int = 0 
    atoi(test_str)
    itoa(test_int)
