"""
All the maths to move the Turtle
"""

import math
import sys
sys.path.append("./quat/cgkit/light/")
from cgtypes import *

class Turtle:

    def __init__(self, block='GRASS', qdir=[0,1,0,0], qrot=[0,0,-1,0]):
        self.w, self.x, self.y, self.z = qdir
        self.wr, self.xr, self.yr, self.zr = qrot
        self._pos = vec3(self.x, self.y, self.z)
        self._tilepos = vec3(int(round(self.x)), int(round(self.y)), int(round(self.z)))
        # unit quaternion to describe direction
        self._qdir = quat(self.w, self.x, self.y, self.z)
        # another unit quaternion to describe left-right rotation axis
        self._qrot = quat(self.wr, self.xr, self.yr, self.zr)
        self._blocktype = block
        self._pendown = True
    
    # default for describing position is now quaternion, although w is always 0 and we could write it as a vector, too - might change it again
    def setPos(self, x, y, z):
        self.x = self.correctNearZero(x)
        self.y = self.correctNearZero(y)
        self.z = self.correctNearZero(z)
        self._pos = vec3(self.x, self.y, self.z)
        
    def getPos(self):
        return self._pos

    def getTilePos(self):
        self._tilepos = vec3(int(round(self.x)), int(round(self.y)), int(round(self.z)))
        return self._tilepos

    # set or get direction of Turtle (as a quaternion)
    def setDir(self, quat):
        self._dir = quat
        
    def getDir(self):
        return self._qdir
        
    # adding quaternions! rotates turtle left right, or tilts forward/backwards
    def turnBy(self, angle, direction='lr'):
        if direction == 'lr':
            rot_axisq = self._qrot
        else:
            rot_axisq = self._qdir*self._qrot 
        
        q_angle_axis = rot_axisq.toAngleAxis()
        axis_vec = q_angle_axis[1]
        
        self._qdir = quat.fromAngleAxis(self._qdir,math.radians(angle),axis_vec)
        


    # todo: give option of either id or name
    def setBlockType(self, block):
        self._blocktype = block

    def getBlockType(self):
        return self._blocktype

    def pendown(self):
        self._pendown = True

    def forward(self, steps):
        
        # something missing here, should be easy, just no time anymore! 
        # multiply get x,y and z diffd from the new direction quat
        
        print 'xdiff: '+str(xdiff)
        print 'ydiff: '+str(ydiff)
        print 'zdiff: '+str(zdiff)
        
        if self._pendown:
            diff = [xdiff, ydiff, zdiff]
            abs_diff = [abs(x) for x in diff]
            maxdiff = max(abs_diff)
            count = int(round(maxdiff))
            # get index of the maximum value, picks the first occurence
            max_idx = abs_diff.index(maxdiff)
            
            coords = []
            
            coord_incr = self.getCoord_incr(max_idx,diff,count)  
            xincr, yincr, zincr = coord_incr   
            for i in range(count):
                '''print x
                print i*xincr
                print round(x+i*xincr)
                print int(round(x+i*xincr))'''
                coords.append((int(round(self.x+i*xincr)), int(round(self.y+i*yincr)), int(round(self.z+i*zincr))))
                         
            print coords
         
            self._coords = coords

        self._pos += vec3(xdiff, ydiff, zdiff)
        self.x, self.y, self.z = self._pos
        self._tilepos = vec3(int(round(self.x)), int(round(self.y)), int(round(self.z)))

    def correctNearZero(self, x):
        xabs = abs(x)
        xabsfloor = math.floor(xabs)
        if xabs - xabsfloor < 0.0001:
            x = xabsfloor if x >= 0 else xabsfloor*(-1)
        return x
        
    def getIncrement(self, diff, orthsteps):
        if self.correctNearZero(diff) == 0:
            incr = 0
        else:
            incr = diff/orthsteps
        return incr

    def getSign(self, x):
        return 1 if x >= 0 else -1
    
    def getCoord_incr(self,max_idx,diff,count):
        coord_incr = []
        for i in [0,1,2]:
            if i == max_idx:
                coord_incr.append(self.getSign(diff[i]))
            else:
                coord_incr.append(self.getIncrement(diff[i], count)) 
        return coord_incr