#!/usr/local/bin/python3
import random
import unittest
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def set_right_child(self, node):
        self.right = node
    
    def set_left_child(self, node):
        self.left = node
    
class BinarySearchTree:
    root = None
    def __init__(self, data):
        self.data = data
        # Construct a Tree with data
        self.initialize(self.data)

    def insert(self, root, node):
            if node.data <= root.data:
                if root.left == None:
                    root.set_left_child(node)
                    return
                else:
                    self.insert(root.left, node)
            else:
                if root.right == None:
                    root.set_right_child(node)
                    return
                else:
                    self.insert(root.right, node)

    def initialize(self, data):
        for ele in data:
            n = Node(ele)
            if self.root == None:
                self.root = n
                continue
            else:
                self.insert(self.root, n)
        
tree_nodes = []

def inorder(node):
    if node != None:
        inorder(node.left)
        tree_nodes.append(node.data)
        inorder(node.right)


class BinarySearchTreeTestCase(unittest.TestCase):
    # Test tree using random data and inorder property.
    def test_bst(self):
        for _ in range(100):
            global tree_nodes
            tree_nodes = []
            k = random.randint(1,1000)
            data = random.sample(range(1,1000), k)
            x = BinarySearchTree(data)
            inorder(x.root)
            self.assertEqual(tree_nodes, sorted(data))

if __name__=="__main__":
    unittest.main()

