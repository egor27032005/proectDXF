from re import findall

from PythonFiles.Development.FlowChart.FlowChar import FlowChar


class PreparationFlowChar:
    def __init__(self, data, msp, doc):
        self.data = data[1:]
        self.msp = msp
        self.doc = doc
        self.count_borehole_oil_industry = 5
        self.count_water_intake_well = 3
        self.name = "27"
        self.funk()
        self.flowChar = FlowChar(self.doc, self.msp, self.name, self.count_borehole_oil_industry,
                                 self.count_water_intake_well)

    def funk(self):
        self.objects = {}  # словарь для всех объектов со всеми параметрами
        curr_object = ""  # какой объект заполняется сейчас

        for line in self.data:
            print(line)
            if type(line[0]) == str and line[0] not in self.objects:  # если в столбце А начался новый объект то
                curr_object = line[0]  # меняем текущий объект заполнения
                self.objects[curr_object] = {}  # словарь для информации по этому конкретному объекту
                for n in range(int(line[1])):
                    self.objects[curr_object][line[2].replace("№", str(n + 1))] = {}  # создаем необходимое количество словарей для отдельных объектов этого типа
            else:
                if line[2] == "Параметр":  # игнорируем заполнение "шапки" одного объекта
                    continue
                else:
                    for cell in range(2, len(line), 3):
                        notation = list(self.objects[curr_object].keys())[0]  # находим обозначение текущего объекта
                        number = findall(r"(?<!\w)-?\d+", notation)[-1]  # меняем его номер в зависимости от столбца
                        real_number = (cell - 2) // 3 + 1  # ищем номер объекта в соответствии со структурой
                        curr_obj = notation.replace(number, str(real_number))  # создаем обозначение текущего объекта

                        setting, value, unit = line[cell], line[cell + 1], line[cell + 2]

                        if type(setting) == type(value) == type(
                                unit) != str:  # проверка на пустые строки (возникают из-за разного количества объектов каждого типа
                            continue
                        self.objects[curr_object][curr_obj][
                            setting] = f"{str(value)} {str(unit)}"  # заполняем данные параметр: "значение + ед.измерения"

        print(self.objects)
