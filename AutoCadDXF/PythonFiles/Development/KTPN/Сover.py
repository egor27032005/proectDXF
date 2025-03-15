class Cover:
    def __init__(self,msp,x1,x2,y):
        self.msp = msp
        self.x1 = x1
        self.x2 = x2
        self.y = y
        self.msp.add_line((x1, y), (x2, y),dxfattribs={'color': 2})
        self.msp.add_line((x1, y-147,7), (x2, y-147,7),dxfattribs={'color': 2})
        self.msp.add_line((x2, y), (x2, y-147,7),dxfattribs={'color': 2})