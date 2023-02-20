import pygame
import random
from pygame.locals import *

pygame.init()

# Define the screen size
screen_width = 800
screen_height = 1080

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Define the clock
clock = pygame.time.Clock()


# Define the colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0,0,0)
GREEN = (0,255,0)


class Explode:
    def __init__(self, x, y, size, color, vel):
        self.x = x
        self.y = y
        self.color = color
        self.vel = vel
        self.size = size
        self.width = 8

    def update(self):
        self.size += self.vel
        self.width -= 0.2

    def draw(self, screen):
        self.update()
        if int(self.width) < 1:
            explodes.remove(self)
        else:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, int(self.width))
        



# Define the Particle class
class Particle:
    def __init__(self, x, y, vx, vy, size, color, lifeSpan):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.speed_x = vx
        self.speed_y = vy
        
        self.age = 0
        if lifeSpan == -1:
            self.sizeSpeed = 0.3
            self.ax = 0
            self.ay = 1
        else:
            self.sizeSpeed = 0
            self.ax = 0
            self.ay = 0
        self.lifeSpan = lifeSpan

        #accurate glow
        #glowFalloffFactor = 60
        #self.glowColor = (color[0]//glowFalloffFactor,color[1]//glowFalloffFactor,color[2]//glowFalloffFactor)
        #self.glowSize = self.size * 3

        #efficient glow
        glowFalloffFactor = 10
        self.glowColor = (color[0]//glowFalloffFactor,color[1]//glowFalloffFactor,color[2]//glowFalloffFactor)
        self.glowSize = self.size * 2
        
        

    def draw(self, screen):
        self.update()
        #accurate glow
##        for i in range(0,self.glowSize,1):
##            surf = pygame.Surface((800,600))
##            surf.set_colorkey((0,0,0))
##            pygame.draw.circle(surf, self.glowColor, (int(self.x), int(self.y)), i)
##            screen.blit(surf, (0,0), special_flags=BLEND_RGB_ADD)

        #efficient easy glow
        surf = pygame.Surface((screen_width,screen_height))
        surf.set_colorkey((0,0,0))
        pygame.draw.circle(surf, self.glowColor, (int(self.x), int(self.y)), self.glowSize)
        screen.blit(surf, (0,0), special_flags=BLEND_RGB_ADD)
        
        
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_x += self.ax
        self.speed_y += self.ay
        self.size -= self.sizeSpeed
        #self.glowSize = int(self.size * 3)
        self.glowSize = int(self.size * 2)
        self.age += 1






class ProgramFlow:
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = 10
        self.speed_x = vx
        self.speed_y = vy
        self.age = 0
        self.sizeSpeed = 0

        #accurate glow
        glowFalloffFactor = 20
        self.glowColor = (color[0]//glowFalloffFactor,color[1]//glowFalloffFactor,color[2]//glowFalloffFactor)

        #efficient glow
        #glowFalloffFactor = 10
        #self.glowColor = (color[0]//glowFalloffFactor,color[1]//glowFalloffFactor,color[2]//glowFalloffFactor)
        
        self.glowSize = self.size * 3
        

    def draw(self, screen):
        self.update()
        #accurate glow
        for i in range(self.size,self.glowSize,3):
            surf = pygame.Surface((800,600))
            surf.set_colorkey((0,0,0))
            pygame.draw.circle(surf, self.glowColor, (int(self.x), int(self.y)), i)
            screen.blit(surf, (0,0), special_flags=BLEND_RGB_ADD)

        #efficient easy glow
##        surf = pygame.Surface((screen_width,screen_height))
##        surf.set_colorkey((0,0,0))
##        pygame.draw.circle(surf, self.glowColor, (int(self.x), int(self.y)), self.glowSize)
##        screen.blit(surf, (0,0), special_flags=BLEND_RGB_ADD)
        
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
        #pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, 3)


        if self.size < 1  or not(-10 < self.y < 610) :
            programFlowParticles.remove(self)
        elif not(-10 < self.x < 750):
            explodes.append(Explode(self.x, self.y, self.size, self.color, 2))
            programFlowParticles.remove(self)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.size -= self.sizeSpeed
        self.glowSize = int(self.size * 3)
        self.age += 1


    def output(self,typeOfOut):
        particles.append(Particle(self.x, self.y, 0, -1,10, GREEN, 120))

def redrawWin():
    for particle in particles:
        particle.draw(screen)
        if particle.size < 1 or not(-10 <particle.x < 810) or not(-10 <particle.y < 610):
            particles.remove(particle)
        elif (particle.lifeSpan != -1 and particle.lifeSpan < particle.age):
            explodes.append(Explode(particle.x, particle.y, particle.size, particle.color, 2))
            
##            for i in range(9):
##                particles.append(Particle(particle.x, particle.y, (random.randint(0,20)/10 -1)*3, (random.randint(0,20)/10 -1)*3 - 5,5, GREEN, -1))
            
            particles.remove(particle)

            
    for particle in programFlowParticles:
        particle.draw(screen)
        

    for explode in explodes:
        explode.draw(screen)

    # Update the screen
    pygame.display.update()




        
# Create a list to store the particles
particles = []
programFlowParticles = []
explodes = []

#particle = Particle(50, screen_height // 2, 1, 0, WHITE)
#particles.append(particle)

programFlow = ProgramFlow(50, screen_height // 2, 1, 0, WHITE)
programFlowParticles.append(programFlow)


# Set the start time
start_time = pygame.time.get_ticks()
out = False
# Run the game loop
while True:
    # Handle events
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    # Define frames per second
    clock.tick(60)
    
    # Clear the screen
    screen.fill(BLACK)

    # Get the elapsed time
    elapsed_time = pygame.time.get_ticks() - start_time

    if programFlow.x == 400 and not(out):
        programFlow.output(5)
        out = True

    redrawWin()
