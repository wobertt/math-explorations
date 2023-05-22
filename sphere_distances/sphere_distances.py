"""
Let S be a spherical shell of radius 1, i.e., the set of points satisfying x^2 + y^2 + z^2 = 1. Find the average
straight line distance between two points of S.

(Assume a uniform distribution on the sphere)
"""

import matplotlib.pyplot as plt
import numpy as np


def get_point_on_sphere():
    vec = np.random.normal(size=3)
    return vec / np.linalg.norm(vec)


def get_points_arr(num_pts):
    arr = np.empty([num_pts, 3])
    for i in range(num_pts):
        arr[i] = get_point_on_sphere()
    
    return arr


def plot_points(pts_arr):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    north_pole = np.array([0, 0, 1])
    pts_arr = pts_arr.T
    col = [np.linalg.norm(pt-north_pole) for pt in pts_arr.T]

    ax.scatter(pts_arr[0], pts_arr[1], pts_arr[2], c=col)

    R = 0.5
    ax.set_xlim(-R, R)
    ax.set_ylim(-R, R)
    ax.set_zlim(-R, R)
    ax.axis('equal')
    plt.show()


def get_distances_array(num_samples):
    arr1 = get_points_arr(num_samples)
    arr2 = get_points_arr(num_samples)

    get_dist = lambda u, v: np.linalg.norm(u-v)

    distances = np.array([get_dist(u, v) for u, v in zip(arr1, arr2)])

    return distances


def plot_distances(distances, n_bins):
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.hist(distances, bins=n_bins)
    plt.show()
