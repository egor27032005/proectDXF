import os

import ezdxf
from ezdxf import units
import re

from PythonFiles.Development.Consumer.Consumer import Consumer


class Automat:
    def __init__(self, msp, startX, startY, text:list=["A","B","E","D"]):
        self.msp=msp
        self.text = text
        self.startX = startX
        self.startY = startY
        self.consumer = self.text[-3]
        self.first_part_text=self.text[:6]
        self.second_part_text=[self.text[-2],self.text[-1]]
        self.files()
        self.zeroPoint()
        self.transferringCoordinates()
        self.printer()
        self.getConsumer()

    def getConsumer(self):
        cs=Consumer(self.msp,self.consumer,self.startX,self.startY-192.76)

    def files(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path1 = os.path.join(current_dir, "../../../AbTxtFiles/KTPN1/AutomatFiles/Automatlines.txt")
        file_path2 = os.path.join(current_dir, "../../../AbTxtFiles/KTPN1/AutomatFiles/Automatpolyline.txt")
        file_path3 = os.path.join(current_dir, "../../../AbTxtFiles/KTPN1/AutomatFiles/Automatcircle.txt")
        with open(file_path1) as file:
            self.lines = [list(map(float, line.split())) for line in file]
        with open(file_path2) as file:
            self.polylines = [list(map(float, line.split())) for line in file]
        with open(file_path3) as file:
            self.circle = [list(map(float, line.split())) for line in file]

    def zeroPoint(self):
        # Нахождение точки для смещения
        max_list = max(self.lines, key=lambda x: x[2])
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

        # Добавление текста
        for i in range(len(self.first_part_text)):
            insertion_point = (self.startX + 5, self.startY - i * 5 - 40)
            self.msp.add_mtext(self.first_part_text[i], dxfattribs={
                'insert': insertion_point,
                'char_height': 2.5,
                'color': 1,
                'style': 'ROMANS',  # Применяем стиль Romans
                'attachment_point': 1  # Аналог AttachmentPoint в pyautocad
            })
        cord=[self.startX -5,self.startX + 1]
        for i in range(len(self.second_part_text)):
            insertion_point = (cord[i], self.startY - 190)
            self.msp.add_mtext(self.second_part_text[i], dxfattribs={
                'insert': insertion_point,
                'char_height': 2.5,
                'rotation': 90,
                'color': 1,
                'style': 'RomansStyle',  # Применяем стиль Romans
                'attachment_point': 1  # Аналог AttachmentPoint в pyautocad
            })


if __name__ == '__main__':
    # Создание нового DXF-документа
    doc = ezdxf.new('R2010', setup=True)
    doc.units = units.MM  # Устанавливаем единицы измерения (миллиметры)

    # Получаем Modelspace
    msp = doc.modelspace()

    # Текст для добавления
    text = [
        "QF2\\P3P\\PIcu=50 кА\\PIn=100 А\\PIr=90 A\\PIsd=10Ir=900А",
        "52.19410237388183",
        "83.95261765813484",
        "0.0"
    ]

    # Создание объекта Automat
    a = Automat(msp,1000, 0, text)

    # Сохранение DXF-файла
    doc.saveas("output.dxf")