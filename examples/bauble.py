import sys
sys.path.append("..")
from turtlecraft import Turtlecraft

T = Turtlecraft('TNT')

for i in range(30):
    circle()
    T.rt(6)
    T.setBT('MELON')
    circle()
    T.rt(6)
    T.setBT('TNT')
    
def circle():
    for i in range(60):
        T.tilt_fd(6)
        T.fd(2)

