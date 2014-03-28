import sys
sys.path.append("../lib")
from turtlecraft import Turtlecraft

T = Turtlecraft()

for i in range(4):
    T.fd(10)
    T.rt(90)

T.tilt_bk(90)
T.fd(10)
T.tilt_fd(90)

for i in range(4):
    T.fd(10)
    T.rt(90)
    
def move_draw_down_pillar():
    T.pu()
    T.fd(10)
    T.tilt_fd(90)
    T.pd()
    T.fd(10)
    T.tilt_bk(90)
    T.rt(90)
    
def move_draw_up_pillar():
    T.pu()
    T.fd(10)
    T.tilt_bk(90)
    T.pd()
    T.fd(10)
    T.tilt_fd(90)
    T.rt(90)

move_draw_down_pillar()
move_draw_up_pillar()
move_draw_down_pillar()





    


