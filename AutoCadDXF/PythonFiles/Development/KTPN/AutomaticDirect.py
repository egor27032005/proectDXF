class AutomaticDirect:
    def __init__(self,msp,x1,x2,y,count=None):
        self.msp=msp
        self.x1=x1
        self.x2=x2
        self.y=y
        self.msp.add_line((x1, y), (x2,y))
        self.msp.add_line((x1, y+0.35), (x2,y+0.35))
        if count!=None:
            if count=="l":self.msp.add_line((x1, y-0.95), (x1,y+0.95))
            elif count=="r":self.msp.add_line((x2, y-0.95), (x2,y+0.95))
            else:
                self.msp.add_line((x2, y - 0.95), (x2, y + 0.95))
                self.msp.add_line((x1, y - 0.95), (x1, y + 0.95))

