import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # initizalize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
    pygame.display.set_caption("boot.dev: Asteroids!")
    
    # main game loop
    game_running = True
    while game_running:
        for event in pygame.event.get()
            if event.type == pygame.QUIT:
                return
            
        black = pygame.Color((0,0,0))
        view = screen.fill(color=black)
        pygame.display.flip()
    
    
if __name__ == "__main__":
    main()