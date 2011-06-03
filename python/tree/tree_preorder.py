#!/usr/bin/env python
from Tree import Node, Tree
def build_test_tree():
    return  Node(value=100,
                    left = Node(value=50, 
                        left=Node(value=25), right=Node(value=75)),
                    right = Node(value=150,
                        left=Node(value=125, left=Node(value=110)),
                        right=Node(value=175))
                    )
def preorder(current):
    if current is None : return
    if current.value is not None: print current.value
    preorder(current.get_left())
    preorder(current.get_right())

def inorder(current):
    if current is None : return
    inorder(current.get_left())
    if current.value is not None: print current.value
    inorder(current.get_right())

def preorder_iter(current):
    stack = []
    stack.append(current)
    while stack.__len__() > 0 :
        cur = stack.pop()
        if cur.value is not None: print cur.value
        if cur.get_right() is not None: stack.append(cur.get_right())
        if cur.get_left() is not None: stack.append(cur.get_left())

if __name__=='__main__':
   root = build_test_tree()
   #preorder(root)
   bst = Tree(Node())
   bst.generate_bst_from_array(rate=20)
   inorder(bst.get_root())
   #preorder_iter(bst.get_root())
