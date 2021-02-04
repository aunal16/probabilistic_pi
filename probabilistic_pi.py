# IMPORT LIBRARIES
from random import seed
from random import random

# SET SEED (random)
seed(13)

# SET GLOBAL VARIABLES
N = 10
pairs = list()

def generate_points(num_of_points):
    n = num_of_points
    
    for _ in range(2*N):
        x = random()
        y = random()

        pairs.append((x,y))

if __name__ == "__main__":
    generate_points(N)
    print(pairs)

