"""
Main class that provides convenience functions to Turtle
"""

# Place a settings.py to use your on custom values
try:
    from settings import *  # @UnusedWildImport # noqa
except ImportError:
    SERVER = 'localhost'
    PORT = 4711
    MCPIPY_PATH = '../../mcpipy'


import sys
sys.path.append(MCPIPY_PATH)
import mcpi.minecraft as minecraft
import mcpi.block as block
from turtlemc import Turtle


class Turtlecraft:

    BLOCKTYPES = ['GRASS', 'AIR', 'DIRT', 'STONE', 'TNT', 'GOLD_ORE', 'LAVA', 'MELON']

    def __init__(self):
        self.mc = minecraft.Minecraft.create(SERVER, PORT)
        p = self.mc.player.getPos()
        self.Turtle = Turtle(p.x, p.y + 10, p.z, 0, 'GOLD_ORE')

    def fd(self, steps):
        self.Turtle.forward(steps)
        if self.Turtle._pendown:
            xpos, y, zpos = self.Turtle.getPos()
            blocktype = self.getBlockString(self.Turtle.getBlockType())
            for x, z in self.Turtle._coords:
                self.mc.setBlock(x, y, z, blocktype)

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
