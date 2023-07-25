import pygame
import random
import sys

class species:
    def __init__(self, speed, stamina, x, y, size):
        
        self.food = 100
        self.life = 100
        self.speed = speed
        self.stamina = stamina
        self.x = x
        self.y = y
        self.size = size
        pygame.draw.circle(screen, color='red', center=(x,y), radius=5)

    def move(self):
        self.x = self.x+self.speed
        pygame.draw.circle(screen, color='red', center=(self.x,self.y), radius=5)

def initEcosystem(numSpecies):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        screen.fill('grey')
        for species in numSpecies:
            animal = numSpecies[species]
            animal.move()
            #print(species)
        pygame.display.update()
        clock.tick(50)

HEIGHT = 1000
WIDTH = 1000

pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
screen.fill('grey')
pygame.display.set_caption('Simulated Ecosystem')
clock = pygame.time.Clock()

numspecies = {}
for i in range(0,100):
    xCord = random.randint(0,HEIGHT)
    yCord = random.randint(0,WIDTH)
    numspecies[i] = species(speed=2, stamina=5, x=xCord, y=yCord)

initEcosystem(numspecies)


