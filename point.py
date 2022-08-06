class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_coords(self) -> tuple[int, int]:
        return self.x, self.y

    def set_coords(self, x: int, y: int):
        self.x = x
        self.y = y
