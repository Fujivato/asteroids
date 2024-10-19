import pygame
from constants import *
from circleshape import *
from player import *

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
    game_clock = pygame.time.Clock()
    delta_time = 0
 
    # initialise the player
    player_x_pos = SCREEN_WIDTH/2
    player_y_pos = SCREEN_HEIGHT/2
    player = Player(player_x_pos, player_y_pos)
    
    # run the game
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update the delta time:
        delta_time = game_clock.tick(60)/1000
        
        # update objects
        player.update(delta_time)
                
        # render objects
        black = pygame.Color((0,0,0))
        view = screen.fill(color=black)
        player.draw(screen)
        
        # flip the buffers
        pygame.display.flip()
    
if __name__ == "__main__":
    main()