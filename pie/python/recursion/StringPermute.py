#!/usr/bin/env python
def permute(pattern, out, used):
    if out.__len__() == pattern.__len__(): 
        print ''.join(out)
        return
    for index in range(pattern.__len__()):
        if used[index]: continue
        used[index] = True
        out.append(pattern[index])
        permute(pattern, out, used)
        used[index] = False
        out.pop()
        

if __name__=='__main__':
    pattern = 'hat'
    used = [False for x in range(pattern.__len__())]
    permute([c for c  in pattern],[],used)
