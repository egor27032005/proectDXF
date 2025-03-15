import ezdxf

from PythonFiles.Development.KTPN.Automat import Automat
from PythonFiles.Development.KTPN.AutomaticDirect import AutomaticDirect
from PythonFiles.Development.KTPN.KTPN1.TableKTPN1 import TableKTPN1
from PythonFiles.Development.KTPN.Starter import Starter
from PythonFiles.Development.KTPN.Сover import Cover


class KTPN1:
    def __init__(self,msp,countAutomat,arrAutomat,arrTable):
        self.countAutomat = countAutomat
        self.msp=msp
        self.arrAutomat = arrAutomat
        self.arrForAutomat = self.arrAutomat[2:]
        self.arrForStarter = self.arrAutomat[:2]
        self.arrTable = arrTable
        self.startPointX = 500
        self.startPointY = 500
        self.table=TableKTPN1(self.msp,self.startPointX-70,self.startPointY+30,self.countAutomat,self.arrTable)
        self.starter = Starter(self.msp,self.startPointX, self.startPointY, self.arrForStarter)
        self.automat()

    def automat(self):
        point2X, point2Y = self.startPointX + 143.4, self.startPointY - 14.58
        self.automats = [Automat(self.msp, point2X + i * 35, point2Y,text=self.arrForAutomat[i]) for i in
                         range(self.countAutomat)]
        autDir=AutomaticDirect(self.msp,point2X - 59,point2X + 35 * (self.countAutomat - 1) + 15,point2Y,"r")
        cover=Cover(self.msp,self.startPointX,point2X + 35 * (self.countAutomat - 1) + 30,self.startPointY)
