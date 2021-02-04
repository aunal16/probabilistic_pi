# IMPORT LIBRARIES
from random import seed
from random import random
import matplotlib.pyplot as plt
import math

# SET SEED (random)
seed(13)

# SET GLOBAL VARIABLES
N = 10
pairs = list()
distances = list()

fig, ax = plt.subplots(figsize=(4,4))
marker_size = 5

# DEFINE FUNCTIONS
def generate_points(num_of_points):
    
    n = num_of_points
    
    for _ in range(N):
        x = random()
        y = random()

        pairs.append((x,y))

def plot_circle():
    circle = plt.Circle((0.5,0.5), 0.5, color = 'g', fill = False)
    ax.add_patch(circle)

def calc_distances():
    for i in range(len(pairs)):
        dist = math.sqrt((0.5 - pairs[i][0])**2 + (0.5 - pairs[i][1])**2)
        distances.append(dist)

if __name__ == "__main__":
    generate_points(N)
    plot_circle()
    plt.scatter(*zip(*pairs), s = marker_size)

    calc_distances()

    outside = sum(map(lambda x : x > 0.5, distances))
    inside = N - outside

    print("Inside:", inside, "Outside:", outside)
    
    plt.xlabel("x");    plt.ylabel("y");
    plt.xlim((0,1));    plt.ylim((0,1));
    plt.show()
