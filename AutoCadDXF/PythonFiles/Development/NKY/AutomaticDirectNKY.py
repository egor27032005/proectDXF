class AutomaticDirectNKY:
    def __init__(self,msp,x1,x2,x3,y):
        self.msp = msp
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y = y
        self.text1="НКУ, секция 1, 400 В, 50 Гц, 35 кА/80 кА"
        self.text2="НКУ, секция 2, 400 В, 50 Гц, 35 кА/80 кА"
        self.lines(self.x1,self.x2,self.x3,self.y)
        self.rivets(self.x1,self.y)
        self.rivets(self.x3,self.y)

        self.msp.add_line((x2+20, y+4.2), (x2+20, y + 7.55))
        self.msp.add_line((x2+7.32, y+4.2), (x2+7.32, y + 7.55))
        self.text()
        self.nonsense(self.x1)
        self.nonsense(self.x2+20)

    def lines(self,x1,x2,x3,y):

        self.msp.add_line((x1, y+5.37), (x2+7.32, y+5.37))
        self.msp.add_line((x1, y+6.37), (x2+7.32, y+6.37))

        self.msp.add_line((x2+20, y + 5.37), (x3, y + 5.37))
        self.msp.add_line((x2+20, y + 6.37), (x3, y + 6.37))


        self.msp.add_line((x1, y), (x3, y))
        self.msp.add_line((x1, y-4.69), (x3, y-4.69))
    def rivets(self,x,y):
        self.msp.add_line((x, y-0.85 ), (x, y + 0.85))
        self.msp.add_line((x, y-3.85 ), (x, y - 5.53))
        self.msp.add_line((x, y+4.2 ), (x, y + 7.55))
    def text(self):
        self.msp.add_mtext(self.text1, dxfattribs={
            'insert': (self.x1+10,self.y+11),
            'char_height': 2.5,
            'color': 1,
            'style': 'ROMANS',  # Применяем стиль Romans
            'attachment_point': 1,
            'line_spacing_factor': 1.1  # Аналог AttachmentPoint в pyautocad
        })
        self.msp.add_mtext(self.text2, dxfattribs={
            'insert': (self.x2+30, self.y + 11),
            'char_height': 2.5,
            'color': 1,
            'style': 'ROMANS',  # Применяем стиль Romans
            'attachment_point': 1,
            'line_spacing_factor': 1.1  # Аналог AttachmentPoint в pyautocad
        })
    def nonsense(self,x):
        self.msp.add_line((x+0.58, self.y +4.1), (x+4.12, self.y + 7.64), dxfattribs={'color': 3})
        self.msp.add_line((x+1.58, self.y +4.1), (x+5.12, self.y + 7.64), dxfattribs={'color': 3})
        self.msp.add_line((x+2.58, self.y +4.1), (x+6.12, self.y + 7.64), dxfattribs={'color': 3})

        self.msp.add_line((x+1.58, self.y - 1.77), (x+5.12, self.y + 1.77), dxfattribs={'color': 3})

        self.msp.add_line((x+1.58, self.y - 6.46), (x+5.12, self.y - 2.92), dxfattribs={'color': 3})

        self.msp.add_line((x+4.62, self.y - 2.92), (x+5.62, self.y - 2.92), dxfattribs={'color': 3})

