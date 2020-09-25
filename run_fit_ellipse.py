#!/usr/bin/env python3
import numpy as np
from numpy.random import rand as rand
import matplotlib.pyplot as plt

from fitEllipse import fit_ellipse

# rotation matrix
def rotation_matrix(theta):
    st = np.sin(theta)
    ct = np.cos(theta)
    return np.matrix([[ct, st], [-st, ct]])


# test the fitting on randomly generated ellipse data
n_samples = 40
for sample_i in range(0, n_samples):
    arc = 2.0
    R = np.arange(0, arc * np.pi, 0.01)
    n = len(R)

    # random ellipse data
    x_0 = 0.1 + 1.5 * rand() - 0.1 * rand() * rand(n)
    y_0 = 0.1 + 1.5 * rand() - 0.1 * rand() * rand(n)
    y_s = 0.1 + 1.5 * rand() - 0.1 * rand() * rand(n)
    x_s = 0.1 + 1.5 * rand() - 0.1 * rand() * rand(n)
    x = x_0 + x_s * np.cos(R) + 0.01 * rand(n)
    y = y_0 + y_s * np.sin(R) + 0.01 * rand(n)

    # random rotation
    theta = rand() * np.pi * 2.0
    rot = rotation_matrix(theta)

    # apply rotation matrix
    for i in range(0, n):
        xy = np.matrix([x[i], y[i]]).T
        xy = np.dot(rot, xy)
        x[i], y[i] = xy[0], xy[1]

    # fit an ellipse to the above data
    a, b, center0, center1, phi = fit_ellipse(x, y)
    center, axes = (center0, center1), (a, b)

    # generate points on the fitted ellipse
    a, b = axes
    xx = center[0] + a * np.cos(R) * np.cos(phi) - b * np.sin(R) * np.sin(phi)
    yy = center[1] + a * np.cos(R) * np.sin(phi) + b * np.sin(R) * np.cos(phi)

    # plot the data points and the fitted ellipse
    plt.figure(0)
    plt.plot(x, y, color='blue', label='points')
    plt.plot(xx, yy, '+', color='red', label='fitted ellipse', linewidth=2.0)
    plt.legend()
    plt.axes().set_aspect('equal', 'datalim')
    plt.savefig('plot' + str(sample_i) + '.png')
    plt.clf()
