from PythonFiles.Development.KTPN.Automat import Automat


class AutomatRes(Automat):
    def __init__(self,msp, startX, startY, text:list=["A","B","E","D"]):
        super().__init__(msp, startX, startY, text)
        self.msp=msp
        self.startX=startX
        self.startY=startY
        self.text=text