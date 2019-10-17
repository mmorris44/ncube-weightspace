from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import copy
import random

dimensions = 5
scale = 0.2
shift = 0.1

def plot_line(coords1, coords2):
    ax.plot([coords1[0], coords2[0]], [coords1[1], coords2[1]], [coords1[2], coords2[2]])

def plot_points(points):
    vals = []
    for i in range(3):
        vals.append([])
        for j in range(len(points)):
            vals[i].append(points[j][i])
    ax.scatter(vals[0], vals[1], vals[2], s=20)

def dif_by_one(point1, point2):
    dif = False
    for i in range(len(point1)):
        if point1[i] != point2[i]:
            if not dif: dif = True
            else: return False
    return True

def scale_points(points):
    for j in range(len(points)):
        for i in range(len(points[j])):
            points[j][i] = points[j][i] * scale

def stereo_project(point):
    for i in range(len(point) - 1):
        point[i] = (point[i] / (1 - point[-1])) + shift
    return point[0:len(point) - 1]

def dec_to_bin(num):
    return bin(num)

def bin_to_str(num):
    return str(num)[2:]

def dec_to_arr(num):
    string = bin_to_str(dec_to_bin(num))
    length = len(string)
    padding = dimensions - length
    return [0]*padding + list(map(int, list(string)))

def zeroes_to_minus_1(arr):
    for i in range(len(arr)):
        if arr[i] == 0: arr[i] = -1

# Set up figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_zlim3d(-4, 4)

# Set up points
points = []
for i in range(2**dimensions):
    point = dec_to_arr(i)
    zeroes_to_minus_1(point)
    points.append(point)
original_points = copy.deepcopy(points)

# Scale the points
scale_points(points)

# Stereo project
for i in range(len(points)):
    for j in range(dimensions - 2):
        points[i] = stereo_project(points[i])

# Add height coordinate to all points
for i in range(len(points)):
    points[i].append(random.uniform(-0.5,0.5))

# Plot points
plot_points(points)

# Plot lines
for i in range(len(points)):
    for j in range(i+1, len(points)):
        if dif_by_one(original_points[i], original_points[j]):
            plot_line(points[i], points[j])


fig.show()
