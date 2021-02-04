# IMPORT LIBRARIES
from random import seed
from random import random
import matplotlib.pyplot as plt
import math

# SET SEED (random)
seed(13)

# SET GLOBAL VARIABLES
N = 10**5
radius = 0.5
origin = [0.5, 0.5]
pairs, distances = list(), list()
marker_size = 1

# DEFINE FUNCTIONS
def generate_points(num_of_points):
    for _ in range(num_of_points):
        x = random()
        y = random()
        pairs.append((x,y))

def plot_circle():
    circle = plt.Circle((0.5,0.5), radius, color = 'g', fill = False)
    ax.add_patch(circle)

def calc_distances():
    for i in range(len(pairs)):
        dist = math.sqrt((0.5 - pairs[i][0])**2 + (0.5 - pairs[i][1])**2)
        distances.append(dist)

if __name__ == "__main__":

    fig, ax = plt.subplots(figsize=(4,4))
    generate_points(N)
    plot_circle()
    plt.scatter(*zip(*pairs), s = marker_size)

    calc_distances()

    outside = sum(map(lambda x : x > radius, distances))
    inside = N - outside

    print("Inside:", inside, "Outside:", outside)
    ratio = inside / N
    pi = ratio * 4
    pi_str = '{0:.15g}'.format(ratio*4)
    print("Monte Carlo Integration Result: \u03c0 =", pi_str)
    print("Exact value of \u03c0 =", math.pi)
    print("Error:", (pi - math.pi)/math.pi*100,"%")
    
    plt.xlabel("x");    plt.ylabel("y");
    plt.xlim((0,1));    plt.ylim((0,1));
    plt.show()
