import pygame
from constants import *
from player import Player
def main():
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()  
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000
        for thing in updatables:
            thing.update(dt)
        while player.rotation >= 360.0:
            player.rotation -= 360
        while player.rotation <= -360.0:
            player.rotation += 360
        for thing in drawables:    
            thing.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()