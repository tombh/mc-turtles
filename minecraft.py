import sys
PATH_TO_MCPI = ".."
sys.path.append(PATH_TO_MCPI)

import mcpi.minecraft
import mcpi.block as block

# Globals
mc = mcpi.minecraft.Minecraft.create()
player = mc.player
cursor = player.getPos()
block_type = block.GRASS


def clear(size):
    mc.setBlocks(-size, -size, -size, size, size, size, block.AIR.id)


def chat(message):
    mc.postToChat(message)


def draw():
    mc.setBlock(cursor.x, cursor.y, cursor.z, block_type)


def setBlockType(block_type_int):
    global block_type
    block_type = block_type_int


def forward(length):
    for move in range(0, length):
        cursor.x = cursor.x + 1
        draw()


def backward(length):
    for move in range(0, length):
        cursor.x = cursor.x - 1
        draw()


def left(length):
    for move in range(0, length):
        cursor.z = cursor.z - 1
        draw()


def right(length):
    for move in range(0, length):
        cursor.z = cursor.z + 1
        draw()


def up(length):
    for move in range(0, length):
        cursor.y = cursor.y + 1
        draw()


def down(length):
    for move in range(0, length):
        cursor.y = cursor.y - 1
        draw()
