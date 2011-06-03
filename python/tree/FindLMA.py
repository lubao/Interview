#!/usr/bin/env python
from Tree import Tree, Node
import random
def find_path(cur, target, path=[]):
    if cur.value is None :
        return False
    path.append(cur.value)
    if cur.value == target :
        return True
    if find_path(cur.left, target, path):
        return True
    if find_path(cur.right, target, path):
        return True
    path.pop()
    return False

if __name__=="__main__":
    rate = 100
    sample=[i for i in range(1000)]
    data = random.sample(sample, rate)
    data.sort()
    root = Node()
    bst = Tree(root)
    root=bst.generate_bst_from_sorted_array(data, bst.get_root(), upper=rate-1)
    path = []
    target = data[rate/5]
    print target
    find_path(root, data[rate/5], path)
    print path
    
