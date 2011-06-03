#!/usr/bin/env python
def combine(pattern, used, out, start):
    #if out.__len__() > 0 : print ''.join(out)
    for index in range(start,pattern.__len__()):
        if used[index]: continue
        out.append(pattern[index])
        used[index] = True
        combine(pattern, used, out, index)
        used[index] = False
        out.pop()

def combine_iter(pattern):
    index = 1
    while index < (1 << pattern.__len__()):
        out = []
        mask,pos = 1,0
        while mask <= index:
            if mask & index:
                out.append(pattern[pos])
            mask <<=1
            pos += 1
        #print ''.join(out)
        index += 1
    

if __name__=='__main__':
    pattern = 'abcdefghijk'
    used = [False for x in range(pattern.__len__())]
    #combine([c for c in pattern], used, [], 0)
    combine_iter(pattern)
