#!/usr/bin/python
"""
Based on Gregor Lingl's Python demos: https://code.google.com/p/python-turtle-demo/
"""
import sys
sys.path.append("../lib")
from turtlecraft import Turtlecraft

T = Turtlecraft()


# Visual Modeling with Logo: A Structural Approach to Seeing
# by James Clayson
# Koch curve, after Helge von Koch who introduced this geometric figure in 1904
# p. 146
def fractalgon(n, rad, lev, dir):
    import math

    # if dir = 1 turn outward
    # if dir = -1 turn inward
    edge = 2 * rad * math.sin(math.pi / n)
    T.pu()
    T.fd(rad)
    T.pd()
    T.tilt_fd(180 - (90 * (n - 2) / n))
    for i in range(n):
        fractal(edge, lev, dir)
        T.tilt_fd(360 / n)
    T.tilt_bk(180 - (90 * (n - 2) / n))
    T.pu()
    T.bk(rad)
    T.pd()


# p. 146
def fractal(dist, depth, dir):
    if depth < 1:
        T.fd(dist)
        return
    fractal(dist / 3, depth - 1, dir)
    T.tilt_bk(60 * dir)
    fractal(dist / 3, depth - 1, dir)
    T.tilt_fd(120 * dir)
    fractal(dist / 3, depth - 1, dir)
    T.tilt_bk(60 * dir)
    fractal(dist / 3, depth - 1, dir)

fractalgon(3, 50, 4, 1)
