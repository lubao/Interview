#!/usr/bin/env python 
def swap(all_words, cur, last):
    while cur < last:
        tmp = all_words[cur]
        all_words[cur] = all_words[last]
        all_words[last] = tmp
        cur += 1
        last -= 1
    return all_words

def reverse_string(org):
    all_words = [c for c in org]
    cur, last = 0, len(org)-1
    all_words = swap(all_words,cur,last)
    start = 0
    while cur <= last:
        is_space = False
        if all_words[cur] != ' ':
            cur += 1
        else: is_space = True
        if is_space or cur == last:
            if  is_space : end = cur - 1
            else : end=cur
            all_words = swap(all_words,start,end)
            cur += 1
            start = cur
    print ''.join(all_words)

if __name__ == '__main__':
    test = 'Reversing this string is fast.'
    reverse_string(test)
