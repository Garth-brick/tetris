from cell import Cell
import pygame

from position import Position


# this will store the values of all the blocks which have been set down
class Grid:
    NUM_ROWS_DEFAULT = 20
    NUM_COLS_DEFAULT = 10
    PADDING = 1
    
    
    def __init__(self, num_rows=NUM_ROWS_DEFAULT, num_cols=NUM_COLS_DEFAULT):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = Cell.size
        self.grid = [[0] * self.num_cols for _ in range(self.num_rows)]
        self.colors = Cell.get_cell_colors()
        
        
    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                
                # the color for each cell
                cell_value = self.grid[row][col]
                cell_color = self.colors[cell_value]
                
                # initialising a pygame Rect object for each cell
                cell_rect = pygame.Rect(
                    col * Cell.size + col * Grid.PADDING,
                    row * Cell.size + row * Grid.PADDING,
                    Cell.size,
                    Cell.size
                )
                
                # drawing the cell
                pygame.draw.rect(screen, cell_color, cell_rect)
                
                
    def __repr__(self) -> str:
        result = []
        for row in self.grid:
            row = map(str, row)
            result.append(" ".join(row))
        return "\n".join(result)
    
    
    def is_inside(self, row: int, col: int) -> bool:
        if row in range(self.num_rows) and col in range(self.num_cols):
            return True
        return False
    
    def is_empty_cell(self, row: int, col: int) -> bool:
        if not self.grid[row][col]:
            return True
        return False
    
    def move_inside(self, row, col) -> tuple[int, int]:
        row_offset = 0
        col_offset = 0
        if row < 0:
            row_offset = 1
        if row >= self.num_rows:
            row_offset = -1
        if col < 0:
            col_offset = 1
        if col >= self.num_cols:
            col_offset = -1
        return (row_offset, col_offset)
    
    def row_is_full(self, row) -> bool:
        for col in range(self.num_cols):
            if not self.grid[row][col]:
                return False
        return True
    
    def clear_row(self, row) -> None:
        for col in range(self.num_cols):
            self.grid[row][col] = 0
            
    def move_row_down(self, row, offset) -> None:
        assert row + offset > 0, "cannot move row down any further"
        if not offset:
            return
        for col in range(self.num_cols):
            self.grid[row + offset][col] = self.grid[row][col]
            self.grid[row][col] = 0
            
    def clear_full_rows(self) -> int:
        completed_rows = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.row_is_full(row):
                completed_rows += 1
                self.clear_row(row)
            else:
                self.move_row_down(row, completed_rows)
        return completed_rows
    
    def reset(self) -> None:
        self.grid = [[0] * self.num_cols for _ in range(self.num_rows)]