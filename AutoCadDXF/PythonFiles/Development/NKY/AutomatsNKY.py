from PythonFiles.Development.NKY.Automats.Automat220 import Automat220
from PythonFiles.Development.NKY.Automats.Automat380 import Automat380
from PythonFiles.Development.NKY.Automats.AutomatMagnet import AutomatMagnet
from PythonFiles.Development.NKY.Automats.AutomatRes import AutomatRes
from PythonFiles.Development.NKY.Automats.DivAutomat import DivAutomat


class AutomatsNKY:
    def __init__(self,msp,countAutomats,x,y,automat_consumers):
        self.msp=msp
        self.countAutomats=countAutomats
        self.x=x
        self.y=y
        self.automat_consumers=automat_consumers
        self.double_consumers=["Сх. У наружным освещением","Сх. У Э. двиг. С кнопочным постом и каробкой зажимов","Сх. У Э. двиг. С кнопочным постом"]
        self.pointsX()
        self.printAutomats()
    def pointsX(self):
        self.autPointsX=[self.x]
        for i,consumer in enumerate(self.automat_consumers[-1]):
            if consumer in self.double_consumers:
                elem=self.autPointsX[-1]+60
                self.autPointsX.append(elem)
            else:
                elem = self.autPointsX[-1] + 30
                self.autPointsX.append(elem)
    def printAutomats(self):
        for i,automat in enumerate(self.automat_consumers[0]):
            match automat:
                case "обычный 220":
                    aut=Automat220(self.msp,self.autPointsX[i],self.y)
                case "обычный 380":
                    aut = Automat380(self.msp,self.autPointsX[i],self.y)
                case "диф автомат":
                    aut=DivAutomat(self.msp,self.autPointsX[i],self.y)
                # case "резерв":
                #     aut=AutomatRes(self.msp,self.autPointsX[i],self.y)
                case "обычный  с магнитным пускателем":
                    aut=AutomatMagnet(self.msp,self.autPointsX[i],self.y)

