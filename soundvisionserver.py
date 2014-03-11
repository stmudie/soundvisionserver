import os
import pygame
import time
import random
import math

class pyscope :
    screen = None;
    
    def __init__(self):
        "Ininitializes a new pygame screen using the framebuffer"
        # Based on "Python GUI in Linux frame buffer"
        # http://www.karoltomala.com/blog/?p=679
        pygame.init()
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print "I'm running under X display = {0}".format(disp_no)
        
        # Check which frame buffer drivers are available
        # Start with fbcon since directfb hangs with composite output
        drivers = ['fbcon', 'directfb', 'svgalib']
        found = False
        for driver in drivers:
            # Make sure that SDL_VIDEODRIVER is set
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print 'Driver: {0} failed.'.format(driver)
                continue
            found = True
            break
    
        if not found:
            raise Exception('No suitable video driver found!')
        
        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print "Framebuffer size: %d x %d" % (size[0], size[1])
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        self.screen.fill((0, 0, 0))        
        # Initialise font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()

    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."

    def test(self):
        # Fill the screen with red (255, 0, 0)
        red = (255, 0, 0)
        self.screen.fill(red)
        # Update the display
        pygame.display.update()

# Create an instance of the PyScope class
scope = pyscope()

clock = pygame.time.Clock()
grey = (100, 100, 100)
font = pygame.font.Font(None, 600)
text_surface = font.render('Scan Finished',True, (155,200,255))
rect = text_surface.get_rect()


elapsed = 0
start = pygame.time.get_ticks()
#while elapsed <= 10:
#    clock.tick(30)
#    elapsed = (pygame.time.get_ticks()-start)/1000.
#    scope.screen.fill(grey)
#    display_surface = pygame.transform.rotate(pygame.transform.smoothscale(text_surface,(int(150*elapsed),int(50*elapsed))),500*elapsed)
#    rect = display_surface.get_rect()
#    rect.center = (500,500)
#    scope.screen.blit(display_surface,rect.topleft)
#    scope.screen.blit(font.render("{0:.2f}".format(elapsed),True,(255,255,255)),(1000,100))
#    scope.screen.blit(font.render("{0:.2f}".format(clock.get_fps()),True,(255,255,255)),(2000,100))
#    pygame.display.update()
frame_no = 0
while elapsed <= 10:
    clock.tick(30)
    elapsed = (pygame.time.get_ticks()-start)/1000.
    r = 50*(math.cos(frame_no/5.)+1)
    g = 50*(math.cos(frame_no/20.)+1)
    b = 50*(math.cos(frame_no/30.)+1)
    scope.screen.fill((r,g,b))
    if frame_no%20 < 15:
        display_surface = pygame.transform.smoothscale(text_surface,(int(50*(rect.width/rect.height)*elapsed),int(50*elapsed)))
        scope.screen.blit(display_surface,(500,500))
    frame_no = frame_no + 1
    pygame.display.update()
    
