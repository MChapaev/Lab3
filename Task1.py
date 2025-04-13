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


class Pentagon(Shape):
    def __init__(self, identifier: str, points: list[tuple[float, float]]):
        if len(points) != 5:
            raise InvalidShapeError("Пятиугольник должен иметь 5 точек")
        super().__init__(identifier, points)


class Triangle(Shape):
    def __init__(self, identifier: str, points: list[tuple[float, float]]):
        if len(points) != 3:
            raise InvalidShapeError("Треугольник должен иметь 3 точки")
        super().__init__(identifier, points)


# Additional methods
def compare(t1: Shape, t2: Shape):
    try:
        a1 = t1.area()
        a2 = t2.area()
        print(f"Площадь {t1.id}: {a1}, Площадь {t2.id}: {a2}")
        if a1 > a2:
            return f"{t1.id} больше"
        elif a1 < a2:
            return f"{t2.id} больше"
        else:
            return "Фигуры одинаковы"
    except Exception as e:
        return f"Ошибка при сравнении: {e}"


def do_lines_intersect(p1, p2, q1, q2):
    def ccw(a, b, c):
        return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])
    return (ccw(p1, q1, q2) != ccw(p2, q1, q2)) and (ccw(p1, p2, q1) != ccw(p1, p2, q2))


def is_intersect(s1: Shape, s2: Shape):
    try:
        edges1 = list(zip(s1.points, s1.points[1:] + [s1.points[0]]))
        edges2 = list(zip(s2.points, s2.points[1:] + [s2.points[0]]))

        for e1_start, e1_end in edges1:
            for e2_start, e2_end in edges2:
                if do_lines_intersect(e1_start, e1_end, e2_start, e2_end):
                    return True
        return False
    except Exception as e:
        return f"Ошибка при проверке пересечения: {e}"


