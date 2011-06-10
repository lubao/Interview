#!/usr/bin/env python
def print_par(l, r, out, count):
    #print 'Entry Point: ',l, r, ''.join(out), count
    #if l < 0 or r < 0 : return
    if l ==0 and r == 0: 
        #print ''.join(out)
        return
    else:
        #print l, r, ''.join(out), count
        if l > 0:
            out[count] = '('
            print_par(l-1, r, out, count + 1)
        #print 'Pick Up Point One: ',l, r, ''.join(out), count
        if r - l > 0:
            out[count] = ')'
            print_par(l, r-1, out, count + 1)
        #print 'Pick Up Point Two: ',l, r, ''.join(out), count

def print_par_new (l, r, out, count):
    if l == 0:
        while r > 0:
            out[count]=')'
            r -= 1
            count += 1
        #print ''.join(out)
        return
    if l > 0 :
        out[count]='('
        print_par_new(l-1, r, out, count+1)
    if l < r :
        out[count]=')'
        print_par_new(l,r-1,out,count+1)

if __name__=='__main__':
    count =  10 
    print_par(count, count, ['' for x in range(count << 1)], 0)
    # this new function has better performance
    # for count = 10
    # new one take 0.134 ns
    # old one take 0.225 ns
    print_par_new(count, count, ['' for x in range(count << 1)], 0)
