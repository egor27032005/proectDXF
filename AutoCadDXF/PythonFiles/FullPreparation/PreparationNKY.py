from PythonFiles.Development.NKY.NKY import NKY


class PreparationNKY:
    def __init__(self,data,msp):
        self.data=data
        self.msp=msp
        self.automat_consumers=self.find_and_combine_elements(data)
        self.new_array = self.reorder_lists(self.convert_to_strings(self.data))
        self.arrAutomat = self.automat_create(self.new_array[:11])
        self.arrTable = [sublist + [sublist[0]] for sublist in self.new_array[13:]]
        for i in range(3):
            self.arrTable[0].insert(-1, "")
        # sum(self.arrTable[0],[])
        self.get_count_automat()
        self.del_nan()
        for i in self.automat_consumers:
            print(i)
        self.nky=NKY(self.msp,self.count1, self.count2,self.automat_consumers)

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
    def convert_to_strings(self, nested_list):
        ar = [[str(item) if str(item) != "nan" else "" for item in sublist] for sublist in nested_list]
        a = [self.remove_trailing_empty_strings(x) for x in ar]
        return a

    def get_count_automat(self):
        for list in self.new_array:
            if "номер линии" in [str(item).lower() for item in list]:
                ind = list.index("ШС")
                self.count1 = ind - 4
                self.count2 = len(list) - self.count1-4
                self.ar = self.pad_lists(self.arrTable, len(list) + 3)
                self.part = self.arrAutomat.pop(ind - 2)


    def remove_trailing_empty_strings(self, strings):
        strings_copy = strings.copy()
        while strings_copy and strings_copy[-1] == "":
            strings_copy.pop()
        return strings_copy
    def automat_create(self,matrix):
        trimmed_matrix = [row[2:] for row in matrix]
        transposed_matrix = list(map(list, zip(*trimmed_matrix)))
        return transposed_matrix
    def reorder_lists(self,list_of_lists):
        """
        Переупорядочивает список списков в соответствии с порядком первых элементов.
        Если порядок короче, остальные элементы остаются на своих местах.
        :param list_of_lists: Список списков.
        :param order: Список с желаемым порядком первых элементов.
        :return: Переупорядоченный список списков.
        """
        first_elements_dict = {sublist[0]: sublist for sublist in list_of_lists}
        reordered_list = []
        original_index = 0
        order=["Тринсформатор, обозн, тип, мощность  кВт, напряжение кВ","Сбоные шины, напряжение кВт, частота Гц, Ток термической стойки",
               "Приборы измерения","защитный аппарат","Аппарат на вводу 6(10) кВ",
               "Трансформатор тока коэф трансформации","ТИП автомата",
               "Вид кабеля","Потребители","Марка сечения","L"]
        for key in order:
            if key in first_elements_dict:
                reordered_list.append(first_elements_dict[key])
                # Удаляем из словаря, чтобы не добавлять повторно
                del first_elements_dict[key]
        # Добавляем оставшиеся элементы в исходном порядке
        for sublist in list_of_lists:
            if sublist[0] in first_elements_dict:
                reordered_list.append(sublist)
        return reordered_list

    def pad_lists(self,list_of_lists, target_length):
        return [inner_list + [''] * (target_length - len(inner_list)) for inner_list in list_of_lists]

    def del_nan(self):
        self.automat_consumers=[[j for j in i if str(j) != "nan"] for i in self.automat_consumers ]