import os

from PythonFiles.Development.FlowChart.Block.CreateBlocks import CreateBlocks


class WaterIntakeWell:
    def __init__(self,doc,msp,startX,startY):
        self.doc=doc
        self.msp=msp
        self.startX=startX
        self.startY=startY
        self.objects={23: [(0.0, 0.7904047919226803, (49.624657596539976, -4.721847875341942, 0.0))],
                      51: [(0.0, 1.0, (22.489806841214886, 53.282904194973526, 0.0)), (0.0, 1.9586146809120466, (74.10686019412321, 31.799188667357654, 0.0))],
                      35: [(0.0, 0.38326196759046366, (16.3529563244374, 6.003450838063145, 0.0))],
                      33: [(270.02533149428854, 1.0221368877337618, (18.54021598867257, 23.830791183086227, 0.0)), (270.02533149428854, 0.968908848376488, (48.862379326536576, 42.54580223838492, 0.0)), (270.02533149428854, 0.968908848376488, (48.85064189638852, 57.240836145242056, 0.0))],
                      25: [(89.76480560511978, 0.8694635417016136, (21.473929596779758, 26.100123691455835, 0.0))],
                      34: [(0.0, 1.0, (40.905891176103616, 29.880602506757715, 0.0)), (0.0, 0.9673334831675923, (53.860821674062095, 30.150145465088183, 0.0)), (0.0, 1.0333189085823937, (40.59066278502789, 46.008753717453004, 0.0))],
                      }
        self.files()
        self.zeroPoint()
        self.transferringCoordinates()
        self.printer()
        self.create()
    def create(self):
        for key, value in self.objects.items():
            for lis in value:
                c = CreateBlocks(self.doc, self.msp, lis[2][0] + self.distanceX, lis[2][1] + self.distanceY, key,
                                 lis[0], lis[1])


    def files(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path1 = os.path.join(current_dir, "../../../AbTxtFiles/FlowChart/WaterIntakeWellFiles/lines.txt")
        file_path2 = os.path.join(current_dir, "../../../AbTxtFiles/FlowChart/WaterIntakeWellFiles/polyline.txt")
        file_path3 = os.path.join(current_dir, "../../../AbTxtFiles/FlowChart/WaterIntakeWellFiles/circle.txt")
        with open(file_path1) as file:
            self.lines = [list(map(float, line.split())) for line in file]
        with open(file_path2) as file:
            self.polylines = [list(map(float, line.split())) for line in file]
        with open(file_path3) as file:
            self.circle = [list(map(float, line.split())) for line in file]

    def zeroPoint(self):
        # Нахождение точки для смещения
        max_list = min(self.lines, key=lambda x: x[3])
        self.x, self.y = max_list[1], max_list[2]
        self.distanceX = self.startX - self.x
        self.distanceY = self.startY - self.y

    def transferringCoordinates(self):
        # Преобразование координат
        self.linesT = [self.transform(line) for line in self.lines]
        self.polylinesT = [self.transform(line) for line in self.polylines]
        self.circleT = [[cir[0], cir[1] + self.distanceX, cir[2] + self.distanceY, cir[3]] for cir in self.circle]

    def transform(self, sublist):
        # Преобразование координат для линий и полилиний
        for i in range(len(sublist)):
            if i == 0:
                continue  # Нулевой элемент не изменяем
            elif i % 2 == 0:
                sublist[i] += self.distanceY  # Чётные позиции
            else:
                sublist[i] += self.distanceX  # Нечётные позиции
        return sublist

    def printer(self):
        # Создание объектов в DXF-документе

        # Добавление линий
        for line in self.linesT:
            color = int(line[0])
            start_point = (line[1], line[2])
            end_point = (line[3], line[4])
            self.msp.add_line(start_point, end_point, dxfattribs={'color': color})

        for circle in self.circleT:
            color = int(circle[0])
            center = (circle[1], circle[2])
            radius = circle[-1]
            self.msp.add_circle(center, radius, dxfattribs={'color': color})

        # Добавление полилиний
        for polyline in self.polylinesT:
            color = int(polyline[0])
            points = polyline[1:]  # Получаем список координат
            # Преобразуем список в формат [(x1, y1), (x2, y2), ...]
            formatted_points = [(points[i], points[i + 1]) for i in range(0, len(points), 2)]
            self.msp.add_lwpolyline(formatted_points, dxfattribs={'color': color})
