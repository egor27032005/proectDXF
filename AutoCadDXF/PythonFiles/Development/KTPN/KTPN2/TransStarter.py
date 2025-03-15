import os

from PythonFiles.Development.KTPN.Starter import Starter


class TransStarter(Starter):
    def __init__(self, msp,startX, startY, textInf):
        super().__init__(msp,startX, startY, textInf)
        self.first_part_text_cord = [(self.startX - 70, self.startY - 55), (self.startX - 1021, self.startY - 55)]

    def files(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Строим путь к файлу lines.txt
        file_path1 = os.path.join(current_dir, "../../../../AbTxtFiles/KTPN1/StarterTranspousFiles/lines.txt")
        file_path2 = os.path.join(current_dir, "../../../../AbTxtFiles/KTPN1/StarterTranspousFiles/polyline.txt")
        file_path3 = os.path.join(current_dir, "../../../../AbTxtFiles/KTPN1/StarterTranspousFiles/circle.txt")
        with open(file_path1) as file:
            self.lines = [list(map(float, line.split())) for line in file]
        with open(file_path2) as file:
            self.polylines = [list(map(float, line.split())) for line in file]
        with open(file_path3) as file:
            self.circle = [list(map(float, line.split())) for line in file]

    def zeroPoint(self):
        max_list = max(self.lines, key=lambda x: x[1])
        self.x, self.y = max_list[1], max(max_list[2], max_list[4])
        self.distanceX = self.startX - self.x
        self.distanceY = self.startY - self.y
        self.list_start = [max_list[1] + self.distanceX, max_list[2] + self.distanceY,
                           max_list[3] + self.distanceX, max_list[4] + self.distanceY]

    def other_text(self):
        x = self.startX
        y = self.startY
        texts = {"1500/5": (x - 25, y - 118), "2500/5": (x - 80, y - 116), "PE": (x - 40, y - 133),
                 "N": (x - 89, y - 133), "A": (x - 72.5, y - 24.5), "V": (x - 81.5, y - 24.5), "Wh": (x - 78, y - 35),
                 "РУНН": (x - 94, y - 12),"T1\nТМГ-1600 кВа\n10/0.4":(x - 95, y + 17)}

        for i in range(len(texts)):
            self.msp.add_mtext(list(texts.items())[i][0], dxfattribs={
                'insert': list(texts.items())[i][1],
                'char_height': 2.5,

                'color': 1,
                'style': 'RomansStyle',  # Применяем стиль Romans
                'attachment_point': 5 # Аналог AttachmentPoint в pyautocad
            })