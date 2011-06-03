#!/usr/bin/env python
import random
from Utils import rotate
def binary_search (data, lower, upper, target):
    if upper < lower : 
        print 'NOT EXIST'
        return
    mid = lower+((upper-lower)/2)
    if target == data[mid]: 
        print mid
        return
    elif target > data[mid] : binary_search(data, mid+1, upper, target)
    else : binary_search(data, lower, mid-1, target)

def binary_search_iter(data, lower, upper, target):
    while (True):
        if upper < lower :
            print 'NOT EXIST'
            break
        mid = lower + ((upper-lower)/2)
        if target == data[mid]:
            print mid
            break
        elif target > data[mid]: lower = mid+1
        else: upper = mid-1

def binary_search_iter_rotate(data, lower, upper, target):
    while (True):
        if upper < lower :
            print 'NOT EXIST'
            break
        mid = lower + ((upper-lower)/2)
        if target == data[mid]:
            print mid
            break
        if data[upper] <= data[mid] and data[lower] <= data[mid]:
            if target > data[mid] : upper = mid - 1
            else: lower = mid + 1
        elif data[upper] >= data[mid] and data[lower] >= data[mid]:
            if target > data[mid] : lower = mid + 1
            else: upper = mid - 1
        else:
            if target > data[mid]:
                if target > data[upper]:
                    upper = mid - 1
                else:
                    lower = mid + 1
            else: 
                if target > data[lower]:
                    upper = mid - 1
                else:
                    lower = mid + 1
        print '({0}, {1})'.format(lower, upper) 

if __name__=='__main__':
    sample=[i for i in range(1000)]
    test = random.sample(sample, 100)
    test.sort()
    test = rotate(test, 70)
    binary_search_iter_rotate(test, 0, len(test)-1, test[45])
    test = [15,16,19,20,25,1,3,4,5,7,10,14]
    binary_search_iter_rotate(test, 0, len(test)-1, 5)
