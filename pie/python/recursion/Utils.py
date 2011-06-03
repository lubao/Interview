#!/usr/bin/env python
def reverse(data, start, end):
    while start < end:
        tmp = data[start]
        data[start] = data[end]
        data[end] = tmp
        start += 1
        end -= 1
    return data

def rotate(data, step):
    data = reverse (data, 0, step-1)
    data = reverse (data, step, len(data)-1)
    data = reverse (data, 0, len(data)-1)
    return data
