import math
import os


from PythonFiles.Development.Consumer.Consumer import Consumer
from PythonFiles.Development.KTPN.Automat import Automat
from PythonFiles.Development.KTPN.CableType import CableType


class Automat220():
    def __init__(self,msp, doc,startX, startY, res,consumer,text:list=["A","B","E","D"],cabelName="3 жильный с 0"):
        self.msp=msp
        self.startX=startX
        self.startY=startY
        self.text=text
        self.consumer=consumer
        self.doc=doc
        self.res=res
        self.cabelName=cabelName
        self.cabelLengt=95
        self.first_part_text = self.text[:6]
        self.second_part_text = [self.text[-2], self.text[-1]]
        self.files()
        self.zeroPoint()
        self.transferringCoordinates()
        if res==True:
            self.linesT=self.reserve()
        else:
            self.cabel = CableType(self.msp,self.cabelName, self.startX+4.34, self.startY -self.cabelLengt)
            self.consum()
        self.printer()

    def consum(self):
        len=139.83
        cons = Consumer(self.msp, self.doc, self.consumer, self.startX + 4.35, self.startY -len)
    def files(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path1 = os.path.join(current_dir, "../../../AbTxtFiles/NKY/Automat220Files/lines.txt")
        file_path2 = os.path.join(current_dir, "../../../AbTxtFiles/NKY/Automat220Files/polyline.txt")
        file_path3 = os.path.join(current_dir, "../../../AbTxtFiles/NKY/Automat220Files/circle.txt")
        with open(file_path1) as file:
            self.lines = [list(map(float, line.split())) for line in file]
        with open(file_path2) as file:
            self.polylines = [list(map(float, line.split())) for line in file]
        with open(file_path3) as file:
            self.circle = [list(map(float, line.split())) for line in file]
    def reserve(self):
        max_distance = 79  # Максимальное допустимое расстояние
        clipped_lines = []  # Список для хранения обрезанных прямых

        for line in self.linesT:
            color, x1, y1, x2, y2 = line  # Распаковываем данные прямой

            # Проверяем, находятся ли обе точки в допустимой зоне
            if abs(y1 - self.startY) <= max_distance and abs(y2 - self.startY) <= max_distance:
                # Если обе точки в зоне, добавляем прямую без изменений
                clipped_lines.append([color, x1, y1, x2, y2])
            else:
                # Если хотя бы одна точка выходит за пределы, обрезаем прямую
                # Вычисляем новые координаты для точек, которые выходят за пределы
                if abs(y1 - self.startY) > max_distance:
                    # Если первая точка выходит за пределы, обрезаем её
                    y1 = self.startY + max_distance if y1 > self.startY else self.startY - max_distance
                if abs(y2 - self.startY) > max_distance:
                    # Если вторая точка выходит за пределы, обрезаем её
                    y2 = self.startY + max_distance if y2 > self.startY else self.startY - max_distance

                # Добавляем обрезанную прямую в список
                clipped_lines.append([color, x1, y1, x2, y2])

        return clipped_lines



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
            self.msp.add_circle(
                center,
                radius,
                dxfattribs={'color': 2}
            )

            # Добавляем заливку (HATCH) для круга
            hatch = self.msp.add_hatch(color=2)  # 2 — это желтый цвет
            hatch.set_solid_fill(color=2)  # Устанавливаем сплошную заливку желтым цветом

            # Создаем полилинию, аппроксимирующую окружность
            points = self.get_circle_points(center, radius, num_points=36)  # 36 точек для аппроксимации
            hatch.paths.add_polyline_path(points)


        # Добавление полилиний
        for polyline in self.polylinesT:
            color = int(polyline[0])
            points = polyline[1:]  # Получаем список координат
            # Преобразуем список в формат [(x1, y1), (x2, y2), ...]
            formatted_points = [(points[i], points[i + 1]) for i in range(0, len(points), 2)]
            self.msp.add_lwpolyline(formatted_points, dxfattribs={'color': color})

        # Добавление текста
        for i in range(len(self.first_part_text)):
            insertion_point = (self.startX + 7, self.startY - i * 5 -17)
            self.msp.add_mtext(self.first_part_text[i], dxfattribs={
                'insert': insertion_point,
                'char_height': 2.5,
                'color': 1,
                'style': 'ROMANS',  # Применяем стиль Romans
                'attachment_point': 1,
                'line_spacing_factor': 1.1  # Аналог AttachmentPoint в pyautocad
            })
        if self.res==False:
            cord = [self.startX , self.startX + 5]
            for i in range(len(self.second_part_text)):
                insertion_point = (cord[i], self.startY - 138)
                self.msp.add_mtext(self.second_part_text[i], dxfattribs={
                    'insert': insertion_point,
                    'char_height': 2.5,
                    'rotation': 90,
                    'color': 1,
                    'style': 'ROMANS',  # Применяем стиль Romans
                    'attachment_point': 1  # Аналог AttachmentPoint в pyautocad
                })

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