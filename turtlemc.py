"""
All the maths to move the Turtle
"""

import math
import sys
sys.path.append("./quat/cgkit/light/")
from cgtypes import *

class Turtle:

    def __init__(self, block='GRASS', pos = [0,0,0], dir=[1,0,0], rot=[0,-1,0]):
        self.x, self.y, self.z = pos
        self._pos = vec3(pos)
        self._dir = vec3(dir)
        self._rot = vec3(rot)
       
        self._tilepos = vec3(int(round(self.x)), int(round(self.y)), int(round(self.z)))
        # unit quaternion to describe direction
        # self._qdir = quat(self.w, self.x, self.y, self.z)
        # another unit quaternion to describe left-right rotation axis
        # self._qrot = quat(self.wr, self.xr, self.yr, self.zr)
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

    # set or get direction vector of Turtle
    def setDir(self, x, y, z):
        self._dir = vec3(x, y, z)
        
    def getDir(self):
        return self._dir
        
   
    def turnBy(self, angle, direction='lr'):
        ''' This is at th heart of the whole class, and of the whole Turtle 3d logic. The only place where we need quaternions, but here they are really really useful'''
        if direction == 'lr':
            # no need for quat yet, set vec component to rotation axis           
            rot_axis_vec = self._rot
        else:
            # generate rotation and dir quaternions, calculate rot axis
            xr, yr, zr = self._rot
            q_rotation = quat(0, xr, yr, zr)
            xd, yd, zd = self._dir
            q_dir = quat(0, xd, yd, zd)
            q_rotation *= q_dir
            # we will need the vector component of that quat
            rot_angle, rot_axis_vec = q_rotation.toAngleAxis()

        # create a new quat for the rotation from angle and vector
        angle_rad = math.radians(angle)
        q_rotate = quat(angle_rad, rot_axis_vec)   
             
        self._dir = q_rotate.rotateVec(self._dir)
        self._dir = vec3([self.correctNearZero(coord) for coord in self._dir])
        
        # in case of tilting, we need to recalculate the rotation axis vector
        # claculation via quats
        if direction != 'lr':
            xd, yd, zd = self._dir
            qdir = quat(0, xd, yd, zd)
            qrot = qdir*q_rotation
            r_angle, r_axis_vec = qrot.toAngleAxis()
            self._rot = r_axis_vec
            
        
    # todo: give option of either id or name
    def setBlockType(self, block):
        self._blocktype = block

    def getBlockType(self):
        return self._blocktype

    def pendown(self):
        self._pendown = True

    def forward(self, steps):
        
        xdiff, ydiff, zdiff = [coord*steps for coord in self._dir]      
                       
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