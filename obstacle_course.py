from mcpi.minecraft import Minecraft
from mcpi import block
import random
from minecraftstuff import MinecraftTurtle
from mcpi import vec3

mc = Minecraft.create("localhost", 4711)



myId = mc.getPlayerEntityId("SohailM")
myPos = mc.player.getPos()
x = myPos.x
y = myPos.y
z = myPos.z



def draw_name(position):
    # create minecraft turtle
    steve = MinecraftTurtle(mc, position)

    steve.penblock(block.WOOL.id, 11)
    steve.speed(10)

    # S
    steve.backward(5)
    steve.up(90)
    steve.forward(3)
    steve.up(90)
    steve.backward(5)
    steve.down(90)
    steve.forward(3)
    steve.down(90)
    steve.backward(5)

    #
    steve.penup()
    #
    # O
    steve.backward(3)
    steve.down(90)
    steve.forward(6)
    steve.pendown()
    steve.up(90)
    steve.backward(3)
    steve.down(90)
    steve.backward(6)
    steve.down(90)
    steve.backward(3)
    steve.down(90)
    steve.backward(6)
    steve.up(180)
    steve.backward(6)

    #
    steve.penup()
    #

    # H
    steve.backward(2)
    steve.down(90)
    steve.forward(6)
    steve.down(90)
    steve.backward(8)
    steve.pendown()
    steve.forward(6)
    steve.penup()
    steve.up(90)
    steve.forward(1)
    steve.up(90)
    steve.forward(3)
    steve.pendown()
    steve.down(90)
    steve.forward(3)
    steve.up(90)
    steve.forward(3)
    steve.backward(6)


    #
    steve.penup()
    #

    steve.up(90)
    steve.backward(3)
    steve.down(90)
    steve.forward(6)
    steve.pendown()
    steve.backward(6)
    steve.up(90)
    steve.backward(4)
    steve.up(90)
    steve.backward(6)
    steve.forward(3)
    steve.down(90)
    steve.forward(3)
    steve.backward(3)
    steve.up(90)
    steve.forward(3)

    # I
    steve.penup()
    steve.down(90)
    steve.backward(3)
    steve.pendown()
    steve.backward(6)
    steve.penup()
    steve.backward(1)
    steve.up(90)
    steve.backward(6)
    steve.up(90)
    steve.backward(7)
    steve.pendown()
    steve.forward(6)
    steve.backward(3)
    steve.up(90)
    steve.backward(6)

    #
    steve.penup()
    #

    # L

    steve.backward(1)
    steve.down(90)
    steve.forward(5)
    steve.up(90)
    steve.forward(7)
    steve.up(90)
    steve.backward(7)
    steve.pendown()
    steve.forward(6)
    steve.down(90)
    steve.backward(6)


# Upon entry to the server
#mc.postToChat(mc.player.getPos())
mc.postToChat("Hello Sohail. Welcome to the Obstacle Course.")

cp1Reached = False
cp2Reached = False
cp3Reached = False


spawnX = -.50
spawnY = 0.0
spawnZ = 2.42

mc.player.setPos(spawnX, spawnY, spawnZ)


while(True):
    currentPos = mc.player.getPos()
    curX = currentPos.x
    curY = currentPos.y
    curZ = currentPos.z

    if (curZ > 13.5 and cp1Reached == False):
        mc.postToChat("Checkpoint 1 Reached")
        cp1Reached = True
        spawnZ = 13.5

    if (curZ > 35.8 and cp2Reached == False):
        mc.postToChat("Checkpoint 2 Reached")
        cp2Reached = True
        spawnZ = 35.8
        
    if (curZ > 49 and cp3Reached == False):
        mc.postToChat("CONGRATULATIONS! YOU'VE BEAT THE OBSTACLE COURSE!")
        cp3Reached = True
        spawnZ = 49

    if (curY < -7):
        if (cp1Reached and not cp2Reached):
            mc.postToChat("Whoopsie. Try again!")
            mc.postToChat("Respawned at Checkpoint 1")
            mc.player.setPos(spawnX, spawnY, spawnZ)
        elif (cp2Reached and not cp3Reached):
            mc.postToChat("Whoopsie. Try again!")
            mc.postToChat("Respawned at Checkpoint 2")
            mc.player.setPos(spawnX, spawnY, spawnZ)
        elif (cp3Reached):
            mc.postToChat("Winner of Obstacle Course! Respawn at Beginning")
            mc.player.setPos(-.50, 0.0, 2.42)
        else:
            mc.postToChat("Whoopsie. Try again!")
            mc.player.setPos(-.50, 0.0, 2.42)

    blockEvents = mc.events.pollBlockHits()

    for blockEvent in blockEvents:
        draw_name(vec3.Vec3(22,12,70))

