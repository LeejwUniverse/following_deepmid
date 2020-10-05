import numpy as np
from collections import deque
import matplotlib.pyplot as plt
import math

class Node():
    def __init__(self, axis_data, cur_dim, data_set, left_node, right_node):
        self.parent = axis_data
        self.dim = cur_dim
        self.left_child = left_node
        self.right_child = right_node
        self.data_set = data_set

class kd_tree():
    def __init__(self, k_dim):
        self.k = k_dim
    
    def euclidean_distance(self, a, b):
        distance = 0
        for i,j in zip(a,b):
            distance+= (i - j)**2
        return math.sqrt(distance)

    def add_node(self, data_set, level):
        data_len = len(data_set)
        cur_dim = level % self.k # start from level 0 (root point).
     
        if data_len == 1: # only one data point is stored at the parent node. both child nodes store None. 
            return Node(data_set[0], cur_dim, data_set, None, None)
        data_set = sorted(data_set, key=lambda x: x[cur_dim]) # have to sort every time, because dimention of axis is always changed.
        
        if data_len == 2: # In case of two data points, bigger data point is stored at the parent node and second data point is stored at the left child node. 
            return Node(data_set[1], cur_dim, data_set, self.add_node(data_set[:1], level + 1), None)
        
        left_mid = len(data_set)//2
        right_mid = len(data_set)//2 + 1
        # median data point is stored at the parent node, the left child node stores data points under median point, the right childe node stores data points over median point.
        return Node(data_set[left_mid], cur_dim, data_set, self.add_node(data_set[:left_mid], level + 1), self.add_node(data_set[right_mid:], level + 1))

    def construct_kdtree(self, data_set):
        kdtree = self.add_node(data_set, 0)
        return kdtree

    def search(self, x, kdtree):
        # find closest neighbor data point. And calculate distance.
        cur_node = kdtree
        while True:
            if cur_node.parent[cur_node.dim] > x[cur_node.dim]:
                if cur_node.left_child != None:
                    cur_node = cur_node.left_child
                else:
                    break
            else:
                if cur_node.right_child != None:
                    cur_node = cur_node.right_child
                else:
                    break
       
        return cur_node.parent, self.euclidean_distance(x, cur_node.parent)
    
    def preorder(self, store_node, cur_node, level):
        # traversal tree.
        store_node.append([level,cur_node.parent])
        if cur_node.left_child != None:
            self.preorder(store_node, cur_node.left_child, level+1)
        else:
            store_node.append([level+1, None])
        if cur_node.right_child != None:
            self.preorder(store_node, cur_node.right_child, level+1)
        else:
            store_node.append([level+1, None])
        return store_node

    def print_all(self, kd_tree):
        store_node = []
        cur_node = kd_tree
        level = 0
        store_node = self.preorder(store_node, cur_node, level)
        print(store_node)

def main():
    kdtree = kd_tree(2)
    list_temp=[]
    gen_x = np.random.randint(100, size=10)
    gen_y = np.random.randint(100, size=10)

    for i, j in zip(gen_x, gen_y):
        list_temp.append([i,j])
    print(list_temp)
    print(list_temp[0:5])
    print()
    ##list_temp = [[7,2],[5,4],[9,6],[2,3],[4,7],[8,1]]
    kd = kdtree.construct_kdtree(list_temp)
    kdtree.print_all(kd)
    x = [10,2]
    print(kdtree.search(x,kd))
if __name__ == '__main__':
    main()