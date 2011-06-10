#!/usr/bin/env python

def check(out):
    for i in range(out.__len__()-1):
        for j in range(i+1, out.__len__()):
            if abs(i-j) == abs(out[i] - out[j]):
                return False
    return True

def queen_chess(row, used, out, size):
    if out.__len__() == size:
        if check(out) : 
            print out
        return
    for i in range(size):
        if used[i] : continue
        used[i] = True
        out.append(row[i])
        queen_chess(row, used, out, size)
        used[i] = False
        out.pop()

if __name__=='__main__':
    size = 8 
    row = [i for i in range(size)]
    used = [False for i in range(size)]
    out = []
    queen_chess(row, used, out, size)
