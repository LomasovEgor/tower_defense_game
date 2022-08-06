from point import Point


class MoveQueue:
    def __init__(self):
        self.points: list[Point] = []

    def get_first(self) -> Point:
        return self.points[0]

    def append_point(self, x: int, y: int):
        self.points.append(Point(x, y))

    def delete_last(self):
        self.points.pop(-1)

    def delete_first(self):
        self.points.pop(0)
