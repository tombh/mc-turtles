import sys
PATH_TO_MCPI = ".."
sys.path.append(PATH_TO_MCPI)
import mcpi.minecraft as minecraft
import mcpi.block as block
from turtlemc import Turtle

class Turtlecraft:
    
    BLOCKTYPES = ['GRASS','AIR','DIRT','STONE','TNT','GOLD_ORE','LAVA','MELON']

    def __init__(self,x=0,y=1,z=0,dir=0,block = 'GRASS'):
        self.Turtle = Turtle(x,y,z,dir,block)
        self.mc = minecraft.Minecraft.create()
    
    def fd(self,steps):
        self.Turtle.forward(steps)
        if self.Turtle._pendown:
            xpos,y,zpos = self.Turtle.getPos()
            blocktype = self.getBlockString(self.Turtle.getBlockType())
            for x,z in self.Turtle._coords:
                self.mc.setBlock(x,y,z,blocktype)

    def lt(self,degrees):
        self.Turtle.turnBy(degrees*(-1))

    def rt(self,degrees):
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
        self.mc.setBlocks(-size, 1, -size, size, 1, size, block.AIR.id)