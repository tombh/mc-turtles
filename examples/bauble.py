import sys
sys.path.append("../lib")
from turtlecraft import Turtlecraft

T = Turtlecraft()

T.pu()
T.tilt_bk(90)
T.fd(50)
T.tilt_fd(90)
T.pd()


def circle():
    for i in range(60):
        T.tilt_fd(6)
        T.fd(2)

for i in range(30):
    circle()
    T.rt(6)
    T.setBT('MELON')
    circle()
    T.rt(6)
    T.setBT('TNT')
