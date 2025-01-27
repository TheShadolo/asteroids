import pygame
from constants import *
from player import Player
def main():
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()  
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000
        player.update(dt)
        while player.rotation >= 360.0:
            player.rotation -= 360
        while player.rotation <= -360.0:
            player.rotation += 360
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()