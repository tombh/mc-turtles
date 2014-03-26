"""
All the maths to move the Turtle
"""

import math
from cgtypes import vec3, quat


class Turtle:

    def __init__(self, position=[0, 0, 0], direction=[1, 0, 0], rotation=[0, -1, 0]):
        """
        `position': The [x, y, z] coordinate position of the turtle in Euclidean space.
        `direction': The [i, j, k] unit vector for the turtle's direction.
        `rotation': The [i, j, k] unit vector for the turtle's rotation (direction the shell faces)
        """
        self._pos = self.setPos(*position)  # Floating point representation of turtle's position
        self._tilepos = self.getTilePos()  # Integer representation of turtle's position
        self._dir = self.setDir(*direction)
        self._rot = vec3(rotation)
        self._blocktype = 'GRASS'
        self._pendown = True

    def setPos(self, x, y, z):
        self.x = self.correctNearZero(x)
        self.y = self.correctNearZero(y)
        self.z = self.correctNearZero(z)
        self._pos = self.getPos()
        return self._pos

    def getPos(self):
        return vec3(self.x, self.y, self.z)

    def getTilePos(self):
        return vec3(int(round(self.x)), int(round(self.y)), int(round(self.z)))

    def setDir(self, i, j, k):
        self._dir = vec3([self.correctNearZero(coord) for coord in [i, j, k]])
        return self._dir

    def getDir(self):
        return self._dir

    def turnBy(self, angle, direction='lr'):
        """
        Crucial function for turtle movement - turtle rotating around axis that depends on both
        type of movement and turtle's direction and rotation - using vector multiplication and
        in one place quaternions.
        """
        if direction == 'lr':
            # Left-right movement is around the rotation axis.
            rot_axis_vec = self._rot
        elif direction == 'tilt':
            # Tilting up or down occurs around the axis perpendicular to the direction vector
            # and the rotation axis (ie. the cross product of the two vectors).
            rot_axis_vec = self._rot.cross(self._dir)
            # Recalculate the rotation axis vector. This is the cross product of the newly
            # calulated direction vector and the rotation vector we just used.
            self._rot = self._dir.cross(rot_axis_vec)
        else:
            raise RuntimeError("Unsuppoorted turning direction")

        # Using the angle and the rotation axis unit vector, we create a quaternion for the
        # rotation.
        # See http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation for more info.
        angle_rad = math.radians(angle)
        q_rotate = quat(angle_rad, rot_axis_vec)

        # Use the quaternion to rotate the direction vector around the rotation axis by the given
        # angle.
        new_dir_vec = q_rotate.rotateVec(self._dir)
        self._dir = self.setDir(*new_dir_vec)

    # TODO: give option of either id or name
    def setBlockType(self, block):
        self._blocktype = block

    def getBlockType(self):
        return self._blocktype

    def pendown(self):
        self._pendown = True

    def forward(self, steps):
        """
        Generate a list of integer coordinates that represent a forward movement along
        the current direction.
        """
        # coords is a list of all the steps that the turtle needs to take
        coords = []
        # Split the number of steps into increasingly larger distances, starting with 1 and ending
        # with the final destination
        for i in range(steps):
            # Multiply the current step distance by the direction unit vector
            # and round down to an integer.
            coords.append([int(round(coord + i*coord)) for coord in self._dir])
        self._coords = coords
        self._pos += vec3(*[steps*coord for coord in self._dir])
        self.x, self.y, self.z = self._pos
        self._tilepos = self.getTilePos()

    def correctNearZero(self, x):
        xabs = abs(x)
        xabsfloor = math.floor(xabs)
        if xabs - xabsfloor < 0.0001:
            x = xabsfloor if x >= 0 else xabsfloor*(-1)
        return x
