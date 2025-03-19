import ezdxf

class FirstPartTable:
    def __init__(self, msp,startX, startY):
        self.startX = startX
        self.startY = startY
        self.length = 70
        self.msp = msp  # Создаем новый DXF документ


        # Создаем текстовый стиль с шрифтом Romans

        self.coordText = [self.startY - i for i in [0, 28.32, 56.8, 74, 115, 132.48, 154.86, 253.95, 261.51, 269.71]]
        self.startSecondPartY = self.startY - 253.95
        self.startSecondPartY2 = self.startY - 277
        self.firstPart = [
            ["Трансформатор", "обозначение", "тип", "мощность, кВА", "напряжение, кВ"],
            ["Сборные шины", "Напряжение кВ", "Частота, Гц Ток", "термической", "стойкости, kA"],
            ["Приборные измерения"],
            ["Защитный аппарат: ", "Тип Нормальный ток In, A", "Уставка расцепителя по току защиты",
             "от перегрузок Ir, А",
             "Уставка токовой отсечки Isd, А", "Предельная отключающая способность",
             "автоматического выключателя Icu, кА",
             "Характеристика автомата (B, C, D)"],
            ["Аппарат на вводе", " 6(10) кВ"],
            ["Трансформатор тока", "коэффицитент", "трансформации"],
            ["Марка - сечение,", "мм^2 - длина, м", "труба, длина, м", "Маркировка"],
            ["Номер шкафа"], ["Тип"], [""]
        ]
        self.create_first_part()
    def create_first_part(self):
        for i, line in enumerate(self.firstPart):
            mtext_content = "\n".join(line)
            insertion_point_text = (self.startX + 3, self.coordText[i] - 3)
            insertion_point = (self.startX, self.coordText[i])
            second_point = (self.startX + self.length, self.coordText[i])
            self.msp.add_line(insertion_point, second_point, dxfattribs={'color': 2})
            xp=0
            if line=="Номер шкафа" or "Тип":
                xp=18
            insertion_point_text = (self.startX + 3, self.coordText[i] - 3)
            self.msp.add_mtext(mtext_content, dxfattribs={
                'insert': insertion_point_text,
                'char_height': 2.5,
                'color': 1,
                'style': 'ROMANS',  # Применяем стиль Romans
                'attachment_point': 1  # Аналог AttachmentPoint в pyautocad
            })

        # Добавляем вертикальные линии
        point3 = (self.startX, self.startY)
        point4 = (self.startX, self.startSecondPartY2)
        self.msp.add_line(point3, point4, dxfattribs={'color': 2})

        point5 = (self.startX + self.length, self.startY)
        point6 = (self.startX + self.length, self.startSecondPartY2)
        self.msp.add_line(point5, point6, dxfattribs={'color': 2})

