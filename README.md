#Minecraft Turtles

We have been using the Minecraft Raspberry Pi edition in our Code Club and experimented with the API.

This is an attempt to recreate LOGO turtle movements in Minecraft, by placing blocks along their paths. Still very basic.

(Not to be mixed up with the Turtles of the Computercraft Mod: [http://computercraft.info/wiki/Turtle](http://computercraft.info/wiki/Turtle) )

##Examples

**Hello World**
```python
from turtlecraft import Turtlecraft
T = TurtleCraft()
T.chat("Hello World")
```

**Basic Commands**
```python
# Move the turtle forward
T.fd(steps)
# Rotate the turtle right or left
T.rt(degrees)
T.lt(degrees)

# Set an area the size of <square_length>^2 to the AIR block
T.clear(square_length)

# Set the current block type. Similar to traditional turtle's pencolor()
# There are hundreds of block types, but for now just added a list of possible blocks:  ['GRASS','AIR','DIRT','STONE','TNT','GOLD_ORE','LAVA','MELON'] 
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
T.Turtle.setPos()
# What block type is set at the moment?
T.Turtle.getBlockType()
# Which direction is the turtle facing?
T.Turtle.getDir()
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


