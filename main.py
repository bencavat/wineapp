from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys

np.random.seed(1)


def closest_wine(var_data, belief):
    #print(belief.shape)
    print(var_data.shape)

    error = var_data - belief
    print(error)
    absolute_sum_error = np.sum(np.abs(error), axis=0)
    return var_data[:, np.argmin(absolute_sum_error.T)]


def stochastic_belief(belief):
    return belief + np.random.normal(0,0.1)


def update_belief(var_data, belief):
    pass


size = width, height = 320, 240
black = 0, 0, 0

var_names = ['Acidity', 'Body', 'Alcohol', 'Type']

num_dummy_wines = 20

var_data = np.abs(np.random.normal(0,1,(4, num_dummy_wines)))
var_data[3,:] = np.random.randint(0,2, (1, num_dummy_wines))


global_belief = np.array([[0.2], [0.7], [1], [1]])

individual_belief = stochastic_belief(global_belief)

selected_wine = closest_wine(var_data[0:3,:], global_belief[0:3,:])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(var_data[0,:], var_data[1,:], var_data[2,:])
ax.scatter([0.2], [0.7], [1])
ax.scatter(selected_wine[0], selected_wine[1], selected_wine[2])

ax.set_xlabel('Acidity')
ax.set_ylabel('Body')
ax.set_zlabel('Alcohol')
plt.show()
