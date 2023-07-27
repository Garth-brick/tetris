from grid import Grid
from blocks import *
import pygame
import random
import copy


class Game:
    BLOCKS = [
            Lblock(), 
            Jblock(), 
            Iblock(), 
            Oblock(), 
            Sblock(), 
            Tblock(), 
            Zblock()
        ]
    
    def __init__(self):
        self.grid: Grid = Grid()
        self.blocks: list[Block] = copy.deepcopy(Game.BLOCKS)
        self.current_block: Block = self.get_random_block()
        self.next_block: Block = self.get_random_block()
        self.game_over = False
        
    def get_random_block(self) -> Block:
        # original game rules
        # we need to cycle through all the blocks in a random order before repeating 
        if not self.blocks:
            self.blocks = copy.deepcopy(Game.BLOCKS)
        block: Block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
        
    def draw(self, screen: pygame.Surface):
        self.grid.draw(screen)
        self.current_block.draw(screen)
        
    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_is_inside() or not self.block_fits():
            # if the block is not inside after the move then undo the move
            self.current_block.move(0, 1)
        
    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_is_inside() or not self.block_fits():
            # if the block is not inside after the move then undo the move
            self.current_block.move(0, -1)
        
    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_is_inside() or not self.block_fits():
            # if the block is not inside after the move then undo the move
            self.current_block.move(-1, 0)
            self.lock_block()
            
    def lock_block(self):
        # we now need to update the values of the frid each time the block touches the bottom
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            self.grid.grid[tile.row][tile.col] = self.current_block.color_id
        self.current_block = self.next_block
        if not self.block_fits():
            self.game_over = True
        self.next_block = self.get_random_block()
        self.grid.clear_full_rows()
        
    def block_fits(self):
        # checking for collisions with other blocks as well
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty_cell(tile.row, tile.col):
                return False
        return True
                    
    def rotate(self):
        self.current_block.rotate()
        # if the block is not inside after the move then move it inside
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            row_offset, col_offset = self.grid.move_inside(tile.row, tile.col)
            self.current_block.move(row_offset, col_offset)
        
    def block_is_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.col):
                return False
        return True
    
    def reset(self):
        self.grid.reset()
        self.blocks = copy.deepcopy(Game.BLOCKS)
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()