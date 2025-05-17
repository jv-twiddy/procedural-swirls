import pygame
from pixel import *

# my actual code for creating the swirls 
radius = 200

# generate all the pixels
pixels = [Pixel(x,y) for x in range(-100,100) for y in range(-100,100)]

# calculate the colour/ brightness of the pixels 
for x in pixels:
    val = std_dev(x.distance,50,2)*255
    x.colour = (val,val,val)

print(pixels) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 
# initialize pygame
pygame.init()
screen_size = (600, 600)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")
 
# clock is used to set a max fps
clock = pygame.time.Clock()
 
# create a demo surface, and draw a red line diagonally across it
surface_size = (25, 45)
test_surface = pygame.Surface(surface_size)
test_surface.fill(WHITE)
pygame.draw.aaline(test_surface, RED, (0, surface_size[1]), (surface_size[0], 0))
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #clear the screen
    screen.fill(WHITE)
     
    # draw to the screen
    # YOUR CODE HERE
    x = (screen_size[0]/2) - (surface_size[0]/2)
    y = (screen_size[1]/2) - (surface_size[1]/2)
    #screen.blit(test_surface, (x, y))
    
    for x in pixels:
        pygame.draw.rect(screen,x.colour,(x.x+100,x.y+100,1,1))
    
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()