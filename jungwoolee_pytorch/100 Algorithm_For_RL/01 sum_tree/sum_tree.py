import numpy as np
from collections import deque
import matplotlib.pyplot as plt

class sum_tree():
    def __init__(self, buffer_size):
        self.tree_index = buffer_size - 1 # define sum_tree leaf node index.
        self.buffer_index = 0 # define replay buffer index.

        self.replay_buffer = [0 for i in range(buffer_size)] # set rplay buffer size.
        self.array_tree = [0 for i in range((buffer_size * 2) - 1)] # set sum_tree size (double of buffer size)
        self.buffer_size = buffer_size

    def update_tree(self, index):
        # index is a starting leaf node point.
        while True:
            index = (index - 1)//2 # parent node index.
            left = (index * 2) + 1 # left child node inex.
            right = (index * 2) + 2 # right child node index
            self.array_tree[index] = self.array_tree[left] + self.array_tree[right] # sum both child node.
            if index == 0: ## if index is a root node.
                break

    def add_data(self, data, priority):
        if self.tree_index == (self.buffer_size * 2) - 1: # if sum tree index achive last index.
            self.tree_index = self.buffer_size - 1 # change frist leaf node index.
        if self.buffer_index == self.buffer_size: # if replay buffer index achive last index.
            self.buffer_index = 0 # change first index (0 zero)

        self.replay_buffer[self.buffer_index] = data # append data at current replay buffer index.
        self.array_tree[self.tree_index] = priority # append priority at current sum_tree leaf node index.

        self.update_tree(self.tree_index) # update sum_tree node. propagate from leaf node to root node.

        self.tree_index += 1 # count current sum_tree index
        self.buffer_index += 1 # count current replay buffer index
    
    def search(self, num):
        index = 0 # always start from root index.
        while True:
            left = (index * 2) + 1
            right = (index * 2) + 2
            if num <= self.array_tree[left]: # if child left node is over current value. 
                index = left                # go to the left direction.
            else:
                num -= self.array_tree[left] # if child left node is under current value.
                index = right               # go to the right direction.
            if index >= self.buffer_size - 1: # if current node is leaf node, break!
                break

        return index - (self.buffer_size - 1) # return real index in replay buffer.

def main():
    buffer_size = 8
    store_kv = {} # test 8 leaf node.
    data_list = ['a','b','c','d','e','f','g','h'] # data list
    priority_list = [5,5,10,2,8,20,15,35] # priority list
    Sum_tree = sum_tree(buffer_size) # sum_tree.

    for d,p in zip(data_list, priority_list): # add 8 test data and priority.
        Sum_tree.add_data(d,p)
    
    print(Sum_tree.array_tree) # check. array sum_tree
    print(Sum_tree.replay_buffer) # check. replay buffer.
    print()
    test_random_set = np.random.randint(100, size=10000) # generate test number set from discrete uniform distribution.
    print(test_random_set)
    for i in test_random_set: # test sampling according to sum_tree.
        index = Sum_tree.search(i)
        if str(data_list[index]) not in store_kv:
            store_kv[str(data_list[index])] = 0
        store_kv[str(data_list[index])] += 1
    print(store_kv)
    store_kv = sorted(store_kv.items(),key=lambda x : x[0])
    x = []
    y = []
    x_p = []
    y_p = []
    for i, j in store_kv:
        x.append(i)
        y.append(j)
        x_p.append(i)
        y_p.append((j/10000) * 100)
    fig, axes = plt.subplots(1, 2)
    axes[0].bar(x,y,color='red')
    axes[0].set_xlabel('data')
    axes[0].set_ylabel('count of sampling data')
    axes[0].set_title('sampling data (10000)')
    axes[1].bar(x_p,y_p,color='blue')
    axes[1].set_xlabel('data')
    axes[1].set_ylabel('percentage')
    axes[1].set_title('sampling data (10000)')
    
    plt.tight_layout()
    plt.show()
if __name__ == '__main__':
    main()
    