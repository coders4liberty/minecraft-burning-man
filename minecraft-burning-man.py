''' Welcome to Minecraft Burning Man, a collaborative project by Coders for Liberty, to raise awareness about coding. 
## theme song: “Burn” by Rebel Inc.” youtu.be/YMrOokBvpYM
## Use the Raspberry Juice plugin on PC version http://www.stuffaboutcode.com/2014/10/minecraft-raspberryjuice-and-canarymod.html
## visit raspberrypi.org/learning/getting-started-with-minecraft-pi to get started
## Visit stuffaboutcode.com/p/minecraft-api-reference.html for a list of the Minecraft commands.
## Let the coding begin! '''

## header
## import
from mcpi.minecraft import Minecraft
from time import sleep
from mcpi import block
import math
mc = Minecraft.create()


## variables
## blocks, I skipped some. Visit stuffaboutcode.com/p/minecraft-api-reference.html for more.
air = 0
stone = 1
grass = 2
dirt = 3
cobblestone = 4
wood = 5
sapling = 6
bedrock = 7
water = 9
lava = 10
sand = 12
gravel = 13
leaves = 18
glass = 20
lapisLazuli = 21
sandstone = 24
bed = 26
cobweb = 30
wool = 35
yellowFlower = 37
blueFlower = 38
mushroom = 39
redMushroom = 40
gold = 41
iron = 42
Brick = 45
tnt = 46
bookshelf = 47
moss = 48
obsidian = 49
torch = 50
fire = 51
stairs = 53
chest = 54
diamond = 57
craft = 58
furnace = 61
door = 64
redstone = 73
snow = 78
ice = 79
snowBlock = 80
cactus = 81
clay = 82
sugarCane = 83
glowstone = 89
stoneBrick = 98
glass = 102
melon = 103
fenceGate = 107
fence = 85
glowingObsidian = 246

##wool colors
white = 0
orange = 1
magenta = 2
lightBlue = 3
yellow = 4
lime = 5
pink = 6
grey = 7
lightGrey = 8
cyan = 9
purple = 10
blue = 11
brown = 12
green = 13
red = 14
black = 15

## functions

def giantMeteor(x,y,z,r):
        xMin = x - r
        xMax = x + r
        yMin = y - r
        yMax = y + r
	
        for i in range(r):
                for j in range(r):
                        xi = x-i
                        yi = y-j
                        xf = x+i
                        yf = y+j
                        mc.setBlocks(x-i,y-j, z-(r*r-xi*xi-yi*yi), xf,yf, z+(r*r-xi*xi-yi*yi), 246)

def delMeteor(x,y,z,r):
        xMin = x - r
        xMax = x + r
        yMin = y - r
        yMax = y + r
	
        for i in range(r):
                for j in range(r):
                        xi = x-i
                        yi = y-j
                        xf = x+i
                        yf = y+j
                        mc.setBlocks(x-i,y-j, z-(r*r-xi*xi-yi*yi), xf,yf, z+(r*r-xi*xi-yi*yi), air)
				
def giantMeteor2016():
        t = 0
        X = 0
        Y = 130
        Z = 0
        y = 130
        while (y > 0):
                #x = X - 9.8*t*t
                y = Y - 9.8*t*t
                #z = Z - 9.8*t*t
                giantMeteor(X,y,Z,2)
                sleep(2)
                delMeteor(X,y,Z,2)
                t = t + 1

def warp(x,y,z):
    mc.player.setPos(x,y,z)

def tunnel(w,x,y,z, colors):
    mc.postToChat("Building tunnel")
    air = 0
    wool = 35
    ##hole downwww
    ##mc.setBlock(x,10,z, x,y-4,z, air)
    for i in colors:
        ##ceiling
        mc.setBlocks(x, y+w+2, z-w, x, y+w+2, z+w, wool, i)
        ##floor
        mc.setBlocks(x, y-1, z-w, x, y-1, z+w, wool, i)
        ##minus wall
        mc.setBlocks(x,  y-1, z-w-1, x, y+w+2, z-w-1, wool, i)
        ##plus wall
        mc.setBlocks(x, y-1, z+w+1, x, y+w+2, z+w+1, wool, i)
        ##air
        mc.setBlocks(x, y, z-w, x, y+w+1, z+w, air)
        x = x + 1
    mc.postToChat("Tunnel Built")


def hole(w,x,y,z, colors):
    mc.postToChat("Digging hole")
    air = 0
    wool = 35
    ##hole downwww
    ##mc.setBlock(x,10,z, x,y-4,z, air)
    for i in colors:
        ##ceiling
        mc.setBlocks(x+w+2, y, z-w, x, y, z+w, wool, i)
        ##floor
        mc.setBlocks(x-1, y, z-w, x-1, y, z+w, wool, i)
        ##minus wall
        mc.setBlocks(x-1,  y, z-w-1, x+w+2, y, z-w-1, wool, i)
        ##plus wall
        mc.setBlocks(x-1, y, z+w+1, x+w+2, y, z+w+1, wool, i)
        ##air
        mc.setBlocks(x, y, z-w, x+w+1, y, z+w, air)
        y = y - 1
    mc.postToChat("Dig dug")
	
