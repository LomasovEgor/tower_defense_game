class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self) -> tuple[int, int]:
        return self.x, self.y


class MovePoints:
    def __init__(self):
        self.points: list = []

    def append_point(self, x: int, y: int):
        self.points.append(Point(x, y))

    def delete_last(self):
        self.points.remove(-1)

    def delete_first(self):
        self.points.remove(0)
