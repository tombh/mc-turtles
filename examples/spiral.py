import sys
sys.path.append("../lib")
from turtlecraft import Turtlecraft
T = Turtlecraft()

T.setBT('GOLD_ORE')


def spiral(n, length):
    angle = 360.0/n
    up = 0
    for i in range(n):
        T.fd(length)
        T.lt(angle)
        T.tilt_bk(up)
        up = up + 0.005
        angle = angle - 0.01

spiral(2000, 1)
