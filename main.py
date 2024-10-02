import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Player Object
    Player.containers = (updatable, drawable)  
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        # Updatables
        for obj in updatable:
            obj.update(dt)

        # Drawables
        for draw in drawable:
            draw.draw(screen)
         
        pygame.display.flip()  
        
 
        # Frame Rate
        dt = clock.tick(60) / 1000


        



if __name__ == "__main__":
    main()

    