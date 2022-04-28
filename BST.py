import os
import sys
import argparse



class Node():

    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_left_child(self):
        return self.left

    def set_left_child(self, left_pointer):
        self.left = left_pointer

    def get_right_child(self):
        return self.right

    def set_right_child(self, right_pointer):
        self.right = right_pointer
        
    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def __str__(self):
        return f"node value is: {self.get_value()}"

    def __repr__(self):
        return f"Node({self.get_value()})"


class Tree():

    def __init__(self, value):
        self.root = Node(value)

    
    def get_root(self):
        return self.root
        




def main():
    node0 = Node('apple')
    node1 = Node('banana')
    node2 = Node('orange')
    node0.set_left_child(node1)
    node0.set_right_child(node2)

    print(f"node0 left child: {node0.left.value}")
    print(f"node0 has left child: {node0.has_left_child()}")
    print(f"node1 has left child: {node1.has_left_child()}")

    tree = Tree('apple')
    tree.get_root().set_left_child(node1)
    tree.get_root().set_right_child(node2)
    print(tree)

if __name__ == '__main__':
    main()

