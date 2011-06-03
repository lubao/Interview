#!/usr/bin/env python
def remove_string(org, rm):
    # build a lookup table(HASH)
    # according to the letter in rm
    remove = [c for c in rm]
    ret = [c for c in org if c not in remove]
    print ''.join(ret)

def remove_string_dict(org, rm):
    # build a lookup table(HASH)
    # according to the letter in rm
    table = {}
    for c in rm:
        table[c]= None
    ret = [c for c in org if c not in table]
    print ''.join(ret)

if __name__=='__main__':
    org = 'Battle of the Vowels: Hawaii vs.Grozny'
    rm = 'aeiou'
    remove_string(org, rm)
    remove_string_dict(org, rm)
