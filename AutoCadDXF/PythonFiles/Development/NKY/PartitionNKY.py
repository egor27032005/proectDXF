import math
import os

from PythonFiles.Development.KTPN.KTPN2.Partition import Partition


class PartitionNKY(Partition):
    def __init__(self,msp, startX, startY, text):
        super().__init__(msp, startX, startY, text)
        self.msp = msp
        self.startX = startX
        self.startY = startY
        self.text = text
    def files(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path1 = os.path.join(current_dir, "../../../AbTxtFiles/NKY/PartitionFiles/lines.txt")
        file_path2 = os.path.join(current_dir, "../../../AbTxtFiles/NKY/PartitionFiles/polyline.txt")
        file_path3 = os.path.join(current_dir, "../../../AbTxtFiles/NKY/PartitionFiles/circle.txt")
        with open(file_path1) as file:
            self.lines = [list(map(float, line.split())) for line in file]
        with open(file_path2) as file:
            self.polylines = [list(map(float, line.split())) for line in file]
        with open(file_path3) as file:
            self.circle = [list(map(float, line.split())) for line in file]
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
            self.msp.add_circle(center, radius, dxfattribs={'color': 2})
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
        self.ozer_text()

    def ozer_text(self):
        x = self.startX
        y = self.startY
        texts = {"ABP": [x+10, y-33]}
        for text, coords in texts.items():
            self.msp.add_text(text, dxfattribs={'insert': (coords[0], coords[1]), 'height': 2.5, 'color': 1})
    def textPr(self):
        insertion_point = (self.startX+6, self.startY)
        text = "\n".join(self.text[:6])
        self.msp.add_mtext(text, dxfattribs={
            'insert': insertion_point,
            'char_height': 2.5,
            'line_spacing_factor': 1.2,
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