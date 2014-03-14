import sys
sys.path.append("..")
from turtlecraft import Turtlecraft
T = Turtlecraft()


def spiral(n, length):
    angle = 360.0/n
    for i in range(n):
        T.fd(length)
        T.lt(angle)
        angle = angle - 0.1

spiral(300, 1)
