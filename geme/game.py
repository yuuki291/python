import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((400,300))
    pygame.display.set_caption("Test")


    while(1):
       screen.fill((0,0,0))
       pygame.display.update()

       for event in pygame.event.get():
           if event.type == quit:
               pygame.quit()
               sys.exit()


if __name__ == "__main__":
    main()