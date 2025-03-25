from PythonFiles.Development.NKY.AutomaticDirectNKY import AutomaticDirectNKY
from PythonFiles.Development.NKY.AutomatsNKY import AutomatsNKY
from PythonFiles.Development.NKY.CoverNKY import CoverNKY
from PythonFiles.Development.NKY.FirstPartTableNKY import FirstPartTableNKY
from PythonFiles.Development.NKY.PartitionNKY import PartitionNKY


class NKY:
    def __init__(self,msp,countAutomat1,countAutomat2,automat_consumers,doc,part_list):
        self.countAutomat1 = countAutomat1
        self.countAutomat2 = countAutomat2
        self.msp=msp
        self.doc=doc
        self.automat_consumers=automat_consumers
        self.part_list=part_list
        self.automatX=0
        self.automatY=0
        self.automats=AutomatsNKY(self.msp,self.doc,self.countAutomat1,self.countAutomat2,self.automatX,self.automatY,self.automat_consumers,self.part_list[2])
        point=self.automats.autPointsX[-2]+13.5
        self.direct=AutomaticDirectNKY(self.msp,self.automatX-9,self.automats.pointPartitionX,point,self.automatY)
        self.part = PartitionNKY(self.msp, self.automats.pointPartitionX, self.automatY - 22.41,self.part_list[0])
        self.automats.printAutomats()
        self.cover=CoverNKY(self.msp,self.automatX-10,point+15,self.automatY+17,self.automatY-83)
        self.fptn=FirstPartTableNKY(self.msp,self.automatX-90,self.automatY+17)

    # def text_preparation(self):
    #     for i in self.automat_consumers:
