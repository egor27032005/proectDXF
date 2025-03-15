from PythonFiles.Development.Consumer.El_dvig import El_dvig
from PythonFiles.Development.Consumer.Wardrobe import Wardrobe


class Consumer:
    def __init__(self,msp,name,x,y):
        self.msp=msp
        self.name=name
        self.x=x
        self.y=y
        self.getConsumer()

    def getConsumer(self):
        match self.name:
            case "Шкаф":
                cons=Wardrobe(self.msp,self.x,self.y)
            case "Э. двигатель":
                cons=El_dvig(self.msp,self.x,self.y)



