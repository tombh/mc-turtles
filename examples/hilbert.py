#!/usr/bin/python
"""
Based on Gregor Lingl's Python demos: https://code.google.com/p/python-turtle-demo/
"""
import sys
sys.path.append("../lib")
from turtlecraft import Turtlecraft

T = Turtlecraft()


# example derived from
# Turtle Geometry: The Computer as a Medium for Exploring Mathematics
# by Harold Abelson and Andrea diSessa
# p. 96-98
def hilbert(size, level, parity):
    if level == 0:
        return
    # rotate and draw first subcurve with opposite parity to big curve
    T.tilt_bk(parity * 90)
    hilbert(size, level - 1, -parity)
    # interface to and draw second subcurve with same parity as big curve
    T.fd(size)
    T.tilt_fd(parity * 90)
    hilbert(size, level - 1, parity)
    # third subcurve
    T.fd(size)
    hilbert(size, level - 1, parity)
    # fourth subcurve
    T.tilt_fd(parity * 90)
    T.fd(size)
    hilbert(size, level - 1, -parity)
    # a final turn is needed to make the turtle
    # end up facing outward from the large square
    T.tilt_bk(parity * 90)

hilbert(2, 4, 1)
