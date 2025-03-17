from PythonFiles.Development.NKY.NKY import NKY


class PreparationNKY:
    def __init__(self,data,msp):
        self.data=data
        self.msp=msp
        self.automat_consumers=self.find_and_combine_elements(data)
        self.count_automat=len(self.automat_consumers[0])
        self.nky=NKY(self.msp,self.count_automat,self.automat_consumers)

    def find_and_combine_elements(self,data):
        tip_automat = next((item[2:] for item in data if item[0] == "ТИП автомата"), None)
        vid_kabelya = next((item[2:] for item in data if item[0] == "Вид кабеля"), None)
        potrebiteli = next((item[2:] for item in data if item[0] == "Потребители"), None)
        result = []
        if tip_automat:
            result.append(tip_automat)
        if vid_kabelya:
            result.append(vid_kabelya)
        if potrebiteli:
            result.append(potrebiteli)
        return result