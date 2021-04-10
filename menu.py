import pygame
import random
import math
from pygame import mixer
import os
import tmain
import sys
import subprocess
import platform
from pygame.locals import *

#create button for directions text file
#create button to upload image
#create button on bottom to show different puzzles for user to solve
#check if clicked buttons
#use arrow keys to see puzzles already uploaded

pygame.init()

size = (850,880)
#screen = pygame.display.set_mode((850,880))
window = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption('Pacific Games: Slide Puzzle')

icon = pygame.image.load("pacificicon.png").convert_alpha()
pygame.display.set_icon(icon)

background = pygame.image.load("MAIN.jpg").convert()

yellow = (255,252,187)
white = (255,255,255)
black = (0,0,0)

###########################################################

screenRefresh = True

textboxGroup = pygame.sprite.OrderedUpdates()

#def menu(Puzzle, start):

def text_objects (text, font):
    textSurface = font.render(text,True, black)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):   #ic inactive color, ac active color
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(mouse)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(background, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "instructionsfile":
                #open in wordpad for windows and textedit for mac
                if platform.system() == 'Darwin':  # macOS
                    subprocess.call(('open', "instructionstest.pdf"))    #could also use text file
                elif platform.system() == 'Windows':  # Windows
                    os.startfile("instructionstest.pdf")
                else:  # linux variants
                    subprocess.call(('xdg-open', "instructionstest.pdf"))

    else:
        pygame.draw.rect(background, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))  # to center image
    background.blit(textSurf, textRect)

def puzzlestext(msg, x, y, w, h, c):   #button color (not real button just text)
    mouse = pygame.mouse.get_pos()
    # print(mouse)
    pygame.draw.rect(background, c, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))  # to center image
    background.blit(textSurf, textRect)
#def instructionsbox(x, y, w, h, c):
    #pygame.draw.rect(background, c, (x, y, w, h))

#def addText(text, x, y, w, h):
    #smallText = pygame.font.Font("freesansbold.ttf", 14)
    #textSurf, textRect = text_objects(text, smallText)
    #textRect.center = ((x + (w / 2)), (y + (h / 2)))  # to center words on rect
    #background.blit(textSurf, textRect)


def gameloop():
    #game loop
    running = True
    while running:
        window.fill((0, 0, 0))
        window.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        button("Upload Image", 50, 300, 200, 100, yellow, white) #"upload")
        button("Instructions", 50, 150, 200, 100, yellow, white, "instructionsfile")
        puzzlestext("Puzzles", 365, 780, 200, 60, yellow)
        button("Back", 225, 780, 100, 60, yellow, white)
        button("Next", 600, 780, 100, 60, yellow, white)


        pygame.display.update()

gameloop()


#use os and let user input path for image they want to upload



