#!/usr/bin/env python
from Utils import Tester 

def insert_sort(data):
    for i in range(1,data.__len__()):
        j = i -1
        tmp = data[i]
        while j >= 0:
            if data[j] > tmp:
                data[j+1] = data[j]
                j -= 1
            else : break
        data[j+1] = tmp
    return data

def merge_insert_sort(data, l, m):
    for i in range(l,m):
        j = i-1 
        tmp = data[i]
        while j >= 0 and j >= l:
            if data[j] > tmp:
                data[j+1] = data[j]
                j -= 1
            else : break
        data[j+1] = tmp
    return data

def quick_sort(data, left, right):
    if left >= right : return
    pivot , i, j= data[left], left, right 
    while i < j :
        while i < right and data[i] <= pivot:
            i += 1
        while j > left and data[j] > pivot:
            j -= 1
        if i < j:
            tmp = data[j]
            data[j]=data[i]
            data[i]=tmp
    data[left] = data[j]
    data[j] = pivot
    quick_sort(data, left, j-1)
    quick_sort(data, j+1, right)

def merge(data, l, scope):
    m = l + scope - 1
    n = m + scope
    k = l
    tmp = []
    if n > data.__len__() :
        n = data.__len__() -1;
    i = m 
    m += 1
    while l <= i and m <= n:
        if data[l] < data[m]:
            tmp.append(data[l])
            l += 1
        else:
            tmp.append(data[m])
            m += 1
    if l > i:
        tmp.extend(data[m:n+1])
    else:
        tmp.extend(data[l:i+1])
    for i in range(k,n+1):
        data[i]=tmp[i-k]
    

def merge_sort_iter (data):
    level = 1 
    while level < data.__len__():
        start = 0
        while start < data.__len__():
            #end = start +level -1
            #if start+level-1 >= data.__len__():
            #    end = data.__len__()-1
            merge(data, start, level)
            #quick_sort(data, start, end)
            #merge_insert_sort(data, start, end)
            start += level << 1 
        level <<= 1
    rest = data.__len__() - (level >> 1)
    if rest > 0:
        merge(data, 0, data.__len__()-1)
        #quick_sort(data, 0, data.__len__()-1)
        #merge_insert_sort(data, 0, data.__len__()-1)


if __name__=='__main__':
    data=Tester._generate_test_list(rate=5000)
    tmp = data[:]
    insert_sort(tmp)
    tmp = data[:]
    quick_sort(tmp, 0, tmp.__len__()-1)
    tmp = data[:]
    merge_sort_iter(tmp)
