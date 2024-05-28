import numpy as np
import torch

# Python function
def ivim(params, b_values):
    # single-coil magnitude signal (at b=0)
    S0 = params[0]
    Dp = params[1]
    Fp = params[2]
    Dt = params[3]
    # single-coil magnitude signal (at non-zero b-value)
    sig = S0 * (Fp * np.exp(-b_values * (Dp + Dt)) + (1 - Fp) * np.exp(-b_values * Dt))  # measured "magnitude" signals
    return sig

# PyTorch function
def ivim_pt(params, b_values):
    # single-coil magnitude signal (at b=0)
    S0 = params[:, 0].unsqueeze(1)
    Dp = params[:, 1].unsqueeze(1)
    Fp = params[:, 2].unsqueeze(1)
    Dt = params[:, 3].unsqueeze(1)
    # single-coil magnitude signal (at non-zero b-value)
    X = S0 * (Fp * torch.exp(-b_values * (Dp + Dt)) + (1 - Fp) * torch.exp(-b_values * Dt))  # measured "magnitude" signals
    return X
