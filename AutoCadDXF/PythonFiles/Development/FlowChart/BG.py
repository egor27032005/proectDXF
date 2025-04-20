class BG:
    def __init__(self,doc,msp,startX,startY,name):
        self.doc=doc
        self.msp=msp
        self.startX=startX
        self.startY=startY
        self.name="БГ-"+name
        self.part1()
        self.pipes()
        self.tex()
    def put_line(self,x1,y1,x2,y2):
        layer_name = "Tehnolog"
        line = self.msp.add_line(
            start=(x1,y1),
            end=(x2,y2),
            dxfattribs={
                "layer": layer_name,
            }
        )
    def put_line_water(self,x1,y1,x2,y2):
        layer_name = "TO_water"
        line = self.msp.add_line(
            start=(x1,y1),
            end=(x2,y2),
            dxfattribs={
                "layer": layer_name,
            }
        )
    def bottom(self,x,y):
        self.msp.add_line((x-10, y), (x +10, y), dxfattribs={'color': 7,"layer": "To_dim"})
        for x0 in [x-6,x-3,x,x+3,x+6,x+9]:
            self.msp.add_line((x0, y), (x0-3, y-3), dxfattribs={'color': 7,"layer": "To_dim"})
    def pipes(self):
        self.put_line_water(self.startX,self.startY+22,self.startX-40,self.startY+22)
        self.put_line_water(self.startX-40,self.startY+22,self.startX-40,self.startY-2)

        self.put_line_water(self.startX, self.startY + 32, self.startX - 49, self.startY + 32)
        self.put_line_water(self.startX - 49, self.startY + 32, self.startX - 49, self.startY - 2)

        self.put_line_water(self.startX, self.startY + 42, self.startX - 67, self.startY + 42)
        self.put_line_water(self.startX - 67, self.startY + 42, self.startX - 67, self.startY - 2)

        self.bottom(self.startX-44,self.startY - 2)
        self.bottom(self.startX-68,self.startY - 2)


    def part1(self):
        self.length=100
        self.hight=175
        self.put_line(self.startX, self.startY,self.startX+self.length, self.startY)
        self.put_line(self.startX+self.length, self.startY,self.startX+self.length, self.startY+self.hight)
        self.put_line(self.startX, self.startY+self.hight,self.startX+self.length, self.startY+self.hight)
        self.put_line(self.startX, self.startY+self.hight,self.startX, self.startY)


    def tex(self):
        self.msp.add_mtext(self.name, dxfattribs={
            'insert': (self.startX+50,self.startY+100),
            'char_height': 16,

            'color': 7,
            'style': 'ROMANS',  # Применяем стиль Romans
            'attachment_point': 5  # Аналог AttachmentPoint в pyautocad
        })