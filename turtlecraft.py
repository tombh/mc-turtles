"""
Main class that provides convenience functions to Turtle
"""

# Place a settings.py to use your own custom values
try:
    from settings import *  # @UnusedWildImport # noqa
except ImportError:
    SERVER = 'localhost'
    PORT = 4711
    MCPIPY_PATH = 'mcpipy'

# Append to the path for importing
import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append("{}/{}".format(PROJECT_ROOT, MCPIPY_PATH))

import mcpi.minecraft as minecraft
import mcpi.block as block
import json
import atexit
import inspect

from turtlemc import Turtle


class Turtlecraft:

    BLOCKTYPES = ['GRASS', 'AIR', 'DIRT', 'STONE', 'TNT', 'GOLD_ORE', 'LAVA', 'MELON']

    def __init__(self):
        self.mc = minecraft.Minecraft.create(SERVER, PORT)
        p = self.mc.player.getPos()
        self.Turtle = Turtle(p.x, p.y + 10, p.z, 0, 'GOLD_ORE')
        self.history = []
        # Make a note of the name of the script that was used to instantiate this object
        self.entry_script = os.path.basename(inspect.stack()[-1][1])
        # Once all turtling has been completed write all the activity to file
        atexit.register(self.write_history)

    def fd(self, steps):
        self.Turtle.forward(steps)
        if self.Turtle._pendown:
            xpos, y, zpos = self.Turtle.getPos()
            for x, z in self.Turtle._coords:
                self.setBlock(x, y, z)

    def setBlock(self, x, y, z):
        blocktype = self.getBlockString(self.Turtle.getBlockType())
        self.mc.setBlock(x, y, z, blocktype)
        self.history.append([x, y, z, blocktype.id])

    def lt(self, degrees):
        self.Turtle.turnBy(degrees*(-1))

    def rt(self, degrees):
        self.Turtle.turnBy(degrees)

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
        self.mc.setBlocks(-size, -size, -size, size, size, size, block.AIR.id)

    def history_file_path(self):
        return "{}/history/{}.json".format(PROJECT_ROOT, self.entry_script)

    def write_history(self):
        with open(self.history_file_path(), 'w') as outfile:
            json.dump(self.history, outfile)
