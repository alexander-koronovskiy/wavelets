import numpy as np
ITER = 16


# sample linear signal
def linear(n=ITER):
    return np.linspace(1, n, n)


# constant signal
def constant(n=ITER):
    return np.ones(n)


# quadratic signal
def quadratic():
    return np.array([25.0, 16.0,  9.0,  4.0,  1.0, 0.0,  1.0,  4.0])


# white noise signal
def w_noise_gen():
    mean = 0
    std = 1
    num_samples = ITER
    return np.random.normal(mean, std, size=num_samples)


# log map algorithm build
def log_map(x, r):
    return r * x * (1 - x)


# logistic map iteration signal
def do_map(
        itter_n=ITER,
        x_array=[0.1],
        r=4):
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r))
    return x_array
