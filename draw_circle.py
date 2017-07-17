import sys
import pygame
import random
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255,255,255))

        for cnt in range(10):
            rad = 100
            x = random.randint(1, 400)
            y = random.randint(1, 300)
            bold = random.randint(1, rad)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            pygame.draw.circle(SURFACE, (r, g, b), (x, y), rad, bold)

            pygame.display.update()
            FPSCLOCK.tick(10)
'''
        #red
        pygame.draw.circle(SURFACE, (255, 0, 0), (50, 50), 20)
        #width
        pygame.draw.circle(SURFACE, (255, 0, 0), (150, 50), 20, 10)

        #green
        pygame.draw.circle(SURFACE, (0, 255, 0), (50, 150), 10)
        pygame.draw.circle(SURFACE, (0, 255, 0), (150, 150), 20)
        pygame.draw.circle(SURFACE, (0, 255, 0), (250, 150), 30)

        #blue
        pygame.draw.circle(SURFACE, (0, 0, 255), (50, 250), 20, 1)

        pygame.display.update()
        FPSCLOCK.tick(3)
'''
if __name__ == '__main__':
    main()


