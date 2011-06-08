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

def postorder(current):
    if current is None : return
    postorder(current.get_left())
    postorder(current.get_right())
    if current.value is not None: print current.value

def preorder_iter(current):
    stack = []
    stack.append(current)
    while stack.__len__() > 0 :
        cur = stack.pop()
        if cur.value is not None: print cur.value
        if cur.get_right() is not None: stack.append(cur.get_right())
        if cur.get_left() is not None: stack.append(cur.get_left())

def morris_preorder(root):
    while root is not None:
        print root.value
        if root.right is not None:
            current = root.left
            if current is None:
                root.left = root.right
            else:
                while current.right is not None:
                    current = current.right
                current.right = root.right
        root = root.left

def morris_inorder(root):
    while root is not None:
        if root.left is not None:
            current = root.left
            tmp = root.left
            if current.right is None:
                current.right = root
            else :
                while current.right is not None:
                    current = current.right
                current.right = root
            root.left = None
            root = tmp
        else:
            print root.value
            root = root.right

def find_target_path (target, root):
    path = []
    while root.value > target:
        root = root.left
    stack = [root]
    while stack.__len__() > 0:
        print path, target
        cur = stack.pop()
        target -= cur.value
        if target == 0:
            path.append(cur.value)
            break
        if target > 0:
            path.append(cur.value)
            if cur.right is not None: stack.append(cur.right)
            if cur.left is not None: stack.append(cur.left)
        else:
           path.pop()
           target += cur.value
    #if target == 0 :
    return path
    #return None

if __name__=='__main__':
    root = build_test_tree()
    #print find_target_path(235,root)
    #preorder(root)
    #print 'Morris Preorder Traversal'
    #morris_preorder(root)
    inorder(root)
    print 'Morris Inorder Traversal'
    morris_inorder(root)
    #bst = Tree(Node())
    #bst.generate_bst_from_array(rate=10)
    #inorder(bst.get_root())
    
    #postorder(root)
    #preorder_iter(bst.get_root())
    #print bst.generate_list_for_bst()
