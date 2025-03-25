import itertools

from PythonFiles.Development.Consumer.Consumer import Consumer
from PythonFiles.Development.NKY.Automat220 import Automat220
from PythonFiles.Development.NKY.Automat380 import Automat380
from PythonFiles.Development.NKY.AutomatMagnet import AutomatMagnet
from PythonFiles.Development.NKY.DivAutomat import DivAutomat


class AutomatsNKY:
    def __init__(self,msp,doc,countAutomat1,countAutomat2,x,y,automat_consumers,part_list):
        self.msp=msp
        self.doc=doc
        self.part_list=part_list
        self.countAutomat1=countAutomat1
        self.countAutomat2=countAutomat2
        self.x=x
        self.y=y
        self.automat_consumers=automat_consumers
        self.y2=self.y-158
        self.updateTable = [2 for _ in range(11)]
        self.double_consumers=["сх. у наружным освещением","сх. у э. двиг. с кнопочным постом и каробкой зажимов","сх. у э. двиг. с кнопочным постом"]

        self.first_colum=['Номер линии','Установленная мощность, кВт','Расчетная мощность, кВт','Расчетный ток,'
        ' А','Расчетная мощность в аварийном режиме, кВт','Расчетный ток в аварийном режиме, А',"'Потеря напряжения до РУ/ЭП, %'",'Iкз 1ф в конце линии, А',
                "Наименование, назначение\n","Место установки, номер по генплану",'Этап строительства']
        self.pointsX()
        self.test_preparation()
        self.put_lines()
    def pointsX(self):
        self.autPointsX=[self.x]
        self.columPointsX=[self.x-12]
        for i,colum in enumerate(self.automat_consumers):
            if colum[1][-1] in self.double_consumers or colum[1][0]=="обычный  с магнитным пускателем":
                elem=self.autPointsX[-1]+60
                self.autPointsX.append(elem)
                self.columPointsX.extend([self.columPointsX[-1]+30,self.columPointsX[-1]+60])
                continue
            else:
                elem = self.autPointsX[-1] + 30
                self.autPointsX.append(elem)
                self.columPointsX.append(self.columPointsX[-1]+30)
        self.autPointsX = [num + 60 if idx > self.countAutomat1-1 else num for idx, num in enumerate(self.autPointsX)]
        self.pointPartitionX = self.autPointsX[self.countAutomat1 ] - 55
        self.columPointsX = [num + 60 if num>self.pointPartitionX else num for idx, num in enumerate(self.columPointsX)]
        self.columPointsX.append(self.pointPartitionX+43)
    def printAutomats(self):
        for i,colum in enumerate(self.automat_consumers):
            automat=colum[1][0]
            consumer=colum[1][-1]
            match automat:
                case "обычный":
                    aut=Automat220(self.msp,self.doc,self.autPointsX[i],self.y,False,consumer=consumer,cabelName=colum[1][1],text=colum[0])
                    # cons = Consumer(self.msp,self.doc, consumer,self.autPointsX[i]+4.35,self.y-139.83)
                case "обычный 220":
                    aut = Automat220(self.msp,self.doc,self.autPointsX[i],self.y,False,consumer=consumer,cabelName=colum[1][1],text=colum[0])
                    # cons = Consumer(self.msp,self.doc, consumer, self.autPointsX[i] + 4.35, self.y -139.83)
                case "обычный 380":
                    aut = Automat380(self.msp,self.doc,self.autPointsX[i],self.y,False,consumer=consumer,cabelName=colum[1][1],text=colum[0])
                    # cons = Consumer(self.msp,self.doc, consumer, self.autPointsX[i] + 4.35, self.y -139.83)
                case "диф автомат":
                    aut=DivAutomat(self.msp,self.doc,self.autPointsX[i],self.y,False,consumer=consumer,cabelName=colum[1][1],text=colum[0])
                    # cons = Consumer(self.msp,self.doc, consumer, self.autPointsX[i] + 4.35, self.y -139.83)
                case "обычный  с магнитным пускателем":
                    aut=AutomatMagnet(self.msp,self.doc,self.autPointsX[i],self.y,False,consumer=consumer,cabelName=colum[1][1],text=colum[0])
                    # cons = Consumer(self.msp,self.doc, consumer, self.autPointsX[i] + 4.35, self.y - 76.02)
                case "резерв":
                    aut = Automat220(self.msp, self.doc,self.autPointsX[i], self.y, True,consumer=consumer,text=colum[0])
                case "обычный 220 резерв":
                    aut = Automat220(self.msp, self.doc,self.autPointsX[i], self.y, True,consumer=consumer,text=colum[0])
                case "обычный 380 резерв":
                    aut = Automat380(self.msp,self.doc, self.autPointsX[i], self.y, True,consumer=consumer,text=colum[0])
                case "диф автомат резерв":
                    aut = DivAutomat(self.msp,self.doc, self.autPointsX[i], self.y, True,consumer=consumer,text=colum[0])
    def test_preparation(self):
        count_main = []
        for i in self.part_list:
            i=self.split_string_by_cell_length(i,34)
            count_main.append(i.count("\n"))
        array=[count_main]
        for colum in self.automat_consumers:
            count_main=[]
            count_two=[]
            for i,text in enumerate(colum[2]):
                colum[2][i]=self.split_string_by_cell_length(text)
                count_main.append(colum[2][i].count("\n"))
            if len(colum)!=3:
                for i, text in enumerate(colum[-1]):
                    colum[-1][i] = self.split_string_by_cell_length(text)
                    count_two.append(colum[-1][i].count("\n"))
                array.append(count_two)
        array.append(count_main)
        len_rows=[(max(elements)+1)*8 for elements in zip(*array)]
        len_rows.insert(0,0)
        self.pointsY=[self.y2-i for i in itertools.accumulate(len_rows)]
        self.texting()
        self.put_column(self.first_colum,self.x-90)
        self.put_column(self.part_list,self.pointPartitionX-15)






    def texting(self):
        for x,colum in enumerate(self.automat_consumers):
            if len(colum)==3:
                self.put_column(colum[-1],self.autPointsX[x]-12)
            else:
                self.put_double_column(colum[2],colum[-1],self.autPointsX[x]-12)
    def split_string_by_cell_length(self, input_string, cell_length=17):
        words = input_string.split()  # Разделяем строку на слова по пробелам
        result = []  # Итоговый список строк
        current_line = ""  # Текущая строка
        for word in words:
            if len(current_line) + len(word) + (1 if current_line else 0) <= cell_length:
                if current_line:
                    current_line += " " + word
                else:
                    current_line = word
            else:
                result.append(current_line)
                current_line = word
        if current_line:
            result.append(current_line)
        result="\n".join(result)
        return result
    def put_column(self,colum,x):
        for y,col in enumerate(colum):
            self.put_text(col,x,self.pointsY[y])
        # self.msp.add_line((x,self.y2), (x,self.pointsY[-1]), dxfattribs={'color': 3})
    def put_double_column(self,colum1,colum2,x):
        for y,col in enumerate(colum1):
            self.put_text(col,x,self.pointsY[y])
            self.put_text(colum2[y],x+30,self.pointsY[y])
        # self.msp.add_line((x,self.y2), (x,self.pointsY[-1]), dxfattribs={'color': 3})
        # self.msp.add_line((x+30,self.y2), (x+30,self.pointsY[-1]), dxfattribs={'color': 3})

    def put_text(self, line, x, y):
        x0 = 3
        y0 = -2
        insertion_point_text = (x + x0, y + y0)
        self.msp.add_mtext(line, dxfattribs={
            'insert': insertion_point_text,
            'char_height': 2.5,
            'color': 1,
            'style': 'ROMANS',
            'attachment_point': 1  # Аналог AttachmentPoint в pyautocad
        })
    def put_lines(self):
        # points_x = [self.autPointsX[0] + i * 30 for i in range(30)]
        for y in self.pointsY:
            point1 = (self.autPointsX[0]-90, y)
            point2 = (self.autPointsX[-1]-12, y)
            self.msp.add_line(point1, point2, dxfattribs={'color': 3})

        for x in self.columPointsX:
            point1 = (x, self.pointsY[0])
            point2 = (x, self.pointsY[-1])
            self.msp.add_line(point1, point2, dxfattribs={'color': 3})
        self.msp.add_line((self.autPointsX[0]-90,self.pointsY[0]), (self.autPointsX[0]-90,self.pointsY[-1]), dxfattribs={'color': 3})