import os

from PythonFiles.Development.Consumer.Consumer import Consumer
from PythonFiles.Development.KTPN.Automat import Automat
from PythonFiles.Development.KTPN.CableType import CableType
from PythonFiles.Development.NKY.Automat220 import Automat220


class AutomatMagnet(Automat220):
    def __init__(self,msp, doc,startX, startY,res,consumer,text:list=["A","B","E","D"],cabelName="3 жильный с 0"):
        super().__init__(msp, doc,startX, startY,res, consumer,text,cabelName)
        self.msp=msp
        self.doc=doc
        self.startX=startX
        self.startY=startY
        self.text=text

    def files(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path1 = os.path.join(current_dir, "../../../AbTxtFiles/NKY/AutomatMagnetFiles/lines.txt")
        file_path2 = os.path.join(current_dir, "../../../AbTxtFiles/NKY/AutomatMagnetFiles/polyline.txt")
        file_path3 = os.path.join(current_dir, "../../../AbTxtFiles/NKY/AutomatMagnetFiles/circle.txt")
        with open(file_path1) as file:
            self.lines = [list(map(float, line.split())) for line in file]
        with open(file_path2) as file:
            self.polylines = [list(map(float, line.split())) for line in file]
        with open(file_path3) as file:
            self.circle = [list(map(float, line.split())) for line in file]
    def consum(self):

        cons_name=["сх. у э. двиг. с кнопочным постом и каробкой зажимов","сх. у э. двиг. с кнопочным постом"]
        if self.consumer not in cons_name:
            cons = Consumer(self.msp, self.doc, self.consumer, self.startX + 4.35, self.startY - 139.83)
            self.msp.add_line((self.startX+4.35,self.startY-76), (self.startX+4.35,self.startY-139.83))
            print(self.consumer)
        else:
            cons = Consumer(self.msp, self.doc, self.consumer, self.startX + 4.35, self.startY -76)