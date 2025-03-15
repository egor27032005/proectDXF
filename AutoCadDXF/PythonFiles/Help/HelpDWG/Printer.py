import pyautocad
from pyautocad import APoint, aDouble


class PrinterNew():
    def __init__(self):
        acad = pyautocad.Autocad(create_if_not_exists=True)
        with open('lines.txt', 'r') as file:
            lines = [list(map(float, line.split())) for line in file]
        for line in lines:
            color=line[0]
            point1 = APoint(line[1], line[2])
            point2 = APoint(line[3], line[4])
            lin=acad.model.AddLine(point1, point2)
            lin.color=color

        with open('circle.txt', 'r') as file:
            circles = [list(map(float, circle.split())) for circle in file]
        for circle in circles:
            center = APoint(circle[1], circle[2])
            radius = circle[-1]
            cir=acad.model.AddCircle(center, radius)
            cir.color=circle[0]
        with open('arcs.txt', 'r') as file:
            arcs = [list(map(float, arc.split())) for arc in file]
        for arc in arcs:
            center = APoint(arc[0], arc[1])
            radius = arc[-1]
            start_angle = arc[3]
            end_angle = arc[4]
            acad.model.AddArc(center, radius, start_angle, end_angle)

        with open('polyline.txt', 'r') as file:
            numbers = [list(map(float, line.split())) for line in file]
        for number in numbers:
            p = aDouble(number[1:])
            pl = acad.model.AddLightWeightPolyline(p)
            pl.color=number[0]

        # with open('acDbSpline.txt', 'r') as file:
        #     numbers = [list(map(float, line.split())) for line in file]
        # for number in numbers:
        #     for i in range(0, len(number) - 3, 2):
        #         point1 = APoint(number[i], number[i + 1])
        #         point2 = APoint(number[i + 2], number[i + 3])
        #         acad.model.AddLine(point1, point2)

if __name__ == '__main__':
    x = PrinterNew()