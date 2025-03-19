from PythonFiles.Development.NKY.Automat220 import Automat220
from PythonFiles.Development.NKY.Automat380 import Automat380
from PythonFiles.Development.NKY.AutomatMagnet import AutomatMagnet
from PythonFiles.Development.NKY.DivAutomat import DivAutomat


class AutomatsNKY:
    def __init__(self,msp,countAutomat1,countAutomat2,x,y,automat_consumers):
        self.msp=msp
        self.countAutomat1=countAutomat1
        self.countAutomat2=countAutomat2
        self.x=x
        self.y=y
        self.automat_consumers=automat_consumers
        self.double_consumers=["Сх. У наружным освещением","Сх. У Э. двиг. С кнопочным постом и каробкой зажимов","Сх. У Э. двиг. С кнопочным постом"]
        self.pointsX()
        print(self.automat_consumers[0])
        print(self.autPointsX)
        print(len(self.autPointsX))
        print(countAutomat1)
        print(countAutomat2)
        self.printAutomats()
    def pointsX(self):
        self.autPointsX=[self.x]
        for i,consumer in enumerate(self.automat_consumers[-1]):
            if i==self.countAutomat1+2:
                self.pointPartitionX = self.autPointsX[-1]+25.35
                self.autPointsX[-1] += 70
                # self.autPointsX.append(elem)
                continue

            elif (consumer in self.double_consumers or self.automat_consumers[0][i]=="обычный  с магнитным пускателем") and i!=self.countAutomat1+1:
                elem=self.autPointsX[-1]+60
                self.autPointsX.append(elem)
                continue
            elif consumer not in self.double_consumers and i!=self.countAutomat1+1:
                elem = self.autPointsX[-1] + 30
                self.autPointsX.append(elem)
    def printAutomats(self):
        for i,automat in enumerate(self.automat_consumers[0]):
            match automat:
                case "обычный":
                    aut=Automat220(self.msp,self.autPointsX[i],self.y)
                case "обычный 220":
                    aut = Automat220(self.msp, self.autPointsX[i], self.y)
                case "обычный 380":
                    aut = Automat380(self.msp,self.autPointsX[i],self.y)
                case "диф автомат":
                    aut=DivAutomat(self.msp,self.autPointsX[i],self.y)
                # case "резерв":
                #     aut=AutomatRes(self.msp,self.autPointsX[i],self.y)
                case "обычный  с магнитным пускателем":
                    aut=AutomatMagnet(self.msp,self.autPointsX[i],self.y)

