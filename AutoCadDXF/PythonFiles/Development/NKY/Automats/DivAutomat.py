import os

from PythonFiles.Development.KTPN.Automat import Automat


class DivAutomat(Automat):
    def __init__(self,msp, startX, startY, text:list=["A","B","E","D"]):
        super().__init__(msp, startX, startY, text)
        self.msp=msp
        self.startX=startX
        self.startY=startY
        self.text=text

    def files(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path1 = os.path.join(current_dir, "../../../AbTxtFiles/NKY/DivAutomatFiles/lines.txt")
        file_path2 = os.path.join(current_dir, "../../../AbTxtFiles/NKY/DivAutomatFiles/polyline.txt")
        file_path3 = os.path.join(current_dir, "../../../AbTxtFiles/NKY/DivAutomatFiles/circle.txt")
        with open(file_path1) as file:
            self.lines = [list(map(float, line.split())) for line in file]
        with open(file_path2) as file:
            self.polylines = [list(map(float, line.split())) for line in file]
        with open(file_path3) as file:
            self.circle = [list(map(float, line.split())) for line in file]