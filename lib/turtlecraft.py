"""
Main class that provides convenience functions to Turtle
"""

# Append to the path for importing
import os
import sys
sys.dont_write_bytecode = True  # Don't create annoying .pyc files
basepath = os.path.dirname(__file__)
PROJECT_ROOT = os.path.dirname(os.path.join(basepath, "..", ".."))
sys.path.append(PROJECT_ROOT)
sys.path.append("{}/lib/deps/mcpipy".format(PROJECT_ROOT))
sys.path.append("{}/lib/deps/cgkit/cgkit/light/".format(PROJECT_ROOT))

# Place a settings.py in the project root to use your own custom values
try:
    from settings import *  # @UnusedWildImport # noqa
except ImportError:
    SERVER = 'localhost'
    PORT = 4711

import mcpi.minecraft as minecraft
import mcpi.block as block
import json
import atexit
import inspect

from turtlemc import Turtle


class Turtlecraft:

    BLOCKTYPES = ['GRASS', 'AIR', 'DIRT', 'STONE', 'TNT', 'GOLD_ORE', 'LAVA', 'MELON']

    def __init__(self, near_player=True):
        # The main Minecraft connection
        self.mc = minecraft.Minecraft.create(SERVER, PORT)
        # Either start the turtle from the world's origin or near the player
        if near_player:
            p = self.mc.player.getPos()
            x, y, z = p.x + 3, p.y - 1, p.z + 3
        else:
            x, y, z = 0, 0, 0
        self.Turtle = Turtle(position=[x, y, z])
        # Record what the turtle does for replaying and deleting blocks
        self.history = []
        # Make a note of the name of the script that was used to instantiate this object
        self.entry_script = os.path.basename(inspect.stack()[-1][1])
        # Once all turtling has been completed write all the activity to file
        atexit.register(self.write_history)

    def fd(self, steps):
        self.Turtle.forward(steps)
        if self.Turtle._pendown:
            for x, y, z in self.Turtle._coords:
                self.setBlock(x, y, z)

    def setBlock(self, x, y, z):
        blocktype = self.getBlockString(self.Turtle.getBlockType())
        self.mc.setBlock(x, y, z, blocktype)
        self.history.append([x, y, z, blocktype.id])

    def lt(self, angle):
        self.Turtle.turnBy(angle*(-1))

    def rt(self, angle):
        self.Turtle.turnBy(angle)

    def tilt_bk(self, angle):
        self.Turtle.turnBy(angle, 'tilt')

    def tilt_fd(self, angle):
        self.Turtle.turnBy(angle*(-1), 'tilt')

    def pu(self):
        self.Turtle._pendown = False

    def pd(self):
        self.Turtle._pendown = True

    def setBT(self, blocktype):
        self.Turtle.setBlockType(blocktype)

    def getBlockString(self, blocktype):
            return {
                'GRASS': block.GRASS,
                'AIR': block.AIR,
                'LAVA': block.LAVA,
                'MELON': block.MELON,
                'TNT': block.TNT,
                'STONE': block.STONE,
                'DIRT': block.DIRT,
                'GOLD_ORE': block.GOLD_ORE
            }.get(blocktype, block.GRASS)

    def chat(self, message):
        self.mc.postToChat(message)

    def clear(self, size):
        p = self.mc.player.getTilePos()
        self.mc.setBlocks(p.x-size, p.y-size, p.z-size, p.x+size, p.y+size, p.z+size, block.AIR.id)

    def history_file_path(self):
        return "{}/history/{}.json".format(PROJECT_ROOT, self.entry_script)

    def write_history(self):
        with open(self.history_file_path(), 'w') as outfile:
            json.dump(self.history, outfile)
