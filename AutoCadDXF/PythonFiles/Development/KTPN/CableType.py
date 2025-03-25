import math


class CableType:
    def __init__(self,msp,name,x,y):
        self.msp=msp
        self.name=name
        self.x=x
        self.y=y
        self.count=int(self.name.strip()[0])
        self.pointsY=[self.y-i*1.34 for i in range(self.count)]
        self.first_part()
    def first_part(self):
        self.msp.add_line((self.x - 1.51, self.y + 0.42), (self.x - 1.36, self.y + 1.5), dxfattribs={'color': 3})
        if "с 0" in self.name:
            self.msp.add_circle(
                (self.x-1.59,self.y-0.27),
                0.5,
                dxfattribs={'color': 3}
            )
            hatch = self.msp.add_hatch(color=3)  # 2 — это желтый цвет
            hatch.set_solid_fill(color=3)
            points = self.get_circle_points((self.x-1.59,self.y-0.27), 0.5, num_points=36)  # 36 точек для аппроксимации
            hatch.paths.add_polyline_path(points)

        for y in self.pointsY:
                self.printLine(y)

    def printLine(self,y):
        self.msp.add_line((self.x-1.48,y+1), (self.x+1.48,y-1), dxfattribs={'color': 3})
    def get_circle_points(self, center, radius, num_points=36):
        """Генерирует точки на окружности."""
        points = []
        for i in range(num_points):
            angle = 2 * math.pi * i / num_points
            x = center[0] + radius * math.cos(angle)
            y = center[1] + radius * math.sin(angle)
            points.append((x, y))
        points.append(points[0])  # Замкнуть путь
        return points
