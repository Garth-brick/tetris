from block import Block
from position import Position


class Lblock(Block):
    color_id: int = 1
    
    def __init__(self) -> None:
        super().__init__(Lblock.color_id)
        self.cells = {
            0: (Position(0,2), Position(1,0), Position(1,1), Position(1,2)),
            1: (Position(0,1), Position(1,1), Position(2,1), Position(2,2)),
            2: (Position(1,0), Position(1,1), Position(1,2), Position(2,0)),
            3: (Position(0,0), Position(0,1), Position(1,1), Position(2,1))
        }
        self.move(0,3)
        

class Jblock(Block):
    color_id = 2
    
    def __init__(self) -> None:
        super().__init__(Jblock.color_id)
        self.cells = {
            0: (Position(0,0), Position(1,0), Position(1,1), Position(1,2)),
            1: (Position(0,1), Position(0,2), Position(1,1), Position(2,1)),
            2: (Position(1,0), Position(1,1), Position(1,2), Position(2,2)),
            3: (Position(0,1), Position(1,1), Position(2,0), Position(2,1))
        }
        self.move(0,3)


class Iblock(Block):
    color_id = 3
    
    def __init__(self) -> None:
        super().__init__(Iblock.color_id)
        self.cells = {
            0: (Position(1,0), Position(1,1), Position(1,2), Position(1,3)),
            1: (Position(0,2), Position(1,2), Position(2,2), Position(3,2)),
            2: (Position(2,0), Position(2,1), Position(2,2), Position(2,3)),
            3: (Position(0,1), Position(1,1), Position(2,1), Position(3,1))
        }
        self.move(-1,3)


class Oblock(Block):
    color_id = 4
    
    def __init__(self) -> None:
        super().__init__(Oblock.color_id)
        self.cells = {
            0: (Position(0,0), Position(0,1), Position(1,0), Position(1,1)),
            1: (Position(0,0), Position(0,1), Position(1,0), Position(1,1)),
            2: (Position(0,0), Position(0,1), Position(1,0), Position(1,1)),
            3: (Position(0,0), Position(0,1), Position(1,0), Position(1,1))
        }
        self.move(0,4)


class Sblock(Block):
    color_id = 5
    
    def __init__(self) -> None:
        super().__init__(Sblock.color_id)
        self.cells = {
            0: (Position(0,1), Position(0,2), Position(1,0), Position(1,1)),
            1: (Position(0,1), Position(1,1), Position(1,2), Position(2,2)),
            2: (Position(1,1), Position(1,2), Position(2,0), Position(2,1)),
            3: (Position(0,0), Position(1,0), Position(1,1), Position(2,1))
        }
        self.move(0,3)
        
class Tblock(Block):
    color_id = 6
    
    def __init__(self) -> None:
        super().__init__(Tblock.color_id)
        self.cells = {
            0: (Position(0,1), Position(1,0), Position(1,1), Position(1,2)),
            1: (Position(0,1), Position(1,1), Position(1,2), Position(2,1)),
            2: (Position(1,0), Position(1,1), Position(1,2), Position(2,1)),
            3: (Position(0,1), Position(1,0), Position(1,1), Position(2,1))
        }
        self.move(0,3)
    
        
class Zblock(Block):
    color_id = 7
    
    def __init__(self) -> None:
        super().__init__(Zblock.color_id)
        self.cells = {
            0: (Position(0,0), Position(0,1), Position(1,1), Position(1,2)),
            1: (Position(0,2), Position(1,1), Position(1,2), Position(2,1)),
            2: (Position(1,0), Position(1,1), Position(2,1), Position(2,2)),
            3: (Position(0,1), Position(1,0), Position(1,1), Position(2,0))
        }
        self.move(0,3)