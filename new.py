import pygame
import random
import math
from pygame import mixer
import os

#create button for directions text file
#create button to upload image
#create button on bottom to show different puzzles for user to solve

pygame.init()

screen = pygame.display.set_mode((850,880))
pygame.display.set_caption('Pacific Games: Slide Puzzle')

icon = pygame.image.load("icon.png").convert_alpha()
pygame.display.set_icon(icon)

background = pygame.image.load("MAIN.jpg").convert()

#def menu(Puzzle, start):

#game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    #pygame.draw.rect()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #(x,y) = pygame.mouse.get_pos()
    #if x >= 100 and y <=700 and event.type == pygame.MOUSEBUTTONDOWN:
        #print("Clicked")
    pygame.display.update()

#use os and let user input path for image they want to upload



