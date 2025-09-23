import pygame
from pixel import *

scale = 6
spacing = 20 # spacing betweeen spirals, higher means less visualy dense 
added = 1 #?? idk what this is supposed to do 
spike = [m.pi/2,100] # make it more spikey with more spike [frequency, size]
hue = None # to implement at some point

# generate all the pixels
pixels = [Pixel(x*scale,y*scale) for x in range(-100,100) for y in range(-100,100)]


def create(pixels,spacing,spike):
    # my actual code for creating the swirls 
    scale = 6

    circles = 10 
    #impotrant for spirals 
    a_eff = spacing*2/m.pi -(spacing/20)*m.pi
    
    # calculate the colour/ brightness of the pixels 
    for x in pixels:
        # make circles iteratively
        val1 = 0
        val2 = 0
        val3 = 0 
        #for y in range(0,circles): removed to bring down the time to compute
            # this calculation for distance is what effects the spirals 
        # for making spiral 
        xr = x.distance+x.angle*a_eff 
        # add spiking effect 
        # what we want to do it goes up and it goes down 
        xr += abs(x.angle%spike[0]-spike[0]/2)*spike[1]
        y = xr//(spacing*scale/2) +1 
        if y > circles:
            y = circles
            
        val1 += std_dev(xr,(y*spacing*scale/2),3)*1000
        val2 += std_dev(xr,(y*spacing*scale/2),15)*1000
        val3 += std_dev(xr,(y*spacing*scale/2),20)*1000
        
        if val1 >255: # when implementing with openGL we may want to use a floor divide as branching might not be an option 
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
                spike[1] -= 10
            if keys[pygame.K_s]:
                spike[1] += 10
            if keys[pygame.K_z]:
                spike[0] -= m.pi/32
            if keys[pygame.K_x]:
                spike[0] +=m.pi/32
    
    #clear the screen
    screen.fill(WHITE)
    create(pixels,spacing,spike)
    # draw to the screen
    # YOUR CODE HERE
    x = (screen_size[0]/2) - (surface_size[0]/2)
    y = (screen_size[1]/2) - (surface_size[1]/2)
    #screen.blit(test_surface, (x, y))
    
    for x in pixels:
        pygame.draw.rect(screen,x.colour,(x.x+100*scale/2,x.y+100*scale/2,scale,scale))
    
    # show vals for spacing and adder
    myfont = pygame.font.SysFont("monospace", 20)
    spacing_t = myfont.render("spacing: "+str(spacing),1,RED)
    added_t = myfont.render("added: "+str(added),1,RED)
    spike0_t = myfont.render("spike Hz: "+str(spike[0]),1,RED)
    spike1_t = myfont.render("spike Ht: "+str(spike[1]),1,RED)
    
    screen.blit(spacing_t,(10,10))
    screen.blit(added_t,(10,30))
    screen.blit(spike0_t,(10,50))
    screen.blit(spike1_t,(10,70))
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)

pygame.quit()