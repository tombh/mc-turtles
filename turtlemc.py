"""
All the maths to move the Turtle
"""
import math


class Turtle:

    def __init__(self, x=0, y=1, z=0, dir=0, block='GRASS'):
        self._tilepos = [int(math.floor(x)), int(math.floor(y)), int(math.floor(z))]
        self._pos = [x, y, z]
        self._dir = dir
        self._blocktype = block
        self._pendown = True

    def setTilePos(self, x, y, z):
        self._tilepos = [int(round(x)), int(round(y)), int(round(z))]

    def getTilePos(self):
        return self._tilepos

    def setPos(self, x, y, z):
        x = self.correctNearZero(x)
        z = self.correctNearZero(z)
        self._pos = [x, y, z]

    def getPos(self):
        return self._pos

    #set Direction of Turtles in degrees
    def setDir(self, dir):
        self._dir = dir

    def turnBy(self, degree):
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

    def forward(self, steps):
        startpos = self.getPos()
        x, y, z = startpos
        dir = self.getDir()

        angle_rad = math.radians(dir)
        xdiff = self.correctNearZero(math.cos(angle_rad))*steps
        zdiff = self.correctNearZero(math.sin(angle_rad))*steps

        if self._pendown:
            coords = []

            xsteps = math.fabs(xdiff)
            zsteps = math.fabs(zdiff)
            if xsteps >= zsteps:
                count = int(round(xsteps))
                sign = self.getSign(xdiff)
                zincr = self.getIncrement(zdiff, count)
                for i in range(count):
                    coords.append((int(x+i*sign), int(round(z+zincr*i))))
            else:
                count = int(round(zsteps))
                sign = self.getSign(zdiff)
                xincr = self.getIncrement(xdiff, count)
                for i in range(count):
                    coords.append((int(round(x+xincr*i)), int(z+i*sign)))

            self._coords = coords

        newx = self.correctNearZero(x + xdiff)
        newz = self.correctNearZero(z + zdiff)
        self._pos = [newx, y, newz]
        self._tilepos = [int(round(newx)), y, int(round(newz))]

    def correctNearZero(self, x):
        xabs = abs(x)
        xabsfloor = math.floor(xabs)
        if xabs - xabsfloor < 0.0001:
            x = xabsfloor if x >= 0 else xabsfloor*(-1)
        return x

    def getIncrement(self, x, orthsteps):
        if self.correctNearZero(x) == 0:
            incr = 0
        else:
            incr = x/orthsteps
        return incr

    def getSign(self, x):
        return 1 if x >= 0 else -1
