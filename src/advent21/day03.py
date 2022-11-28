import numpy as np

def bool_array_to_int(a: np.ndarray) -> int:
    return int(''.join([str(int(val)) for val in a]), 2)


def run():
    report = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010',
              '01010']
    nrep = len(report)
    rep_array = np.array([[int(character) for character in item] for item in report])
    gamma = bool_array_to_int(np.sum(rep_array, axis=0) > nrep/2)
    epsilon = bool_array_to_int(np.sum(rep_array, axis=0) < nrep/2)
    return gamma*epsilon

