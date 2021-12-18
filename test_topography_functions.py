"""
This file is a test file for exploring several strategies to create an interesting topography.
"""

import math

import matplotlib.pyplot as plt
import numpy as np


def interpolate(a0, a1, x):
    if x < 0.0:
        return a0
    if x > 1.0:
        return a1
    return (a1 - a0) * x + a0


def randomGradient(xi, yi):
    w = 8 * 64
    s = int(w / 2)
    a = xi
    b = yi
    a *= 3284157443
    b ^= a << s | a >> w - s
    b *= 1911520717
    a ^= b << s | b >> w - s
    a *= 2048419325

    r = np.random.uniform(0.0, math.pi * 2)
    return np.sin(r), np.cos(r)


def dotGridGradient(xi, yi, x, y):
    vx, vy = randomGradient(xi, yi)
    dx = x - xi
    dy = y - yi
    return dx * vx + dy * vy


def perlin(x, y):
    sx = x
    sy = y
    n0 = dotGridGradient(x, y, x, y)
    n1 = dotGridGradient(x + 1, y, x, y)
    xi0 = interpolate(n0, n1, sx)
    n0 = dotGridGradient(x, y + 1, x, y)
    n1 = dotGridGradient(x + 1, y + 1, x, y)
    xi1 = interpolate(n0, n1, sx)
    return interpolate(xi0, xi1, sy)


def gen_surface(nx, ny):
    return [[perlin(xi, yi) for xi in range(nx)] for yi in range(ny)]


def flatten(Z, x, y):
    return [Z[y][x] for x, y in zip(x, y)]


if __name__ == '__main__':
    nx = 20
    ny = 20

    _x = np.arange(nx)
    _y = np.arange(ny)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()

    bottom = np.zeros_like(x)
    width = depth = 1

    fig = plt.figure(figsize=(14, 14))
    n = 1
    for i in range(1, n + 1):
        print(f'{i}/{n}')
        top = gen_surface(nx, ny)
        top = flatten(top, x, y)
        print(top)

        ax = fig.add_subplot(int(np.sqrt(n)), int(np.sqrt(n)), i, projection='3d')
        ax.bar3d(x, y, bottom, width, depth, top, shade=True)
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.set_zticklabels([])
        ax.axis('off')
        ax.set_zlim(0, 16)

    plt.show()
