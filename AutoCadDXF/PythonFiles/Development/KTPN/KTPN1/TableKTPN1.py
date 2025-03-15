import itertools
import ezdxf

from PythonFiles.Development.KTPN.FirstPartTable import FirstPartTable


class TableKTPN1:
    def __init__(self, msp ,startX, startY, countAutomat, textList):
        self.startX = startX
        self.startY = startY
        self.textList = textList
        self.countAutomat = countAutomat
        self.msp = msp

        # Создаем текстовый стиль с шрифтом Romans


        self.coordText = [self.startY - i - 20 for i in [0, 28.32, 56.8, 74, 115, 132.48, 154.86, 253.95, 261.51, 269.71]]
        self.length = 60
        self.startSecondPartY = self.startY - 253.95
        self.startSecondPartY2 = self.startY - 269.71
        self.lengthOfRow = list(itertools.chain([22, 19, 16], [13 for _ in range(self.countAutomat + 1)]))
        self.updateTable = [2 for _ in range(9)]
        self.second_part_first()
        self.text_create()
        self.cap()
        self.start_table1 = FirstPartTable(self.msp,self.startX - 22, self.startY)

    def cap(self):
        for i in [0, 7.56, 15.76]:
            point1 = (self.startX, self.startSecondPartY - i)
            point2 = (self.startX + 194 + 35 * self.countAutomat, self.startSecondPartY - i)
            self.msp.add_line(point1, point2, dxfattribs={'color': 2})

        point1 = (self.startX + 194 + 35 * self.countAutomat, self.startSecondPartY)
        point2 = (self.startX + 194 + 35 * self.countAutomat, self.startSecondPartY - 23.05)
        self.msp.add_line(point1, point2, dxfattribs={'color': 2})

        cap1 = [["КСО"], ["ШВ"], ["Шкафы линий"]]
        points = [self.pointsX[1] + 8, self.pointsX[2], self.pointsX[3] + 35 * self.countAutomat // 2]
        for i in range(len(cap1)):
            self.put_text(cap1[i], points[i], self.pointsY[0] + 8)

    def second_part_first(self):
        self.pointsX = [self.startX + i - 22 for i in itertools.accumulate(itertools.chain([0, 90, 47, 44], list(itertools.repeat(35, self.countAutomat + 1))))]
        self.pointsY = [self.startSecondPartY2 - i * 12 for i in range(12)]

    def text_create(self):
        for y, line in enumerate(self.textList):
            for x, el in enumerate(line):
                if el.count("\n") == 0 and len(el) <= self.lengthOfRow[x]:
                    self.put_text([el], self.pointsX[x], self.pointsY[y])

                if el.count("\n") == 0 and len(el) > self.lengthOfRow[x]:
                    a = self.split_string_by_cell_length(el, self.lengthOfRow[x])
                    tr = len(a)
                    if tr > self.updateTable[y]:
                        self.update_table(y, tr - self.updateTable[y])
                        self.put_text(a, self.pointsX[x], self.pointsY[y])
                    else:
                        self.put_text(a, self.pointsX[x], self.pointsY[y])

                if el.count("\n") != 0:
                    a = [self.split_string_by_cell_length(f, self.lengthOfRow[x]) for f in el.split("\n")]
                    a = sum(a, [])
                    tr = len(a)
                    if tr > self.updateTable[y]:
                        self.update_table(y, tr - self.updateTable[y])
                        self.put_text(a, self.pointsX[x], self.pointsY[y])
                    else:
                        self.put_text(a, self.pointsX[x], self.pointsY[y])

        self.put_lines()

    def put_lines(self):
        for y in self.pointsY[:-1]:
            point1 = (self.pointsX[0], y)
            point2 = (self.pointsX[-1], y)
            self.msp.add_line(point1, point2, dxfattribs={'color': 2})

        for i, x in enumerate(self.pointsX):
            t = 0
            if i < 5:
                t = 18.05 - 2.29
            point1 = (x, self.pointsY[0] + t)
            point2 = (x, self.pointsY[-2])
            self.msp.add_line(point1, point2, dxfattribs={'color': 2})

    def put_text(self, line, x, y):
        x0 = 3
        y0 = -2
        if y == self.pointsY[0]:
            x0 = 16
            y0 = -5

        mtext_content = "\n".join(line)
        insertion_point_text = (x + x0+15, y + y0)
        self.msp.add_mtext(mtext_content, dxfattribs={
            'insert': insertion_point_text,
            'char_height': 2.5,
            'color': 1,
            'style': 'RomansStyle',
            'attachment_point': 2  # Аналог AttachmentPoint в pyautocad
        })

    def update_table(self, index, number):
        for i in range(index, len(self.pointsY) - 1):
            self.pointsY[i + 1] -= number * 5
        self.updateTable[index] += number

    def split_string_by_cell_length(self, input_string, cell_length):
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
        return result


if __name__ == '__main__':
    text_list = [
        ['Установленная мощность', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст'],
        ['Установленная мощность, кВm', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст'],
        ['Расчетная мощность, кВm', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', '123\nFSD\nпрограмма ghjuhfvvf l;asfka dfa', '123\nFSD\nпрограмма', '123\nFSD\nпрограмма', '123\nFSD\nпрограмма', '123\nFSD\nпрограмма'],
        ['Расчетный ток , А', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст'],
        ['Расчетная мощность в аварийном режиме, кBm', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст'],
        ['Расчетный ток в аварийном режиме, A', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст'],
        ['Потеря напряжения до РУ/ЭП, %', 'текст\ngdsggsd\nadsfd\nffasddf\nggdsdfg\nsfasdfa', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текстsafasdf'],
        ['Название линии', 'текст', 'текст', 'текст', 'текст', 'текст l;fas falskm l;adsk ;asldkf ;lasdkk', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст'],
        ['Место установки', 'текст', 'текст', 'текст', 'текст df jfdsa sa sdff fiaj sadfas dfasdf sdfasdf afa ', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст', 'текст']
    ]
    dxf=ezdxf.new('R2010')
    t = Table(dxf, 1000, 0, 10, text_list)