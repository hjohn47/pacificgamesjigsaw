import pygame
from pygame.locals import *
from sys import exit
from random import randint
import math
from pygame import mixer
import os


###############################################################
def inArea(gX, gY, pointX, pointY, pointX2, pointY2):
    if pointX < gX < pointX2 and pointY < gY < pointY2:
        return True
    else:
        return False


def inCircle(pointX, pointY, gX, gY, distance):
    xDist = pointX - gX
    xDist = math.fabs(xDist)
    yDist = pointY - gY
    yDist = math.fabs(yDist)
    xyDist = (xDist * xDist) + (yDist * yDist)
    if distance >= math.sqrt(xyDist):
        return True
    else:
        return False


############################################################

imagestring = ""
endstring = ""
secendstring = ""
scene = 0
keyonce = 1
text = ""
blink = 0
caps = 0
imageOn = 0
col = 0
row = 0
hit = -1
offsetX = 0
offsetY = 0
pix = 1

#clock = pygame.time.Clock()
#pygame.mixer.init(44100, 16, 2, 4096)
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pacific Games: Slide Puzzle')

icon = pygame.image.load("icon.png").convert_alpha()
pygame.display.set_icon(icon)

# pygame.scrap.init()

#font1 = pygame.font.Font("etobicoke.ttf", 16)

#bg = pygame.image.load("bg.png").convert()
#MAIN = pygame.image.load("MAIN.png").convert()

background = pygame.image.load("MAIN.png")

#gray = pygame.image.load("gray.png").convert()

#bas = pygame.image.load("bas.png").convert()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            running = False

#p = pygame.image.load("sp50.png").convert_alpha()

#look = pygame.image.load("look.png").convert()
#returnx = pygame.image.load("return.png").convert()

#WELLDONE = pygame.image.load("WELLDONE.png").convert()

#green = pygame.image.load("green.png").convert_alpha()

#snip = pygame.mixer.Sound("SNIP1.ogg")
#bambam = pygame.mixer.Sound("Relaxing.mp3")

b1 = pygame.image.load("baseimages/waterfall.png").convert()
b2 = pygame.image.load("baseimages/lakesunset.png").convert()
b3 = pygame.image.load("baseimages/kittensunlight.png").convert()
b4 = pygame.image.load("baseimages/puppy.png").convert()
b5 = pygame.image.load("baseimages/hammock.png").convert()
b6 = pygame.image.load("baseimages/bub.png").convert()
#b7 = pygame.image.load("baseimages/doa1.png").convert()
#b8 = pygame.image.load("baseimages/gun.png").convert()
#b9 = pygame.image.load("baseimages/rh.png").convert()
#b10 = pygame.image.load("baseimages/bl.png").convert()
#b11 = pygame.image.load("baseimages/elk.png").convert()
#b12 = pygame.image.load("baseimages/tor.png").convert()
#b13 = pygame.image.load("baseimages/bldr.png").convert()
#b14 = pygame.image.load("baseimages/val2.png").convert()
#b15 = pygame.image.load("baseimages/elv.png").convert()
#b16 = pygame.image.load("baseimages/cat.png").convert()
#b17 = pygame.image.load("baseimages/mars.png").convert()
#b18 = pygame.image.load("baseimages/rum.png").convert()
#b19 = pygame.image.load("baseimages/cab.png").convert()
#b20 = pygame.image.load("baseimages/three.png").convert()

d_list = []
e_list = []


class PP():
    def piece(self, img, col, row, x, y, s):
        self.img = img
        self.col = col
        self.row = row
        self.x = x
        self.y = y
        self.s = s


for i in range(13):
    for ii in range(10):
        b = PP()
        b.piece(pygame.image.load("bas.png").convert(), i, ii, 0, 0, 0)
        d_list.append(b)

#text = font1.render(imagestring, True, (0, 0, 0))
#text2 = font1.render("Load failed", True, (255, 0, 0))
#textF = font1.render("Open the folder 'yourimage'", True, (0, 0, 0))
#textE = font1.render("Drop the image in the folder.", True, (0, 0, 0))
#textP = font1.render("Enter the name of the file with the keyboard below.", True, (0, 0, 0))
#textL = font1.render("Click the Load button.", True, (0, 0, 0))
#textLB = font1.render("LOAD", True, (255, 255, 255))
#textME = font1.render("MAIN    EXIT", True, (255, 255, 255))