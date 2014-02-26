#Minecraft Turtles

Been teaching a Code Club to primary school kids. This is an early attempt to recreate the classic turtles in Minecraft.

##Examples

**Hello World**
```python
import minecraft
chat("Hello World")
```

**Basic Commands**
```python
# Move the turtle in the implied direction
# Note that there is no rotation, it is crude 90 degree movement at the moment
forward(distance)
backward(distance)
left(distance)
right(distance)
up(distance)
down(distance)

# Set an area the size of <cubic_length>^3 to the AIR block
clear(cubic_length)

# Set the current block type. Similar to traditional turtle's pencolor()
# There are hundreds of block types
setBlockType(block_int)
```

**The 'mc' global**    
The `mc` instance is inherited from `mcpi` and has all the expected methods and properties
```python
# Player position
mc.player.getPos()
# Camera position
mc.player.setPos(x, y, z)
mc.camera.setPos(x, y, z)
# Blocks
mc.SetBlock(x, y, z, block_type)
```

**Some Block Types**
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


