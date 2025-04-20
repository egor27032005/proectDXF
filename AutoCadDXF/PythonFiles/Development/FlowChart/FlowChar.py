from PythonFiles.Development.FlowChart.BG import BG
from PythonFiles.Development.FlowChart.BoreholeOilIndustry import BoreholeOilIndustry
from PythonFiles.Development.FlowChart.DrainageTank import DrainageTank
from PythonFiles.Development.FlowChart.IY import IY
from PythonFiles.Development.FlowChart.Pipe import Pipe
from PythonFiles.Development.FlowChart.WaterIntakeWell import WaterIntakeWell
from PythonFiles.Development.FlowChart.YDX import YDX


class FlowChar:
    def __init__(self,doc,msp,name,count_borehole_oil_industry,count_water_intake_well):
        self.doc=doc
        self.msp=msp
        self.name=name
        self.count_borehole_oil_industry=count_borehole_oil_industry
        self.count_water_intake_well=count_water_intake_well
        self.startX=0
        self.startY=0
        self.pipe = Pipe(self.doc, self.msp)
        self.iy=IY(self.doc,self.msp,self.startX,self.startY,self.count_borehole_oil_industry,self.name)
        self.create_borehole_oil_industry()
        self.create_water_intake_well()
        self.drainage_tank=DrainageTank(self.doc,self.msp,self.startX-100,self.startY-100)
        self.bg = BG(self.doc, self.msp, self.startX+100, self.startY+250, self.name)
        self.ydx = YDX(self.doc, self.msp, self.startX-(count_borehole_oil_industry//2)*100-150, self.startY-50, self.name)


    def create_borehole_oil_industry(self):
        left_part=self.iy.left_points
        right_part=self.iy.right_points
        for i,part in enumerate(left_part):
            boil=BoreholeOilIndustry(self.doc,self.msp,self.startX-(150+i*100),self.startY+100+self.iy.length,"left")
            self.borehole_oil_ind(boil.pipe_start_pointX,boil.pipe_start_pointY-1.5,boil.pipe_start_pointX,part[1]-1.5)
            self.borehole_oil_ind(boil.pipe_start_pointX,part[1]-1.5,part[0]-14,part[1]-1.5)
        for i,part in enumerate(right_part):
            boil=BoreholeOilIndustry(self.doc,self.msp,self.startX+(150+i*100),self.startY+100+self.iy.length,"right")
            self.borehole_oil_ind(boil.pipe_start_pointX, boil.pipe_start_pointY-1.5, boil.pipe_start_pointX, part[1]-1.5)
            self.borehole_oil_ind(boil.pipe_start_pointX, part[1]-1.5, part[0]+14, part[1]-1.5)
    def borehole_oil_ind(self,x1,y1,x2,y2):
        layer_name = "ТХ_С_ДРЕНАЖ_035"
        line = self.msp.add_line(
            start=(x1,y1),
            end=(x2,y2),
            dxfattribs={
                "layer": layer_name,
            }
        )
    def create_water_intake_well(self):
        for boil in range(self.count_water_intake_well):
            w=WaterIntakeWell(self.doc,self.msp,239+80*boil+self.startX,self.startY+260)




