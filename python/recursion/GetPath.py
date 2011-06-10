#!/usr/bin/env python

def get_path(right, down, pos, out):
    if right == 0:
        while down > 0:
            out[pos] = 'Y'
            pos += 1
            down -= 1
        #print ''.join(out)
        return
    if down == 0:
        while right > 0:
            out[pos] = 'X'
            pos += 1
            right -= 1
        #print ''.join(out)
        return
    out[pos] = 'X'
    get_path(right-1, down, pos+1, out)
    out[pos]= 'Y'
    get_path(right, down-1, pos+1, out)

def get_path_permute(row, used, out):
    if out.__len__() == row.__len__():
        print ''.join(out)
        return
    for i in range(row.__len__()):
        if used[i] : continue 
        used[i]=True
        out.append(row[i])
        get_path_permute(row, used, out)
        used[i]=False
        out.pop()


if __name__=='__main__':
    size =8
    get_path(size-1, size-1, 0, ['' for x in range((size-1) << 1)])
    # Permutation doesn't work since there are lot of depulication
    # the total number of path of 8x8 is 3432 (choice 7 form 14)
    # Permutatin will produce 14! result which is 87178291200 
    #row = ['X' for x in range(size-1)]
    #row.extend(['Y' for x in range(size-1)])
    #get_path_permute(row,[False for i in range((size-1)<<1)],[])
