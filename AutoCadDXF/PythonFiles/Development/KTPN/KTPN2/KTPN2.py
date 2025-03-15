import itertools

from PythonFiles.Development.KTPN.Automat import Automat
from PythonFiles.Development.KTPN.AutomaticDirect import AutomaticDirect
from PythonFiles.Development.KTPN.KTPN2.Partition import Partition
from PythonFiles.Development.KTPN.KTPN2.Table2KTPN import Table2KTN
from PythonFiles.Development.KTPN.KTPN2.TransStarter import TransStarter
from PythonFiles.Development.KTPN.Starter import Starter
from PythonFiles.Development.KTPN.Сover import Cover


class KTPN2:
    def __init__(self,msp,countAutomat1,countAutomat2,text_table,automat_table,text_part):
        self.msp=msp
        self.countAutomat1 = countAutomat1
        self.countAutomat2 = countAutomat2
        self.text_table = text_table
        self.automat_table = automat_table
        self.text_part = text_part
        self.arrForAutomat = self.automat_table[2:]
        self.arrForStarter = self.automat_table[:2]
        self.startX = 0
        self.startY = 0
        self.startAutomatY = self.startY - 14.58
        self.startAutomatX = self.startX + 143.36
        self.automat()
        self.point_second_part = self.pointsAutomatX[-1] + 148.36
        self.starters()
        self.table = Table2KTN(self.msp, self.startX - 92, self.point_second_part + 2, self.startY + 30,
                               self.countAutomat1, self.countAutomat2, self.text_table)
        self.cov = Cover(self.msp, self.startX, self.point_second_part + 2, self.startY)

    def automat(self):
        pointsAutomatX1 = [x * 35 + self.startAutomatX for x in range(self.countAutomat1)]
        pointsAutomatX2 = [x * 35 + pointsAutomatX1[-1] + 86 for x in range(self.countAutomat2)]
        self.pointsAutomatX = list(itertools.chain(pointsAutomatX1, pointsAutomatX2))
        self.automats = [Automat( self.msp,self.pointsAutomatX[x], self.startAutomatY, self.automat_table[x + 2]) for x
                         in range(len(self.pointsAutomatX))]
        self.partition = Partition(self.msp, pointsAutomatX2[0] - 29.125, self.startAutomatY, self.text_part)
        autDir = AutomaticDirect(self.msp, pointsAutomatX1[0] - 59, pointsAutomatX1[-1] +35, self.startAutomatY, "r")
        autDir2 = AutomaticDirect(self.msp, pointsAutomatX2[0]-35, pointsAutomatX2[-1] +65.215, self.startAutomatY, "l")

    def starters(self):
        self.starter = Starter(self.msp, self.startX, self.startY, self.arrForStarter)
        self.starter2=TransStarter(self.msp, self.pointsAutomatX[-1]+149.62, self.startY, self.arrForStarter)