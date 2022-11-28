import numpy as np

def run():
    positions = np.array([16,1,2,0,4,2,7,1,2,14])
    targets = np.arange(17)
    tar_a = np.tile(targets, (len(positions), 1))
    pos_a = np.tile(positions, (len(targets), 1)).transpose()
    distances = np.abs(tar_a-pos_a)
    fuel_needs = np.sum(distances, axis=0)
    return fuel_needs.min()
