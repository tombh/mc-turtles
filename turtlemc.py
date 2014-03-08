import sys
PATH_TO_MCPI = ".."
sys.path.append(PATH_TO_MCPI)
import mcpi.minecraft as minecraft
import mcpi.block as block
import math


class Turtle:

    def __init__(self,x=0,y=1,z=0,dir=0,block='GRASS'):
        self._tilepos = [int(math.floor(x)),int(math.floor(y)),int(math.floor(z))]
        self._pos = [x,y,z]
        self._dir = dir
        self._blocktype = block
        self._pendown = True

    def setTilePos(self,x,y,z):
        self._tilepos = [int(math.floor(x)),int(math.floor(y)),int(math.floor(z))]

    def getTilePos(self):
        return self._tilepos

    def setPos(self,x,y,z):
        self._pos = [x,y,z]

    def getPos(self):
        return self._pos
    
    #set Direction of Turtles in degrees
    def setDir(self, dir):
        self._dir = dir

    def turnBy(self,degree):
        dircurr = self.getDir()
        dirnew = dircurr + degree
        if dirnew >= 360:
            dirnew = dirnew - 360
        if dirnew < 0:
            dirnew = dirnew + 360
        self.setDir(dirnew)

    def getDir(self):
        return self._dir

    #todo: give option of either id or name
    def setBlockType(self, block):
        self._blocktype = block

    def getBlockType(self):
        return self._blocktype

    def pendown(self):
        self._pendown = True

    def pendown(self):
        self._pendown = False

    def forward(self, steps):
        startpos = self.getPos()        
        x,y,z = startpos
        dir = self.getDir()
        # Taking care of special angles
        if self._dir == 0:
            xdiff = steps
            zdiff = 0
        elif self._dir == 90:
            xdiff = 0        
            zdiff = steps
        elif self._dir == 270:
            xdiff = 0
            zdiff = steps*(-1)
        elif self._dir == 180:
            xdiff = steps*(-1)
            zdiff = 0
        else:
            xdiff = math.cos(math.radians(dir))*steps
            zdiff = math.sin(math.radians(dir))*steps
        # This is going to contain the tiles the turtle passes through
        # We are only recording x and z coordinates, y stays the same
        if self._pendown:
            coords = []
            if self._dir == 0:
                for i in range(steps):
                    coords.append((x+i,z)) 
            elif self._dir == 180:
                for i in range(steps):
                    coords.append((x-i,z))  
            elif self._dir == 90:
                for i in range(steps): 
                    coords.append((x,z+i))
            elif self._dir == 270:
                for i in range(steps):
                    coords.append((x,z-i))
            else:
                xdiff = math.cos(math.radians(dir))*steps
                zdiff = math.sin(math.radians(dir))*steps
                # calculate coordinates passed for each x-step forward
                xsteps = math.ceil(xdiff)
                zdiffunit = math.tan(math.radians(dir))
                for i in range(int(xsteps)):
                    coords.append((x+i,math.ceil(i*zdiffunit)))
            self._coords = coords
              
        newx = x + xdiff
        newz = z + zdiff
        self._pos = [newx,y,newz]
        self._tilepos = [int(math.floor(newx)), y, int(math.floor(newz))]
        
    
    
    

