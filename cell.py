class Cell:
    BLACK: tuple[int, int, int] =  (  0,   0,   0)
    WHITE: tuple[int, int, int] =  (255, 255, 255)
    GRAY: tuple[int, int, int] =   ( 32,  32,  32)
    RED: tuple[int, int, int] =    (227,  70,  59)
    ORANGE: tuple[int, int, int] = (227, 146,  59)
    YELLOW: tuple[int, int, int] = (242, 236,  51)
    GREEN: tuple[int, int, int] =  (155, 224,  70)
    CYAN: tuple[int, int, int] =   ( 59, 227, 193)
    BLUE: tuple[int, int, int] =   ( 59, 179, 227)
    PURPLE: tuple[int, int, int] = (157,  59, 227)
    PINK: tuple[int, int, int] =   (255, 135, 233)
    size: int = 30
    
    @classmethod
    def get_cell_colors(cls):
        return [
            cls.GRAY,
            cls.GREEN,
            cls.RED,
            cls.ORANGE,
            cls.YELLOW,
            cls.PURPLE,
            cls.CYAN,
            cls.BLUE
        ]