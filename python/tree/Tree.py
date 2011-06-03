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

    def get_root(self):
        return self.root

    def generate_bst_from_array(self, data=None, up_bound=1000, rate=100):
        if data is None:
            sample=[i for i in range(up_bound)]
            data = random.sample(sample, rate)
            data.sort()
        self.generate_bst_from_sorted_array(data, self.root, rate-1, 0)

    def generate_bst_from_sorted_array(self, data, current, upper, lower):
        #if lower > upper : return
        mid = lower + (upper-lower)/2
        current.value = data[mid]
        current.left = Node()
        current.right = Node()
        if lower <= mid - 1:
            self.generate_bst_from_sorted_array(
                data, current.left, mid-1, lower 
            )
        if mid + 1 <= upper:
            self.generate_bst_from_sorted_array(
                data, current.right, upper, mid+1 
            )

    def generate_list_for_bst(self):
        ret = []
        queue = [self.root]
        while queue.__len__() > 0:
            working_nodes = []
            res = []
            while queue.__len__() > 0 :
                working_nodes.append(queue.pop(0))
            while working_nodes.__len__() > 0:
                working_node = working_nodes.pop(0)
                if working_node.value is not None:
                    res.append(working_node.value)
                if working_node.get_left() is not None : 
                    queue.append(working_node.get_left())
                if working_node.get_right() is not None:
                    queue.append(working_node.get_right())
            ret.append(res)
        return ret

            
