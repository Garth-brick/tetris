from abc import ABC, abstractmethod
from cell import Cell
from position import Position
from grid import Grid
import pygame

class Block(ABC):
    
    def __init__(self, color_id: int) -> None:
        self.color_id: int = color_id
        self.cells: dict[int, tuple[Position, ...]] = {}
        self._rotational_state: int = 0
        self.row_offset = 0
        self.col_offset = 0
        self.colors: list[tuple[int, int, int]] = Cell.get_cell_colors()
        
    @property
    def rotational_state(self) -> int:
        return self._rotational_state
    
    @rotational_state.setter
    def rotational_state(self, val) -> None:
        assert val in range(4), "invalid rotational state"
        self._rotational_state = val
        
    # updates the offsets of all the rows and columns
    def move(self, rows, cols):
        self.row_offset += rows
        self.col_offset += cols

    # returns the positions of each cell with the offset applied
    def get_cell_positions(self) -> tuple[Position, ...]:
        tiles = self.cells[self._rotational_state]
        moved_tiles: list[Position] = []
        for position in tiles:
            position = Position(
                position.row + self.row_offset,
                position.col + self.col_offset
            )
            moved_tiles.append(position)
        return tuple(moved_tiles)
    
    def draw(self, screen):
        
        # all the occupied tiles in this rotational state
        tiles = self.get_cell_positions()
        
        # drawing all the tiles
        for tile in tiles:
            tile_rect: pygame.Rect = pygame.Rect(
                tile.col * Cell.size + tile.col,
                tile.row * Cell.size + tile.row,
                Cell.size,
                Cell.size
            )
            tile_color = self.colors[self.color_id]
            pygame.draw.rect(
                screen,
                tile_color,
                tile_rect
            )
    
    def rotate(self) -> None:
        if self.rotational_state + 1 >= len(self.cells):
            self.rotational_state = 0
        else:
            self.rotational_state += 1