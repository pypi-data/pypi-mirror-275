import numpy as np
import copy

def sigma_estimate(data, method):
    if method == 'bg':
        data_bg = copy.deepcopy(data)
        sigma_est = np.sum(data_bg) / (len(data_bg) * np.sqrt(np.pi/2))
    return sigma_est
