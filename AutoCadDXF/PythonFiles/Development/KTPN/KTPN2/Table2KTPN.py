import itertools
import ezdxf
from ezdxf import units

from PythonFiles.Development.KTPN.FirstPartTable import FirstPartTable


class Table2KTN:
    def __init__(self, msp, startX, start_second_partX, startY, countAutomat1, countAutomat2, textList):
        self.msp = msp
        self.startX = startX
        self.start_second_partX = start_second_partX
        self.startY = startY
        self.countAutomat1 = countAutomat1
        self.countAutomat2 = countAutomat2
        self.textList = textList
        self.start_table1 = FirstPartTable(self.msp, self.startX, self.startY)
        self.start_table2 = FirstPartTable(self.msp, self.start_second_partX, self.startY)
        self.coordText = [self.startY - i - 20 for i in [0, 28.32, 56.8, 74, 115, 132.48, 154.86, 253.95, 261.51, 269.71]]
        self.startSecondPartY = self.startY - 253.95
        self.startSecondPartY2 = self.startY - 269.71
        self.updateTable = [2 for _ in range(9)]
        self.lengthOfRow = list(itertools.chain([22, 19, 16], [13 for _ in range(self.countAutomat1 + 1)], [30], [13 for _ in range(self.countAutomat2 + 1)], [16, 19, 27,90]))
        self.second_part_first()
        self.cap()
        self.text_create()

    def second_part_first(self):
        self.pointsX = [self.startX + i for i in itertools.accumulate(itertools.chain([0, 70, 47, 44], list(itertools.repeat(35, self.countAutomat1 + 1)), [54.72], list(itertools.repeat(35, self.countAutomat2 + 1)), [44, 47, 90]))]
        self.pointsY = [self.startSecondPartY2 - i * 12 for i in range(12)]

    def cap(self):
        for i in [0, 7.56, 15.76]:
            point1 = (self.startX, self.startSecondPartY - i)
            point2 = (self.startX + 186.74 * 2 + 24 + 35 * (self.countAutomat1 + self.countAutomat2), self.startSecondPartY - i)
            self.msp.add_line(point1, point2, dxfattribs={'color': 2})

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
            if i < 5 or i == self.countAutomat1 + 5 or i == self.countAutomat1 + 4 or i > (self.countAutomat2 + self.countAutomat1 + 4):
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
        insertion_point_text = (x + x0, y + y0)
        self.msp.add_mtext(mtext_content, dxfattribs={
            'insert': insertion_point_text,
            'char_height': 2.5,
            'color': 1,
            'style': 'ROMANS',
            'attachment_point': 1  # Аналог AttachmentPoint в pyautocad
        })

    def update_table(self, index, number):
        for i in range(index, len(self.pointsY) - 1):
            self.pointsY[i + 1] -= number * 5
        self.updateTable[index] += number

    def split_string_by_cell_length(self, input_string, cell_length):
        words = input_string.split()
        result = []
        current_line = ""
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
    doc = ezdxf.new('R2010')  # Создаем новый документ DXF
    msp = doc.modelspace()  # Получаем пространство модели
    textList = [["Sample Text 1", "Sample Text 2"], ["Another Text"]]
    table = Table2KTN(msp, 100, 200, 300, 2, 2, textList)
    doc.saveas("table_output.dxf")  # Сохраняем документ в файл