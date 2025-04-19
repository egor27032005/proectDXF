import os

import ezdxf

from PythonFiles.Development.FlowChart.Block.CreateBlocks import CreateBlocks


class BoreholeOilIndustry:
    def __init__(self,doc,msp,startX,startY,direction):
        self.msp=msp
        self.doc=doc
        self.startX=startX
        self.startY=startY
        self.direction=direction
        self.objects={23: [(0.0, 1.0, (27.640687083450985, 40.37984068660205, 0.0))],
                      34: [(0.0, 1.1231315516799023, (6.648013938961185, 63.54034185793682, 0.0)),
                           (0.0, 1.1231315516799023, (33.26876401557888, 60.11040265948361, 0.0)),
                           (0.0, 1.2292910580805028, (32.775740104586134, 80.2708374142108, 0.0)),
                           (270.0, 1.0937057964353412, (26.882434347048047, 75.48555799848819, 0.0))],
                      35: [(0.0, 1.0, (17.908035962853546, 60.24179992793631, 0.0)), (270.0, 1.0, (26.98579135643763, 92.74280591483802, 0.0))],
                      30: [(0.0, 1.0, (41.520341265208174, 80.9088255269065, 0.0))],
                      31: [(180.0, 1.0, (58.49454770127545, 64.23891234367261, 0.0))],
                      37: [(270.0, 1.0, (28.669445524906962, 101.27875255201997, 0.0))]}


        self.files()
        self.zeroPoint()
        self.transferringCoordinates()
        self.printer()
        self.create()
        self.direct()

    def create(self):
        for key, value in self.objects.items():
            for lis in value:
                c=CreateBlocks(self.doc,self.msp,lis[2][0]+self.distanceX,lis[2][1]+self.distanceY,key,lis[0],lis[1])
    def direct(self):
        x=self.startX+64.2
        y=self.startY-57.42
        if self.direction=="left":
            self.msp.add_line((x,y), (x+6.7,y), dxfattribs={'color': 7})
            self.msp.add_line((x+13.5,y), (x+33.28,y), dxfattribs={'color': 7})
            self.msp.add_line((x+40,y), (x+51,y), dxfattribs={'color': 7})
            self.msp.add_line((x+51,y), (x+51,y-14), dxfattribs={'color': 7})
            self.bottom(x+51,y-14)

            cr=CreateBlocks(self.doc,self.msp,x+6.7,y-1.5,26,1,1.95)
            cr2=CreateBlocks(self.doc,self.msp,x+33.28,y-1.5,34,1,1)

            self.pipe_start_pointX=x+51
            self.pipe_start_pointY=y-14
        else:
            self.msp.add_line((x, y), (x - 6.7, y), dxfattribs={'color': 7})
            self.msp.add_line((x - 13.5, y), (x - 33.28, y), dxfattribs={'color': 7})
            self.msp.add_line((x - 40, y), (x - 51, y), dxfattribs={'color': 7})
            self.msp.add_line((x - 51, y), (x - 51, y-14), dxfattribs={'color': 7})
            self.bottom(x - 51, y-14)

            cr = CreateBlocks(self.doc, self.msp, x - 13.5, y-1.5, 26, 1, 1.95)
            cr2 = CreateBlocks(self.doc, self.msp, x - 39.88, y-1.5, 34, 1, 1)

            self.pipe_start_pointX = x - 51
            self.pipe_start_pointY = y - 14

    def bottom(self,x,y):
        self.msp.add_line((x-10, y), (x +10, y), dxfattribs={'color': 7})
        for x0 in [x-6,x-3,x,x+3,x+6,x+9]:
            self.msp.add_line((x0, y), (x0-3, y-3), dxfattribs={'color': 7})



        
    def files(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path1 = os.path.join(current_dir, "../../../AbTxtFiles/FlowChart/BoreholeOilIndustryFiles/lines.txt")
        file_path2 = os.path.join(current_dir, "../../../AbTxtFiles/FlowChart/BoreholeOilIndustryFiles/polyline.txt")
        with open(file_path1) as file:
            self.lines = [list(map(float, line.split())) for line in file]
        with open(file_path2) as file:
            self.polylines = [list(map(float, line.split())) for line in file]


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

        # Добавление полилиний
        for polyline in self.polylinesT:
            color = int(polyline[0])
            points = polyline[1:]  # Получаем список координат
            # Преобразуем список в формат [(x1, y1), (x2, y2), ...]
            formatted_points = [(points[i], points[i + 1]) for i in range(0, len(points), 2)]
            self.msp.add_lwpolyline(formatted_points, dxfattribs={'color': color})

if __name__ == "__main__":
    doc = ezdxf.new('R2010', setup=True)
    doc.units = ezdxf.units.MM
    msp = doc.modelspace()
    b=BoreholeOilIndustry(doc,msp,100,100,"left")
    doc.saveas("222222.dxf")