## Let The World Be Destroyed
mc.postToChat("Let the World Be Destroyed")
#giantMeteor2016()
#sleep(3)

## sand & air
#mc.player.setPos(0,420,13)
mc.setBlocks(-156,-1,-153, 156,-1,156, stone)
mc.setBlocks(-156, 0,-156, 156,0,156, sand)
mc.setBlocks(-156, 1,-156, 156,156,156, air)


## burning Man
##feet
mc.setBlocks(-6,1,-3, -3,2,3, wood)
mc.setBlocks( 6,1,-3,   3,2,3, wood)
mc.setBlocks(-5,1,-2, -4,1,2, tnt, 1)
mc.setBlocks( 5,1,-2,   4,1,2, tnt, 1)
mc.postToChat("Let")

##legs
mc.setBlocks(-6,3,-3, -3,13,0, wood)
mc.setBlocks(-5,3,-2, -4,13,-1, tnt, 1)

mc.setBlocks(6,3,-3, 3,13,0, wood)
mc.setBlocks(5,3,-2, 4,13,-1, tnt, 1)


##body
mc.setBlocks(-6,14,-3, 6,33,0, wood)
mc.setBlocks(-5,15,-2, 5,32,-1, tnt, 1)

##arm
mc.setBlocks(-9,31,-3, -7,45,0, wood)
mc.setBlocks(-8,32,-2, -8,44,-1, tnt, 1)

mc.setBlocks(9,33,-3, 7,23,0, wood)
mc.setBlocks(8,32,-2, 8,25,-1, tnt, 1)
mc.setBlocks(9,26,-3, 7,23,7, wood)
mc.setBlocks(8,25,-2, 8,24,6, tnt, 1)
mc.postToChat("Let Life")

##torch
mc.setBlocks(-9,46,-3, -7,46,0, tnt, 1)
mc.setBlocks(-10,47,-3, -8,47,0, tnt, 1)
mc.setBlocks(-11,48,-3, -8,48,0, tnt, 1)

##book
mc.setBlocks(11,27,3, 5,29,8, tnt, 1)
mc.setBlocks(10,28,3, 5,28,8, wool)

##head
mc.setBlocks(-3,33,-3, 3,40,3, wood)
mc.setBlocks(-2,34,-2, 2,39,2, tnt, 1)
mc.postToChat("Let Life Live")

#Pi Hole of Death
##When you die, you see the digits of pi flash before your eyes
##When you die, you see numbers as colors
pi = [3, 1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3, 3,8,3,2,7,9,5,0,2,8, 8,4,1,9,7,1,6, 9, 3, 9, 9,3,7,5,1,0,5,8,2,0,9,7,4,9,4,4,5,9,2,3,0,7,8,1,6,4, 0,6,2,8,6,2,0,8,9,9, 8,6,2,8,0,3,4, 8, 2,5,3,4,2, 1,1,7,0, 6, 7,9,8,2,1,4,8,0,8,6,5,1,3,2,8,2,3,0,6, 6,4,7,0,9,3,8,4,4,6,0,9, 5,5,0,5, 8, 2,2, 3, 1,7, 2,5, 3,5,9,4,0,8,1,2,8,4,8,1,1,1,7,4,5,0,2,8,4,1,0,2,7,0,1,9,3,8, 5,2,1,1,0,5,5, 5, 9, 6,4,4,6,2,2,9,4,8,9,5,4,9,3,0,3,8,1,9,6,4,4,2,8,8,1,0,9,7,5,6,6,5,9,3,3,4,4,6,1,2,8,4,7,5,6, 4, 8,2,3,3, 7, 8, 6, 7, 8, 3, 1, 6, 5, 2, 7, 1, 2, 0, 1, 9, 0, 9, 1, 4, 5, 6, 4, 8, 5, 6, 6, 9, 2, 3, 4, 6, 0, 3, 4, 8, 6, 1, 0, 4, 5, 4, 3, 2, 6, 6, 4, 8, 2, 1, 3, 3, 9, 3, 6, 0, 7, 2, 6, 0, 2, 4, 9, 1, 4, 1, 2, 7, 3, 7, 2, 4, 5, 8, 7, 0, 0, 6]
mc.postToChat("This is Madness")
mc.setBlocks(18,1,13, 24,1,19, stone)
hole(1,20,1,16,pi)
mc.postToChat("This is Minecraft Burning Man!")

