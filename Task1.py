# Classes for exception handling
class ShapeException(Exception):
    pass


class InvalidShapeError(ShapeException):
    pass


# Classes for shapes
class Shape:
    def __init__(self, identifier: str, points: list[tuple[float, float]]):
        self.id = identifier
        self.points = points

    def area(self):
        x = [p[0] for p in self.points]
        y = [p[1] for p in self.points]
        return abs(sum(x[i] * y[(i+1)%len(self.points)] - x[(i+1)%len(self.points)] * y[i]
                       for i in range(len(self.points))) / 2)
