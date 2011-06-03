#!/usr/bin/env python
def replace_bits(n, m , i, j):
    m1 = ~0 << j+1
    tmp = i-1
    m2 = 1
    if tmp < 0 : m2 = 0
    else:
        while tmp > 0:
            m2<<=1
            m2+=1
            tmp -= 1
    mask = m1 | m2
    return (n & mask) | (m << i)

def num_convert_bits(a, b):
    c = a ^ b
    num, mask = 0, 1
    while mask <= c :
        if c & mask : num += 1
        mask <<= 1
    return num

def swap_odd_even_bits(n):
    mask_even = 0xAAAAAAAA
    mask_odd = ~mask_even
    return ((n & mask_odd) << 1) | ((n & mask_even) >> 1)
    
def find_miss(data, num_digits):
    mask = 0x80000000
    miss = 0
    while mask > 0:
        res = 0
        for x in data:
            res ^= (x&mask)
        if res : 
            miss += 1
        mask >>= 1
        miss <<= 1
    return miss >> 1

def add_no_plus(a, b):
    if b == 0 : return a
    return add_no_plus(a^b,(a&b) << 1)

def add_no_plus_iter(a, b):
    while b > 0:
        tmp = a^b
        b = (a&b)<<1
        a = tmp
    return a

if __name__=='__main__':
    #res = replace_bits(1<<6, 1<<3, 1, 4)
    #print res
    #res = num_convert_bits(31,8)
    #print res
    #res = swap_odd_even_bits(0x80000000)
    #print res
    #test = [x for x in range(1<<10)]
    #miss = test.pop(256)
    #res = find_miss(test, 10)
    #print res == miss
    print add_no_plus_iter(30,12)
