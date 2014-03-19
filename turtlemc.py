"""
All the maths to move the Turtle
"""

import math
from settings import MCPIPY_PATH
import sys
sys.path.append(MCPIPY_PATH)
from mcpi.vec3 import Vec3

class Turtle:

    def __init__(self, x=0, y=1, z=0, block='GRASS', dir=[0,0],):
        self._tilepos = Vec3(int(round(x)), int(round(y)), int(round(z)))
        self._pos = Vec3(x, y, z)
        self._dir = dir
        self._blocktype = block
        self._pendown = True

    def setTilePos(self, x, y, z):
        self._tilepos = Vec3(int(round(x)), int(round(y)), int(round(z)))

    def getTilePos(self):
        return self._tilepos

    def setPos(self, x, y, z):
        self.x = self.correctNearZero(x)
        self.y = self.correctNearZero(y)
        self.z = self.correctNearZero(z)
        self._pos = Vec3(self.x, self.y, self.z)

    def getPos(self):
        return self._pos

    # set or get direction of Turtle (as a list consisting of 
    # horiz. and vert. component in degrees)
    def setDir(self, dir):
        self._dir = dir
        
    def getDir(self):
        return self._dir
        
    # rotates Turtle in horizontal or vertical direction
    def turnBy(self, angle, direction='horizontal'):
        dir_index = 0 if direction == 'horizontal' else 1
        dircurr = self.getDir()[dir_index]
        dirnew = dircurr + angle
        if dirnew >= 360:
            dirnew = dirnew - 360
        if dirnew < 0:
            dirnew = dirnew + 360
        self._dir[dir_index] = dirnew

    # todo: give option of either id or name
    def setBlockType(self, block):
        self._blocktype = block

    def getBlockType(self):
        return self._blocktype

    def pendown(self):
        self._pendown = True

    def forward(self, steps):
        startpos = self.getPos()
        self.x, self.y, self.z = startpos
        dir = self.getDir()
        print self._dir
        
        angle_hori = math.radians(dir[0])
        angle_vert = math.radians(dir[1])
        xdiff = self.correctNearZero(math.cos(angle_hori))*self.correctNearZero(math.cos(angle_vert))*steps
        ydiff = self.correctNearZero(math.sin(angle_vert))*steps
        zdiff = self.correctNearZero(math.sin(angle_hori))*self.correctNearZero(math.cos(angle_vert))*steps
        
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

        self._pos += Vec3(xdiff, ydiff, zdiff)
        self.x, self.y, self.z = self._pos
        self._tilepos = Vec3(int(round(self.x)), int(round(self.y)), int(round(self.z)))

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