#!/usr/bin/env python
def print_par(l, r, out, count):
    print 'Entry Point: ',l, r, ''.join(out), count
    #if l < 0 or r < 0 : return
    if l ==0 and r == 0: 
        #print ''.join(out)
        return
    else:
        #print l, r, ''.join(out), count
        if l > 0:
            out[count] = '('
            print_par(l-1, r, out, count + 1)
        print 'Pick Up Point One: ',l, r, ''.join(out), count
        if r - l > 0:
            out[count] = ')'
            print_par(l, r-1, out, count + 1)
        print 'Pick Up Point Two: ',l, r, ''.join(out), count

if __name__=='__main__':
    count =  2 
    print_par(count, count, ['' for x in range(count << 1)], 0)
