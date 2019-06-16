import math
mean = 205*49
std = math.sqrt(49)*15

def cdf(mean, std, x):
    return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))



print("{:.4f}".format(cdf(mean, std, 9800)))
