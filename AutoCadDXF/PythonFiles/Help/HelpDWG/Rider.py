import math

import pyautocad
from pyautocad import Autocad, APoint, aDouble
import itertools

class RiderNew:
    def __init__(self):
        self.acad = pyautocad.Autocad(create_if_not_exists=True)
        self.create_lines()

    def create_lines(self):
        self.lines = list(self.acad.iter_objects('Line'))
        self.newLines = [[line.color,*line.coordinates] for line in self.lines if
                    (str(line).find("POINTER(IAcadLWPolyline)")) == 1 ]
        self.newDottedLines = [[line.color,*line.startPoint[0:2], *line.endPoint[0:2]] for line in self.lines if
                          str(line).find("POINTER(IAcadLine)") == 1]
        self.circles = list(self.acad.iter_objects('Circle'))
        self.polylines = list(self.acad.iter_objects("Polyline"))
        self.arcs = list(self.acad.iter_objects("Arc"))
        self.acDbSplines = list(self.acad.iter_objects("AcDbSpline"))
        self.files()

    def files(self):
        with open('lines.txt', 'w') as file:
            for line in self.newLines:
                l = ''.join(str(x) + " " for x in line)
                file.write(l + '\n')
            for line in self.newDottedLines:
                l = ''.join(str(x) + " " for x in line)
                file.write(l + '\n')
        with open('circle.txt', 'w') as file:
            for circle in self.circles:
                line=[circle.color,*circle.center[0:2], circle.radius]
                l = ''.join(str(x) + " " for x in line)
                file.write(l + '\n')
        with open('arcs.txt', 'w') as file:
            for arc in self.arcs:
                l = ''.join(str(x) + " " for x in arc)
                file.write(l + '\n')
        with open('polyline.txt', 'w') as file:
            for polyline in self.polylines:
                l = ''.join(str(x) + " " for x in itertools.chain([polyline.color],polyline.coordinates))
                file.write(l + '\n')
        # with open('acDbSpline.txt', 'w') as file:
        #     for acDbSpline in self.acDbSplines:
        #         l = ''.join(str(x) + " " for x in acDbSpline)
        #         file.write(l + '\n')
if __name__ == '__main__':
    x = RiderNew()