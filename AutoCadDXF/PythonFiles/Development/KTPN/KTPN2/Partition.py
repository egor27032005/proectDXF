import os

import ezdxf
from ezdxf import units

class Partition:
    def __init__(self, msp, startX, startY, text:list=["Sample Text"]):
        self.msp = msp
        self.startX = startX
        self.startY = startY
        self.text = text
        self.files()
        self.zeroPoint()
        self.transferringCoordinates()
        self.printer()
        self.textPr()

    def files(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path1 = os.path.join(current_dir, "../../../../AbTxtFiles/KTPN1/PartitionFiles/lines.txt")
        file_path2 = os.path.join(current_dir, "../../../../AbTxtFiles/KTPN1/PartitionFiles/polyline.txt")
        file_path3 = os.path.join(current_dir, "../../../../AbTxtFiles/KTPN1/PartitionFiles/circle.txt")
        with open(file_path1) as file:
            self.lines = [list(map(float, line.split())) for line in file]
        with open(file_path2) as file:
            self.polylines = [list(map(float, line.split())) for line in file]
        with open(file_path3) as file:
            self.circle = [list(map(float, line.split())) for line in file]

    def zeroPoint(self):
        max_list = max(self.lines, key=lambda x: x[2])
        self.x, self.y = max_list[1], max_list[2]
        self.distanceX = self.startX - self.x
        self.distanceY = self.startY - self.y

    def transferringCoordinates(self):
        self.linesT = [self.transform(line) for line in self.lines]
        self.polylinesT = [self.transform(line) for line in self.polylines]
        self.circleT = [[cir[0], cir[1] + self.distanceX, cir[2] + self.distanceY, cir[3]] for cir in self.circle]

    def transform(self, sublist):
        for i in range(len(sublist)):
            if i == 0:
                continue  # Нулевой элемент не изменяем
            elif i % 2 == 0:
                sublist[i] += self.distanceY  # Чётные позиции
            else:
                sublist[i] += self.distanceX  # Нечётные позиции
        return sublist

    def printer(self):
        for line in self.linesT:
            color = int(line[0])
            start_point = (line[1], line[2])
            end_point = (line[3], line[4])
            self.msp.add_line(start_point, end_point, dxfattribs={'color': color})

        # Добавление кругов
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
        self.ozer_text()
    def textPr(self):
        insertion_point = (self.startX -24, self.startY- 40)
        text = "\n".join(self.text[:6])
        self.msp.add_mtext(text, dxfattribs={
            'insert': insertion_point,
            'char_height': 2.5,
            'line_spacing_factor': 1.2,
            'color': 1,
            'style': 'ROMANS',  # Применяем стиль Romans
            'attachment_point': 1  # Аналог AttachmentPoint в pyautocad
        })


    def ozer_text(self):
        x = self.startX
        y = self.startY
        texts = {"ABP": [x-16, y-101.7], "2500/5": [x-27, y-110]}
        for text, coords in texts.items():
            self.msp.add_text(text, dxfattribs={'insert': (coords[0], coords[1]), 'height': 2.5, 'color': 1})

if __name__ == '__main__':
    doc = ezdxf.new('R2010')  # Создаем новый документ DXF
    msp = doc.modelspace()  # Получаем пространство модели
    partition = Partition(msp, 100, 0, ["Sample Text"])
    doc.saveas("output.dxf")  # Сохраняем документ в файл