import os

import ezdxf

class Starter:
    def __init__(self, msp,startX, startY, textInf):
        self.textInf = textInf
        self.startX = startX
        self.startY = startY
        self.msp = msp
        self.first_part_text=[a[:6] for a in textInf]
        self.first_part_text_cord=[(self.startX+70,self.startY-55),(self.startX+121,self.startY-55)]

        self.files()
        self.zeroPoint()
        self.transferringCoordinates()
        self.printer()
        self.text()
        self.other_text()

    def files(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Строим путь к файлу lines.txt
        file_path1 = os.path.join(current_dir, "../../../AbTxtFiles/KTPN1/StarterFiles/lines.txt")
        file_path2 = os.path.join(current_dir, "../../../AbTxtFiles/KTPN1/StarterFiles/polyline.txt")
        file_path3 = os.path.join(current_dir, "../../../AbTxtFiles/KTPN1/StarterFiles/circle.txt")
        with open(file_path1) as file:
            self.lines = [list(map(float, line.split())) for line in file]
        with open(file_path2) as file:
            self.polylines = [list(map(float, line.split())) for line in file]
        with open(file_path3) as file:
            self.circle = [list(map(float, line.split())) for line in file]

    def zeroPoint(self):
        max_list = min(self.lines, key=lambda x: x[1])
        self.x, self.y = max_list[1], max(max_list[2], max_list[4])
        self.distanceX = self.startX - self.x
        self.distanceY = self.startY - self.y
        self.list_start = [max_list[1] + self.distanceX, max_list[2] + self.distanceY,
                           max_list[3] + self.distanceX, max_list[4] + self.distanceY]

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
            start = (line[1], line[2])
            end = (line[3], line[4])
            self.msp.add_line(start, end, dxfattribs={'color': color})

        for circle in self.circleT:
            color = int(circle[0])
            center = (circle[1], circle[2])
            radius = circle[-1]
            self.msp.add_circle(center, radius, dxfattribs={'color': color})

        for number in self.polylinesT:
            color = int(number[0])
            points = list(zip(number[1::2], number[2::2]))
            self.msp.add_lwpolyline(points, dxfattribs={'color': color})

    def text(self):
        for i in range(len(self.first_part_text)):
            text="\n".join(self.first_part_text[i])
            self.msp.add_mtext(text, dxfattribs={
                'insert': self.first_part_text_cord[i],
                'char_height': 2.5,
                'line_spacing_factor': 1.2,
                'color': 1,
                'style': 'ROMANS',  # Применяем стиль Romans
                'attachment_point': 1  # Аналог AttachmentPoint в pyautocad
            })

    def other_text(self):
        x = self.startX
        y = self.startY
        texts = {"1500/5": (x + 19, y - 116), "2500/5": (x + 73, y - 114), "PE": (x + 35, y - 131),
                 "N": (x + 80, y - 131), "A": (x + 72.4, y - 24.5), "V": (x + 81.5, y - 24.5), "Wh": (x + 77.5, y - 35),
                 "РУНН": (x + 89, y - 10), "0,4 кВ, 50 Гц": (x + 113, y - 10),"T1\nТМГ-1600 кВа\n10/0.4":(x + 85, y + 17)}

        for i in range(len(texts)):
            self.msp.add_mtext(list(texts.items())[i][0], dxfattribs={
                'insert': list(texts.items())[i][1],
                'char_height': 2.5,

                'color': 1,
                'style': 'ROMANS',  # Применяем стиль Romans
                'attachment_point': 5 # Аналог AttachmentPoint в pyautocad
            })
        # mtext = "T1\nТМГ-1600 кВа\n10/0.4"
        # insertion_point = (x + 75, y + 23)
        # self.msp.add_mtext(mtext, dxfattribs={
        #     'insert': insertion_point,
        #     'char_height': 2.5,
        #     'color': 1,
        #     'attachment_point': 2,
        #     'style': 'RomansStyle'  # Применяем стиль Romans
        # })


if __name__ == '__main__':
    textInf = [["Пример текста 1", "Пример текста 2"], ["Дополнительный текст"]]
    starter = Starter(150, 0, "output.dxf", textInf)