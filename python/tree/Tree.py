#!/usr/bin/env python
import random
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def __unicode__(self):
        return '{0}'.format(value)

class Tree:
    def __init__(self, root):
        self.root = root

    def __str__(self):
        return __unicode__()

    def __unicode__(self):
        return str(self.value)

    def get_root(self):
        return self.root

    def generate_bst_from_array(self, data=None, up_bound=1000, rate=100):
        if data is None:
            sample=[i for i in range(up_bound)]
            data = random.sample(sample, rate)
            data.sort()
        self.generate_bst_from_sorted_array(data, self.root, rate-1, 0)

    def generate_bst_from_sorted_array(self, data, 
                current, upper=999, lower=0):
        if lower > upper : return
        mid = lower + (upper-lower)/2
        current.value = data[mid]
        current.left = Node()
        current.right = Node()
        self.generate_bst_from_sorted_array(
            data, current.left, mid-1, lower 
        )
        self.generate_bst_from_sorted_array(
            data, current.right, upper, mid+1 
        )
        return self.root
        
