class YDX:
    def __init__(self,doc,msp,startX,startY,name):
        self.doc=doc
        self.msp=msp
        self.startX=startX
        self.startY=startY
        self.name="УДХ-"+name
        self.part1()
        self.tex()

    def put_line(self, x1, y1, x2, y2):
        layer_name = "Tehnolog"
        line = self.msp.add_line(
            start=(x1, y1),
            end=(x2, y2),
            dxfattribs={
                "layer": layer_name,
            }
        )

    def part1(self):
        self.length = 95
        self.hight = 75
        self.put_line(self.startX, self.startY, self.startX + self.length, self.startY)
        self.put_line(self.startX + self.length, self.startY, self.startX + self.length, self.startY + self.hight)
        self.put_line(self.startX, self.startY + self.hight, self.startX + self.length, self.startY + self.hight)
        self.put_line(self.startX, self.startY + self.hight, self.startX, self.startY)


    def tex(self):
        self.msp.add_mtext(self.name, dxfattribs={
            'insert': (self.startX+40,self.startY+50),
            'char_height': 16,

            'color': 7,
            'style': 'ROMANS',  # Применяем стиль Romans
            'attachment_point': 5  # Аналог AttachmentPoint в pyautocad
        })