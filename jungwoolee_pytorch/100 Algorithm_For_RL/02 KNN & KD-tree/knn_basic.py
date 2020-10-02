import numpy as np
from collections import deque
import matplotlib.pyplot as plt
import math

class KNN():
    def __init__(self, k, data):
        self.k = k
        self.data = data

    def euclidean_distance(self, a, b):
        distance = 0
        for i,j in zip(a,b):
            distance+= (i - j)**2
        return math.sqrt(distance)

    def query(self, x):
        nn_dis=[]
        for i in self.data:
            distance = self.euclidean_distance(x, i)
            nn_dis.append([distance,i])
        nn_dis = sorted(nn_dis, key=lambda x: x[0])
        nn_dis = np.array(nn_dis)
        return nn_dis[:self.k,1:], nn_dis[:self.k,0]
    

def main():
    k = 5
    data_set = []
    gen_x = np.random.randint(1000, size=50)
    gen_y = np.random.randint(1000, size=50)
    for i, j in zip(gen_x, gen_y):
        data_set.append([i,j])
    knn = KNN(k, data_set)
    

    x = [500,500]
    nearest_neighbor, distance = knn.query(x)
    print(nearest_neighbor)
    print(distance)
if __name__ == '__main__':
    main()