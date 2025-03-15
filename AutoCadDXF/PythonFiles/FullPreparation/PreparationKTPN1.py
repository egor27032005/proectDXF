import ezdxf

from PythonFiles.Development.KTPN.KTPN1.KTPN1 import KTPN1


class PreparationKTPN1:
    def __init__(self,data,msp):
        self.msp=msp
        self.data=data
        self.new_array = self.reorder_lists(self.convert_to_strings(self.data))
        self.arrAutomat = self.automat_create(self.new_array[:11])
        self.arrTable = self.new_array[13:]
        self.countAutomat = self.processing_line_numbers()
        self.ktp = KTPN1(self.msp,self.countAutomat, self.arrAutomat, self.arrTable)

    def convert_to_strings(self, nested_list):
        ar = [[str(item) if str(item) != "nan" else "" for item in sublist] for sublist in nested_list]
        a = [self.remove_trailing_empty_strings(x) for x in ar]
        return a
    def automat_create(self,matrix):
        trimmed_matrix = [row[2:] for row in matrix]
        transposed_matrix = list(map(list, zip(*trimmed_matrix)))
        return transposed_matrix

    def processing_line_numbers(self):
        for sublist in self.data:
            if "номер линии" in [str(item).lower() for item in sublist]:
                return int([str(item).lower() for item in sublist][-1])
        return None

    def remove_trailing_empty_strings(self, strings):
        strings_copy = strings.copy()
        while strings_copy and strings_copy[-1] == "":
            strings_copy.pop()
        return strings_copy
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

if __name__ == '__main__':
    doc = ezdxf.new("R2000")
    msp = doc.modelspace()

    arr= [
    ["Тринсформатор, обозн, тип, мощность  кВт, напряжение кВ", "", "1QF", "SF", "QF1", "QF2", "QF3", "QF4", "QF5", "QF6", "QF7", "QF8"],
    ["Сбоные шины, напряжение кВт, частота Гц, Ток термической стойки", "", "текст", "текст", "3P", "3P", "3P", "3P", "3P", "3P", "3P", "3P"],
    ["Приборы измерения", "", "текст", "текст", "Icu=50 кА", "Icu=50 кА", "Icu=50 кА", "Icu=50 кА", "Icu=50 кА", "Icu=50 кА", "Icu=50 кА", "Icu=50 кА"],
    ["защитный аппарат", "", "текст", "текст", "In=100 A", "In=100 A", "In=100 A", "In=100 A", "In=100 A", "In=100 A", "In=100 A", "In=100 A"],
    ["Аппарат на вводу 6(10) кВ", "", "текст", "текст", "Ir=90 A", "Ir=90 A", "Ir=90 A", "Ir=90 A", "Ir=90 A", "Ir=90 A", "Ir=90 A", "Ir=90 A"],
    ["Трансформатор тока коэф трансформации", "", "текст", "текст", "Isd=10lr=900A", "Isd=10lr=900A", "Isd=10lr=900A", "Isd=10lr=900A", "Isd=10lr=900A", "Isd=10lr=900A", "Isd=10lr=900A", "Isd=10lr=900A"],
    ["Марка сечения", "", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст"],
    ["Номер шкафа", "", "1", "", "2", "", "", "", "", "", "", ""],
    ["Тип", "КСО", "ШВ", "", "Шкафы линий", "", "", "", "", "", "", ""],
    ["Номер линии", "", "", "", "1", "2", "3", "4", "5", "6", "7", "8"],
    ["Установленная мощность", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст"],
    ["Установленная мощность, кВm", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст"],
    ["Расчетная мощность, кВm", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст"],
    ["Расчетный ток , А", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст"],
    ["Расчетная мощность в аварийном режиме, кBm", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст"],
    ["Расчетный ток в аварийном режиме, A", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст"],
    ["Потеря напряжения до РУ/ЭП, %", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст"],
    ["Название линии", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст"],
    ["Место установки", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст", "текст"]]
    pr=PreparationKTPN1(arr,msp)
    doc.saveas("solid_hatch.dxf")