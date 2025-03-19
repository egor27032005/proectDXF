import os

from PythonFiles.Development.KTPN.KTPN2.Partition import Partition


class PartitionNKY(Partition):
    def __init__(self,msp, startX, startY, text:list=["Sample Text"]):
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

    def ozer_text(self):
        x = self.startX
        y = self.startY
        texts = {"ABP": [x+16, y-29]}
        for text, coords in texts.items():
            self.msp.add_text(text, dxfattribs={'insert': (coords[0], coords[1]), 'height': 2.5, 'color': 1})
    def textPr(self):
        insertion_point = (self.startX - 24, self.startY - 40)
        # text = "\n".join(self.text[:6])
        # self.msp.add_mtext(text, dxfattribs={
        #     'insert': insertion_point,
        #     'char_height': 2.5,
        #     'line_spacing_factor': 1.2,
        #     'color': 1,
        #     'style': 'ROMANS',  # Применяем стиль Romans
        #     'attachment_point': 1  # Аналог AttachmentPoint в pyautocad
        # })