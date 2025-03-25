class FirstPartTableNKY:
    def __init__(self,msp,x,y):
        self.msp=msp
        self.x=x
        self.y=y
        self.coordText = [self.y - i for i in [0, 32, 76, 100, 152, 175]]
        self.length=78
        self.firstPart = [
            ["Сборные шины", "Напряжение кВ", "Частота, Гц", "Ожидаемый ток трехфазного короткого", "замыкания на шинах НКУ/ток","электродинамической стойкости"],
            ["Защитный аппарат:", "Количество фаз", "Номинальный ток In, А", "Уставка теплового расцепителя Ir, А", "Уставка токовой отсечки Isd, А /","Характеристика автомата (B, C, D)"],
            ["Контактор:","Номинальный ток, А","Ток расцепителя, А"],
            ["Маркировка-марка-сечение, мм2/ -длина, м", "труба, длинна, м"],
            ["Условное графическое изображение, ","обозначение"],
            [""]

        ]
        self.create_first_part()

    def create_first_part(self):
        for i, line in enumerate(self.firstPart):
            mtext_content = "\n".join(line)
            insertion_point_text = (self.x + 3, self.coordText[i] - 3)
            insertion_point = (self.x, self.coordText[i])
            second_point = (self.x + self.length, self.coordText[i])
            self.msp.add_line(insertion_point, second_point, dxfattribs={'color': 3})
            insertion_point_text = (self.x + 3, self.coordText[i] - 3)
            self.msp.add_mtext(mtext_content, dxfattribs={
                'insert': insertion_point_text,
                'char_height': 2.5,
                'color': 1,
                'style': 'ROMANS',  # Применяем стиль Romans
                'attachment_point': 1,
                'line_spacing_factor': 1.1# Аналог AttachmentPoint в pyautocad
            })

        # Добавляем вертикальные линии
        point3 = (self.x, self.y)
        point4 = (self.x, self.y-191.41)
        self.msp.add_line(point3, point4, dxfattribs={'color': 3})

        point5 = (self.x + self.length, self.y)
        point6 = (self.x + self.length, self.y-191.41)
        self.msp.add_line(point5, point6, dxfattribs={'color': 3})
