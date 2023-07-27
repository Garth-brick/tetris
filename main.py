import pygame
import sys
from cell import Cell
from blocks import *
from game import Game
pygame.init()

# initialise the game object
game = Game()

# initialising the window
WINDOW_HEIGHT: int = (
    game.grid.num_rows * Cell.size + 
    (game.grid.num_rows - 1) * game.grid.PADDING
)
WINDOW_WIDTH = (
    game.grid.num_cols * Cell.size +
    (game.grid.num_cols - 1) * game.grid.PADDING
)
WINDOW: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BLACK_COLOR: tuple[int, int, int] = (0, 0, 0)
WINDOW_COLOR: tuple[int, int, int] = BLACK_COLOR
# setting the caption of the window
pygame.display.set_caption("Tetris")

# initialising the clock object
clock = pygame.time.Clock()

# setting FPS to 60 frames per second
FPS = 60


def draw():
    WINDOW.fill(WINDOW_COLOR)
    game.draw(WINDOW)
    pygame.display.update()


GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)

def main() -> None:
    
    running = True
    
    while running:
        clock.tick(FPS)
        draw()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if not game.game_over and event.type == GAME_UPDATE:
                game.move_down()
            if game.game_over and event.type == pygame.KEYDOWN:
                game.reset()
                game.game_over = False
                break
            if event.type == pygame.KEYDOWN:
                keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    game.move_left()
                if keys[pygame.K_RIGHT]:
                    game.move_right()
                if keys[pygame.K_DOWN]:
                    game.move_down()
                if keys[pygame.K_UP]:
                    game.rotate()
        
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()