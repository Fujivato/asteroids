import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def init_player():
    player_x_pos = SCREEN_WIDTH/2
    player_y_pos = SCREEN_HEIGHT/2
    return Player(player_x_pos, player_y_pos) 

def init_asteroid_field():
    return AsteroidField()

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = init_player() # initialise the player
    asteroid_field = init_asteroid_field() # initialise the asteroid field
    
    # initizalize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
    pygame.display.set_caption("boot.dev: Asteroids!")
        
    # main game loop
    game_running = True
    game_clock = pygame.time.Clock()
    delta_time = 0
    
    # run the game
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update the delta time:
        delta_time = game_clock.tick(60)/1000
        
        # update assets in "updatable" container
        for updatable_asset in updatable:
            updatable_asset.update(delta_time)
                
        # check for collisions:
        for asteroid in asteroids:
            for bullet in bullets:
                if asteroid.is_colliding_with(bullet):
                    asteroid.split()
                    bullet.kill()
                pass
            
            if asteroid.is_colliding_with(player):
                raise SystemExit("Game over!")
        
        # refresh screen
        black = pygame.Color((0,0,0))
        view = screen.fill(color=black)
        
        # render assets in the "drawable" container
        for drawable_asset in drawable:
            drawable_asset.draw(screen)
        
        # flip the buffers
        pygame.display.flip()
    
if __name__ == "__main__":
    main()