import itertools

from PythonFiles.Development.FlowChart.Block.CreateBlocks import CreateBlocks


class DrainageTank:
    def __init__(self,doc,msp,startX,startY):
        self.doc=doc
        self.msp=msp
        self.startX=startX
        self.startY=startY
        self.layer_name = "Оборудование"
        self.lines=[[256, 6.447460942170892, 15.101721831910254, 10.197460942170892, 22.601721831910254],
                    [256, 6.447460942170892, 15.101721831910254, 6.447460942170892,7.601721831910254],
                    [256, 6.447460942170892, 7.601721831910254, 10.197460942170892, 0.10172183191025397],
                    [256, 38.32246094217089, 7.601721831910254, 34.57246094217089, 0.10172183191025397],
                    [256, 38.32246094217089,7.601721831910254, 38.32246094217089, 15.101721831910254],
                    [256, 34.57246094217089, 33.851721831910254, 23.322460942170892, 33.851721831910254],
                    [256, 10.197460942170892, 33.851721831910254, 21.447460942170892, 33.851721831910254],
                    [256, 38.32246094217089, 15.101721831910254, 34.57246094217089, 22.601721831910254]]
        self.polylines=[[256, 12.072460564364036, 33.85172165104261, 19.572015660606894, 33.85172165104261, 19.572015660606894, 22.60172689959859, 12.072458795229068, 22.60172689959859, 12.072458795229068, 33.84581181107296],
                        [256, 25.171435737970768, 33.85411368256693, 32.670990834213626, 33.85411368256693, 32.670990834213626, 22.604118931122912, 25.1714339688358, 22.604118931122912, 25.1714339688358, 33.848203842597286],
                        [256, 34.57246052548203, 22.60172294909239, 10.199504066142708, 22.60172294909239, 10.199504066142708, 0.10135725498332704, 34.57263671129067, 0.10135725498332704, 34.57263671129067, 22.601724265927828]]
        self.zeroPoint()
        self.transferringCoordinates()
        self.printer()
        self.tex()
        self.ozer()

    def bottom(self,len,x,y):
        self.msp.add_line((x,y), (x +len, y), dxfattribs={'color': 7,"layer": "To_dim"})
        for x0 in range(int(x+1),int(x +len),3):
            self.msp.add_line((x0, y), (x0-3, y-3), dxfattribs={'color': 7,"layer": "To_dim"})

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
    def ozer(self):
        self.bottom(26,self.startX-20.38,self.startY+13.13)
        self.bottom(75,self.startX+33.29,self.startY+13.13)
        self.msp.add_line((self.startX+26.22, self.startY+13.13), (self.startX+33.29, self.startY+13.13), dxfattribs={'color': 7,"layer": "To_dim"})
        self.msp.add_line((self.startX+13.12, self.startY+13.13), (self.startX+18.72, self.startY+13.13), dxfattribs={'color': 7,"layer": "To_dim"})

        c=CreateBlocks(self.doc,self.msp,self.startX-12,self.startY+33,"41-blue",0,1,171,"To_dim")
        c.block41()
        c.insert_block()
        self.put_line(self.startX -12, self.startY+33, self.startX -12, self.startY + 14.4,"To_dim",171)
        self.put_line(self.startX -12, self.startY +  14.4, self.startX -7.06, self.startY + 14.4,"To_dim",171)
        self.put_line(self.startX -1.06, self.startY +  14.4, self.startX +0.4, self.startY + 14.4,"To_dim",171)
        self.put_line(self.startX +2.65, self.startY +  14.4, self.startX +4.21, self.startY + 14.4,"To_dim",171)

        self.put_line(self.startX +0.4, self.startY +  14.4, self.startX +2.65, self.startY + 13.2,"To_dim",171)
        self.put_line(self.startX +0.4, self.startY +  14.4, self.startX +2.65, self.startY + 15.6,"To_dim",171)
        self.put_line(self.startX +2.65, self.startY +  13.2, self.startX +2.65, self.startY + 15.6,"To_dim",171)

        self.put_line(self.startX +4.21, self.startY +  13.6, self.startX +4.21, self.startY + 15,"To_dim",7)
        self.put_line(self.startX +4.71, self.startY +  13.6, self.startX +4.71, self.startY + 15,"To_dim",7)
        self.put_line(self.startX +4.71, self.startY +  14.4, self.startX +5.62, self.startY + 14.4,"To_dim",7)

        CreateBlocks(self.doc,self.msp,self.startX-1.06,self.startY+13.13,40,90,1.4,layer="To_dim")

    def printer(self):
        for line in self.linesT:
            color = int(line[0])
            start_point = (line[1], line[2])
            end_point = (line[3], line[4])
            self.msp.add_line(
                start=start_point,
                end=end_point,
                dxfattribs={
                    "layer": self.layer_name,
                }
            )
        for polyline in self.polylinesT:
            color = int(polyline[0])
            points = polyline[1:]  # Получаем список координат
            # Преобразуем список в формат [(x1, y1), (x2, y2), ...]
            formatted_points = [(points[i], points[i + 1]) for i in range(0, len(points), 2)]
            self.msp.add_lwpolyline(formatted_points, dxfattribs={'color': color})
            self.msp.add_lwpolyline(formatted_points,
                dxfattribs={
                    "layer": self.layer_name,
                }
            )
    def put_line(self, x1, y1, x2, y2,layer_name = "Tehnolog",color=7):
        self.msp.add_line(
            start=(x1, y1),
            end=(x2, y2),
            dxfattribs={
                "layer": layer_name,
                "color":color
            }
        )
    def tex(self):
        self.msp.add_mtext("ЕД", dxfattribs={
            'insert': (self.startX+15,self.startY-5),
            'char_height': 8,

            'color': 7,
            'style': 'ROMANS',  # Применяем стиль Romans
            'attachment_point': 5  # Аналог AttachmentPoint в pyautocad
        })