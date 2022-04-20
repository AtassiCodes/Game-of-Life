import pygame
import time
import random
import numpy as np
import os
import grid

os.environ["SDL_VIDEO_CENTERED"] = '1'

# resolution
width, height = 1200, 680
size = (width, height)
setsize = width ^ height

def fadein():
    fadein = pygame.Surface((1280, 720))
    fadein.fill((0, 0, 0))
    for alpha in range(0, 300):
        fadein.set_alpha(alpha)
        screen.blit(fadein, (0, 0))
        pygame.display.update()
        pygame.time.delay(2)

loading = pygame.image.load('data/LoadingScreen.png')

def loadingS():
    resized_background = pygame.transform.scale(loading, (width, height))
    screen.blit(resized_background, [0, 0])
    pygame.display.update()



pygame.init()
pygame.display.set_caption("Conway's Game Of Life")
screen = pygame.display.set_mode((size), pygame.RESIZABLE)
clock = pygame.time.Clock()
fps = 300

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0, 14, 71)
white = (255, 255, 255)

scaler = 15
offset = 1

Grid = grid.Grid(width, height, scaler, offset)
# Grid.random2d_array()

pause = False
paused = False
run = True

crashed = False
run = True
while run:
    while not paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        fadein()
        loadingS()
        pygame.display.update()
        pygame.time.wait(5000)
        fadein()
        paused = True

    paused = False
    while not paused:
        clock.tick(fps)
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                paused = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    paused = True
                if event.key == pygame.K_SPACE:
                    pause = not pause

        Grid.Conway(off_color=black, on_color=white, surface=screen, pause=pause)

        if pygame.mouse.get_pressed()[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            Grid.HandleMouse(mouseX, mouseY)

        pygame.display.update()

    pygame.quit()