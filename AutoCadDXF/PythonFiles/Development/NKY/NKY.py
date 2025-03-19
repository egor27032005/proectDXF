from PythonFiles.Development.NKY.AutomatsNKY import AutomatsNKY
from PythonFiles.Development.NKY.PartitionNKY import PartitionNKY


class NKY:
    def __init__(self,msp,countAutomat1,countAutomat2,automat_consumers):
        self.countAutomat1 = countAutomat1
        self.countAutomat2 = countAutomat2
        self.msp=msp
        self.automat_consumers=automat_consumers
        self.automatX=0
        self.automatY=0
        self.automats=AutomatsNKY(self.msp,self.countAutomat1,self.countAutomat2,self.automatX,self.automatY,self.automat_consumers)
        self.part=PartitionNKY(self.msp,self.automats.pointPartitionX,self.automatY-22.41)