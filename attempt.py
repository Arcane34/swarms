import pygame
import random
from pygame.locals import *

pygame.init()

# Define the screen size
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Define the clock
clock = pygame.time.Clock()


# Define the colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0,0,0)

# Define the Particle class
class Particle:
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = 10
        self.speed_x = vx
        self.speed_y = vy
        self.age = 0
        self.sizeSpeed = 0.3

        #accurate glow
        #glowFalloffFactor = 60
        #self.glowColor = (color[0]//glowFalloffFactor,color[1]//glowFalloffFactor,color[2]//glowFalloffFactor)

        #efficient glow
        glowFalloffFactor = 10
        self.glowColor = (color[0]//glowFalloffFactor,color[1]//glowFalloffFactor,color[2]//glowFalloffFactor)
        
        self.glowSize = self.size * 2
        

    def draw(self, screen):

        #accurate glow
        """for i in range(0,self.glowSize,1):
            surf = pygame.Surface((800,600))
            surf.set_colorkey((0,0,0))
            pygame.draw.circle(surf, self.glowColor, (int(self.x), int(self.y)), i)
            screen.blit(surf, (0,0), special_flags=BLEND_RGB_ADD)"""

        #efficient easy glow
        surf = pygame.Surface((800,600))
        surf.set_colorkey((0,0,0))
        pygame.draw.circle(surf, self.glowColor, (int(self.x), int(self.y)), self.glowSize)
        screen.blit(surf, (0,0), special_flags=BLEND_RGB_ADD)
        
        
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.size -= self.sizeSpeed
        self.glowSize -= self.sizeSpeed * 2
        self.age += 1


        
# Create a list to store the particles
particles = []

# Set the start time
start_time = pygame.time.get_ticks()

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


    # Explode the particle into 5 particles after 3 seconds
    
    particle = Particle(screen_width // 2, screen_height // 2, ((random.randint(0,20)/10)-1)*5, ((random.randint(0,20)/10)-1)*5, YELLOW)
    particles.append(particle)

    # Update and draw the particles
    for particle in particles:
        particle.update()
        particle.draw(screen)
        if particle.size < 1 or not(-10 <particle.x < 810) or not(-10 <particle.y < 610) :
            particles.remove(particle)

    # Update the screen
    pygame.display.update()
