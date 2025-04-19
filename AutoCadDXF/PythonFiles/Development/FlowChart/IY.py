import ezdxf

from PythonFiles.Development.FlowChart.Block.CreateBlocks import CreateBlocks


class IY:
    def __init__(self,doc,msp,x,y,count):
        self.doc=doc
        self.msp=msp
        self.count=count
        self.x=x
        self.y=y
        self.part1()
        self.create_points()
        self.right_part()
        self.left_part()
        self.tex()
    def part1(self):
        self.count_leng=self.count-self.count//2
        self.length=55+self.count_leng*11
        self.msp.add_line((self.x, self.y), (self.x+59, self.y), dxfattribs={'color': 7})
        self.msp.add_line((self.x+59, self.y), (self.x+59, self.y+self.length), dxfattribs={'color': 7})
        self.msp.add_line((self.x, self.y+self.length), (self.x+59, self.y+self.length), dxfattribs={'color': 7})
        self.msp.add_line((self.x, self.y+self.length), (self.x, self.y), dxfattribs={'color': 7})
    def create_points(self):
        self.point = [9 + i * 11 for i in range(self.count_leng)]
        self.left_points = [[self.x, y] for y in self.point]
        self.left_points=self.left_points[::-1]
        if self.count%2==0:
            self.right_points = [[self.x+59, y] for y in self.point]
        else:
            self.right_points=[[self.x+59,self.point[y]] for y in range(len(self.point)-1)]
        self.right_points=self.right_points[::-1]
    def right_part(self):
        for point in self.right_points:
            self.msp.add_line((point[0]+6,point[1]-1.5), ((point[0],point[1]-1.5)), dxfattribs={'color': 7})

            self.msp.add_line((point[0] +1, point[1] - 3.5), ((point[0]+1, point[1] + 0.5)), dxfattribs={'color': 7})

            cr=CreateBlocks(self.doc,self.msp,point[0]+13,point[1],25,180,1)
    def left_part(self):
        for point in self.left_points:
            self.msp.add_line((point[0] - 6, point[1]-1.5), ((point[0], point[1]-1.5)), dxfattribs={'color': 7})

            self.msp.add_line((point[0] - 1, point[1] - 3.5), ((point[0] - 1, point[1] + 0.5)), dxfattribs={'color': 7})

            cr=CreateBlocks(self.doc,self.msp,point[0]-13,point[1]-3,25,0,1)
    def tex(self):
        self.msp.add_mtext("ИУ", dxfattribs={
            'insert': (self.x+40,self.y+43),
            'char_height': 20,

            'color': 7,
            'style': 'ROMANS',  # Применяем стиль Romans
            'attachment_point': 5  # Аналог AttachmentPoint в pyautocad
        })


if __name__ == "__main__":
    doc = ezdxf.new('R2010', setup=True)
    doc.units = ezdxf.units.MM
    msp = doc.modelspace()
    c=IY(doc,msp,0,0,5)
    doc.saveas("5.dxf")