import pygame
import time
import random

#creating window in which we are going to make game
width , height = 1000,800
win=pygame.display.set_mode((width,height))

#displaing game name at top
pygame.display.set_caption("Space Wars")

#to keep game on we need a loop we will make a loop
def main():
    run=True

    while run:
       #herar we are making a event which if we close the window game will exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break

    pygame.quit()


if __name__=="__main__":
    main()

