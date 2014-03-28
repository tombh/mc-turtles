[![Build Status](https://travis-ci.org/tombh/mc-turtles.svg?branch=history)](https://travis-ci.org/tombh/mc-turtles)

#Minecraft Turtles

We've been using the Raspberry Pi edition of Minecraft in our [Code Club](https://www.codeclub.org.uk/) and trying out the the [MCPiPy API](http://mcpipy.com).

This is an attempt to recreate [LOGO Turtle](http://en.wikipedia.org/wiki/Logo_(programming_language)#Turtle_and_graphics) movements in Minecraft, by placing blocks along their paths. Still very basic.

(Not to be mixed up with the Turtles of the Computercraft Mod: [http://computercraft.info/wiki/Turtle](http://computercraft.info/wiki/Turtle))

MCPiPy, and therefore Minecraft Turtles, can also be used with the standard PC version of Minecraft. You will need a [CraftBukkit](https://dl.bukkit.org/downloads/craftbukkit/) server running the [Raspberry Juice plugin](http://dev.bukkit.org/bukkit-plugins/raspberryjuice/). There is a [good blog post](http://mcpipy.wordpress.com/2013/02/13/running-python-programs-without-a-raspberry-pi/) on the MCPiPy website describing the steps to do this.

##Installation
```
git clone --recursive git@github.com:tombh/mc-turtles.git
```

If your Minecraft server is a different machine from where you are using this code then you can set custom values for the server's address and port in `settings.py`. You can copy `settings.py.sample` as a starting point.

To draw a flower in your Minecraft world simply issue: `python flowers.py`

##Examples

**Hello World**
```python
from turtlecraft import Turtlecraft
T = Turtlecraft()
T.chat("Hello World")
```

**Basic Commands**
```python
# Move the turtle forward
T.fd(steps)
# Rotate the turtle right or left
T.rt(angle)
T.lt(angle)

# Set an area the size of <square_length>^3 to the AIR block
T.clear(cubic_length)

# Set the current block type. Similar to traditional turtle's pencolor()
# There are hundreds of block types, but for now just added a list of possible blocks:  
#['GRASS','AIR','DIRT','STONE','TNT','GOLD_ORE','LAVA','MELON'] 
# Default is Grass
T.setBT(blocktype)

# Pen up / pen down - While moving the turtle leaves a trail of blocks or not
T.pu()
T.pd()
```

**Accessing the turtle's properties**
```python
# It can be useful to find out where your turtle is (it's invisible so far!)
T.Turtle.getTilePos() 
#You can also set its position
T.Turtle.setPos(x,y,z)
# What block type is set at the moment?
T.Turtle.getBlockType()
# Which direction is the turtle facing?
T.Turtle.getDir()
```

##Contributing

Feedback and PRs are very welcome.

To run tests you will need some dependencies, so Virtualenv can be useful for that:

```bash
# In the project root:
virtuaenv venv
source venv/bin/activate
pip install -r requirements.txt
# To run tests:
nosetests spec/*
```

**Some more Block Types**
```python
AIR = 0
STONE = 1
GRASS = 2
DIRT = 3
COBBLESTONE = 4
WOOD_PLANK = 5
SAPLING = 6
BEDROCK = 7
WATER_FLOWING = 8
WATER = 9
LAVA_FLOWING = 10
LAVA = 11
SAND = 12
GRAVEL = 13
GOLD_ORE = 14
IRON_ORE = 15
COAL_ORE = 16
WOOD = 17
LEAVES = 18
GLASS = 20
LAPIS_ORE = 21
LAPIS = 22
SANDSTONE = 24
BED = 26
COBWEB = 30
TALL_GRASS = 31
WOOL = 35
FLOWER_YELLOW = 37
FLOWER_RED = 38
MUSHROOM_BROWN = 39
MUSHROOM_RED = 40
GOLD = 41
IRON = 42
STONE_SLAB_DOUBLE = 43
STONE_SLAB = 44
BRICK = 45
TNT = 46
BOOKSHELF = 47
MOSSY_STONE = 48
TORCH = 50
FIRE = 51
WOOD_STAIRS = 53
CHEST = 54
DIAMOND_ORE = 56
DIAMOND = 57
CRAFTING_TABLE = 58
FARMLAND = 60
FURNACE = 61
FURNACE_ACTIVE = 62
WOOD_DOOR = 64
LADDER = 65
COBBLESTONE_STAIRS = 67
IRON_DOOR = 71
REDSTONE_ORE = 73
SNOW_COVER = 78
ICE = 79
SNOW = 80
CACTUS = 81
CLAY = 82
SUGAR_CANE = 83
FENCE = 85
GLOWSTONE = 89
INVISIBLE_BEDROCK = 95
STONE_BRICK = 98
GLASS_PANE = 102
MELON = 103
FENCE_GATE = 107
GLOWING_OBSIDIAN = 246
NETHER_REACTOR_CORE = 247
UPDATE_GAME_BLOCK = 249
```


