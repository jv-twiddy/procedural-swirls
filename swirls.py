import pygame
from pixel import *

scale = 6
spacing = 10
added = 1

# generate all the pixels
pixels = [Pixel(x*scale,y*scale) for x in range(-100,100) for y in range(-100,100)]


def create(pixels,spacing):
    # my actual code for creating the swirls 
    scale = 6

    circles = 10 
    a_eff = spacing*2/m.pi -(spacing/20)*m.pi
    # calculate the colour/ brightness of the pixels 
    for x in pixels:
        # make circles iteratively
        val1 = 0
        val2 = 0
        val3 = 0 
        for y in range(0,circles):
            # this calculation for distance is what effects the spirals 
            xr = x.distance+x.angle*a_eff
            val1 += std_dev(xr,(y*spacing*scale/2),3)*1000
            val2 += std_dev(xr,(y*spacing*scale/2),15)*1000
            val3 += std_dev(xr,(y*spacing*scale/2),20)*1000
        
        if val1 >255:
            val1 = 255
        if val2 > 255:
            val2 = 255
        if val3 > 255:
            val3 = 255
        x.colour = (val1,val2,val3)

#print(pixels) 
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
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                spacing -=1
            if keys[pygame.K_w]:
                spacing +=1
            if keys[pygame.K_a]:
                added -=0.1
            if keys[pygame.K_s]:
                added += 0.1
     
    #clear the screen
    screen.fill(WHITE)
    create(pixels,spacing)
    # draw to the screen
    # YOUR CODE HERE
    x = (screen_size[0]/2) - (surface_size[0]/2)
    y = (screen_size[1]/2) - (surface_size[1]/2)
    #screen.blit(test_surface, (x, y))
    
    for x in pixels:
        pygame.draw.rect(screen,x.colour,(x.x+100*scale/2,x.y+100*scale/2,scale,scale))
    
    # show vals for spacing and adder
    myfont = pygame.font.SysFont("monospace", 20)
    spacing_t = myfont.render(str(spacing),1,BLACK)
    added_t = myfont.render(str(added),1,BLACK)
    screen.blit(spacing_t,(10,10))
    screen.blit(added_t,(10,30))
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)

pygame.quit()