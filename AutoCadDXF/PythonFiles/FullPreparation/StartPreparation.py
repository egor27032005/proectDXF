from PythonFiles.FullPreparation.PreparationKTPN1 import PreparationKTPN1
from PythonFiles.FullPreparation.PreparationKTPN2 import PreparationKTPN2
from PythonFiles.FullPreparation.PreparationNKY import PreparationNKY


class StartPreparation:
    def __init__(self,data,type,msp,doc):
        self.data=data
        self.type=type
        self.msp=msp
        self.doc=doc
        # self.doc.styles.new(name="RomansStyle", dxfattribs={
        #     'font': 'Romans.shx',  # Указываем шрифт Romans
        #     'width': 1.0  # Ширина шрифта (можно настроить)
        # })
        self.distribution()
    def distribution(self):
        match self.type:
            case "КТПН1":
                pr=PreparationKTPN1(self.data,self.msp)
            case "КТПН2":
                pr=PreparationKTPN2(self.data,self.msp)
            case "НКУ":
                pr = PreparationNKY(self.data, self.msp)




