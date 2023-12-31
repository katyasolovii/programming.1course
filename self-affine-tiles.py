import numpy as np
import matplotlib.pyplot as plt 
import random

# Twin Dragon
A = [[1, 1],
     [-1, 1]]
D = [[0, 0], [0, 1]]
x_0 = [0.5, 0.5]
k = 100
N = 100_000

matrix = np.array(A)
vector = np.array(x_0)
result = np.dot(matrix, vector)

result_points = []
color_indexes = []

for _ in range(N):
    x = x_0.copy()    
    color_index = 0
    for i in range(k): 
        index = random.randint(0, len(D) - 1)
        x = np.dot(A, x) + D[index]
        color_index = color_index * len(D) + index
    color_indexes.append(color_index)
    result_points.append(x) 

x = [point[0] for point in result_points]
y = [point[1] for point in result_points]

plt.scatter(x, y, 
            s=1,
            c=color_indexes, 
            cmap='plasma', 
            label='точка')

plt.legend()
plt.colorbar()
plt.show()

#Gaskets
#A = [[2, 0],
#     [0, 2]]
#D = [[0, 0], [1, 0], [0, 1], [-1, -1]]
#Rocket
#A = [[3, 0], [0, 3]]
#D = [[0, 0], [1, 1], [2, 2], 
#     [-1, 0], [-2, 0], [-1, 1], 
#     [0, -1], [0, -2], [1, -1]]
#Shooter
#A = [[3, 0],
#     [0, 3]]
#D = [[0, 0], [1, 0], [2, 0], [0, 1], [0, 2], [2, 2], [4, 4], [2, 1], [1, 2]]
