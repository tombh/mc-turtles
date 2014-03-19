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

    def __init__(self, block = 'GRASS', near_player = True, x=0, y=1, z=0, dir=[0,0]):
        self.mc = minecraft.Minecraft.create(SERVER, PORT)        
        if near_player:
            p = self.mc.player.getPos()
            self.x, self.y, self.z = p.x+3, p.y -1, p.z+3  
        else:
            self.x, self.y, self.z = x,y,z
        self.Turtle = Turtle(self.x,self.y,self.z,block)      

    def fd(self, steps):
        self.Turtle.forward(steps)
        if self.Turtle._pendown:
            xpos, ypos, zpos = self.Turtle.getPos()
            blocktype = self.getBlockString(self.Turtle.getBlockType())
            for x, y, z in self.Turtle._coords:
                self.mc.setBlock(x, y, z, blocktype)

    def lt(self, angle):
        self.Turtle.turnBy(angle*(-1))

    def rt(self, angle):
        self.Turtle.turnBy(angle)
        
    def lean_bk(self, angle):
        self.Turtle.turnBy(angle, 'vertical')   
        
    def lean_fd(self, angle):
        self.Turtle.turnBy(angle*(-1),'vertical')      

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
        
    