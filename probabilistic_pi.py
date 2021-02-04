# IMPORT LIBRARIES
from random import seed
from random import random
import matplotlib.pyplot as plt
import math

# SET SEED (random)
seed(13)

# SET GLOBAL VARIABLES
N = 10
radius = 0.5
origin = [0.5, 0.5]
marker_size = 1

# DEFINE FUNCTIONS
def generate_points(num_of_points):
    for _ in range(num_of_points):
        x = random()
        y = random()
        pairs.append((x,y))

def plot_circle():
    circle = plt.Circle((origin[0],origin[1]), radius, color = 'g', fill = False)
    ax.add_patch(circle)

def calc_distances():
    for i in range(len(pairs)):
        dist = math.sqrt((origin[0] - pairs[i][0])**2 + (origin[1] - pairs[i][1])**2)
        distances.append(dist)

# MAIN PROGRAM
if __name__ == "__main__":
    for i in range(1, 6):
        n = N ** i - 1

        # Create empty lists to hold (x,y) pairs and their distances to the origin
        pairs, distances = list(), list()
        # Create new figure for each n
        fig, ax = plt.subplots(num = i, figsize=(4,4)) 
        
        # Generate (x,y) pairs and calculate distances
        generate_points(n)
        calc_distances()
       
        # Plot circle and points
        plot_circle()
        plt.scatter(*zip(*pairs), s = marker_size, color = "orange")

        # Calculate the ratio of the areas
        outside = sum(map(lambda x : x > radius, distances))
        inside = n - outside
        ratio = inside / n
        pi = ratio * 4.0

        print("\nN=",n,"\n------------------------------------------------------")
        print("Inside:", inside, "Outside:", outside) 
        print("Monte Carlo Integration Result: \u03c0 =", '{0:.15g}'.format(pi))
        print("Exact value of \u03c0 =", math.pi)
        print("Error:", abs(pi - math.pi)/math.pi*100,"%")
        print("\n***Close this plot to move onto the next N value")
        
        # Plotting
        plt.xlabel("x");    plt.ylabel("y");    plt.title("N = " + str(n))
        plt.xlim((0,1));    plt.ylim((0,1));
        plt.text(0.025, 0.94, "Error: " + str(abs(pi - math.pi)/math.pi*100) + "%", bbox=dict(facecolor='red', alpha=0.5))
        plt.show()
