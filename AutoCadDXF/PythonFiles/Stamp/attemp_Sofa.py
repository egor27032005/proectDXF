import ezdxf
from ezdxf import units


class Stamp:
    def __init__(self, doc, msp, points):
        self.doc = doc
        self.msp = msp

        self.points = points
        self.max_y, self.min_y, self.max_x, self.min_x = self.points[0], self.points[1], self.points[2], self.points[-1]
        self.width, self.height = self.get_w_and_h()

        self.block = self.doc.blocks.new(name='Stamp')
        self.stamp_ref = self.msp.add_blockref(name='Stamp', insert=(((self.max_x - self.min_x) + self.width) / 2, ((self.max_y - self.min_y) + self.height) / 2), dxfattribs={'layer': "F_TitleBox"})

        self.create_style_text()
        self.draw_borders()
        self.table_main()
        self.table_agreed()
        self.attributes_main()
        self.attributes_agreed()
        self.add_attributes()
        self.text_main_table()

    def get_w_and_h(self):
        sizes = [(210, 297), (297, 420), (420, 297), (420, 594), (594, 841), (841, 594), (841, 1189), (1189, 841)]
        w_draft = self.max_x - self.min_x + 10
        h_draft = self.max_y - self.min_y + 65
        for size in sizes:
            if w_draft <= size[0] and h_draft <= size[1]:
                return size[0], size[1]

    def create_style_text(self):
        self.gost_style_name = "GOST_Type_A"
        if self.gost_style_name not in doc.styles:
            doc.styles.new(
                name=self.gost_style_name,
                dxfattribs={
                    "font": "GOST_A_Regular.ttf",  # Имя файла шрифта (должен быть доступен)
                    "width": 0.7,  # Коэффициент ширины (0.7 — ГОСТовский стандарт)
                }
            )

    def draw_borders(self):
        self.block.add_lwpolyline([(0, 0), (-self.width, 0), (-self.width, self.height), (0, self.height), (0, 0)],
                                  close=True, dxfattribs={"color": 2, "const_width": 0.7})
        self.block.add_lwpolyline(
            [(5, -5), (-self.width - 20, -5), (-self.width - 20, self.height + 5), (5, self.height + 5), (5, -5)],
            close=True, dxfattribs={"color": 4})

    def table_main(self):
        # yellow lines
        self.block.add_lwpolyline([(-185, 0), (-185, 55), (0, 55)], close=False,
                                  dxfattribs={"color": 2, "const_width": 0.7})
        self.block.add_lwpolyline([(-120, 0), (-120, 55)], close=False, dxfattribs={"color": 2, "const_width": 0.7})
        self.block.add_lwpolyline([(-120, 15), (0, 15)], close=False, dxfattribs={"color": 2, "const_width": 0.7})
        self.block.add_lwpolyline([(-120, 30), (0, 30)], close=False, dxfattribs={"color": 2, "const_width": 0.7})
        self.block.add_lwpolyline([(-120, 45), (0, 45)], close=False, dxfattribs={"color": 2, "const_width": 0.7})
        self.block.add_lwpolyline([(-50, 0), (-50, 30)], close=False, dxfattribs={"color": 2, "const_width": 0.7})

        # blue_lines
        self.block.add_lwpolyline([(-175, 30), (-175, 55)], close=False, dxfattribs={"color": 4})
        self.block.add_lwpolyline([(-165, 0), (-165, 55)], close=False, dxfattribs={"color": 4, "const_width": 0.7})
        self.block.add_lwpolyline([(-155, 30), (-155, 55)], close=False, dxfattribs={"color": 4})
        self.block.add_lwpolyline([(-145, 0), (-145, 55)], close=False, dxfattribs={"color": 4, "const_width": 0.7})
        self.block.add_lwpolyline([(-130, 0), (-130, 55)], close=False, dxfattribs={"color": 4, "const_width": 0.7})
        self.block.add_lwpolyline([(-175, 30), (-175, 35)], close=False, dxfattribs={"color": 4, "const_width": 0.7})
        self.block.add_lwpolyline([(-155, 30), (-155, 35)], close=False, dxfattribs={"color": 4, "const_width": 0.7})

        for i in range(1, 11):
            if i == 6 or i == 7:
                self.block.add_lwpolyline([(-185, i * 5), (-120, i * 5)], close=False,
                                          dxfattribs={"color": 4, "const_width": 0.7})
            else:
                self.block.add_lwpolyline([(-185, i * 5), (-120, i * 5)], close=False, dxfattribs={"color": 4})

        self.block.add_lwpolyline([(-50, 25), (0, 25)], close=False, dxfattribs={"color": 4, "const_width": 0.7})
        self.block.add_lwpolyline([(-36, 15), (-36, 30)], close=False, dxfattribs={"color": 4, "const_width": 0.7})
        self.block.add_lwpolyline([(-21, 15), (-21, 30)], close=False, dxfattribs={"color": 4, "const_width": 0.7})

    def table_agreed(self):
        self.block.add_lwpolyline([(-self.width, 0), (-self.width - 12, 0), (-self.width - 12, 85)], close=False,
                                  dxfattribs={"color": 4})
        self.block.add_lwpolyline([(-self.width - 7, 0), (-self.width - 7, 85)], close=False, dxfattribs={"color": 4})
        self.block.add_lwpolyline([(-self.width - 12, 25), (-self.width, 25)], close=False, dxfattribs={"color": 4})
        self.block.add_lwpolyline([(-self.width - 12, 60), (-self.width, 60)], close=False, dxfattribs={"color": 4})
        self.block.add_lwpolyline([(-self.width - 20, 85), (-self.width, 85)], close=False, dxfattribs={"color": 4})

        self.block.add_mtext("Инв.N подл.", dxfattribs={"char_height": 3.0, "color": 4, "attachment_point": 5, "style": self.gost_style_name, 'rotation': 90}).set_location((-self.width - 9.5, 12.5))
        self.block.add_mtext("Подпись и дата", dxfattribs={"char_height": 3.0, "color": 4, "attachment_point": 5, "style": self.gost_style_name, 'rotation': 90}).set_location((-self.width - 9.5, 42.5))
        self.block.add_mtext("Взамен инв.N", dxfattribs={"char_height": 3.0, "color": 4, "attachment_point": 5, "style": self.gost_style_name, 'rotation': 90}).set_location((-self.width - 9.5, 72.5))

        for i in range(1, 4):
            self.block.add_line((-self.width - i * 5, 85), (-self.width - i * 5, 280), dxfattribs={"color": 4})
        heights = [105, 125, 140, 150, 170, 190, 205, 215, 235, 255, 270, 280]
        for height in heights:
            if height in [105, 125, 140]:
                self.block.add_line((-self.width - 15, height), (-self.width, height), dxfattribs={"color": 4})
            else:
                self.block.add_line((-self.width - 20, height), (-self.width, height), dxfattribs={"color": 4})

        self.block.add_mtext("Согласовано", dxfattribs={"char_height": 3.0, "color": 4, "attachment_point": 4, "style": self.gost_style_name, 'rotation': 90}).set_location((-self.width - 17.5, 86.5))

    def attributes_agreed(self):
        self.block.add_attdef(tag="МАРКА1", insert=(-self.width - 12.5, 86.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })
        self.block.add_attdef(tag="ФАМИЛИЯ1", insert=(-self.width - 12.5, 106.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })

        self.block.add_attdef(tag="МАРКА2", insert=(-self.width - 7.5, 86.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })
        self.block.add_attdef(tag="ФАМИЛИЯ2", insert=(-self.width - 7.5, 106.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })

        self.block.add_attdef(tag="МАРКА3", insert=(-self.width - 2.5, 86.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })
        self.block.add_attdef(tag="ФАМИЛИЯ3", insert=(-self.width - 2.5, 106.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })

        self.block.add_attdef(tag="МАРКА4", insert=(-self.width - 17.5, 151.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })
        self.block.add_attdef(tag="ФАМИЛИЯ4", insert=(-self.width - 17.5, 171.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })

        self.block.add_attdef(tag="МАРКА5", insert=(-self.width - 12.5, 151.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })
        self.block.add_attdef(tag="ФАМИЛИЯ5", insert=(-self.width - 12.5, 171.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })

        self.block.add_attdef(tag="МАРКА6", insert=(-self.width - 7.5, 151.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })
        self.block.add_attdef(tag="ФАМИЛИЯ6", insert=(-self.width - 7.5, 171.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })

        self.block.add_attdef(tag="МАРКА7", insert=(-self.width - 2.5, 151.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })
        self.block.add_attdef(tag="ФАМИЛИЯ7", insert=(-self.width - 2.5, 171.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })

        self.block.add_attdef(tag="МАРКА8", insert=(-self.width - 17.5, 216.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })
        self.block.add_attdef(tag="ФАМИЛИЯ8", insert=(-self.width - 17.5, 236.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })

        self.block.add_attdef(tag="МАРКА9", insert=(-self.width - 12.5, 216.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })
        self.block.add_attdef(tag="ФАМИЛИЯ9", insert=(-self.width - 12.5, 236.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })

        self.block.add_attdef(tag="МАРКА10", insert=(-self.width - 7.5, 216.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })
        self.block.add_attdef(tag="ФАМИЛИЯ10", insert=(-self.width - 7.5, 236.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })

        self.block.add_attdef(tag="МАРКА11", insert=(-self.width - 2.5, 216.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })
        self.block.add_attdef(tag="ФАМИЛИЯ11", insert=(-self.width - 2.5, 236.5), dxfattribs={"color": 1, "height": 2.5, "style": self.gost_style_name, "halign": 0, "valign": 2, "width": 0.7,"rotation": 90, })

    def attributes_main(self):
        self.block.add_attdef(tag="НАЗВАНИЕ_ЧЕРТЕЖА", insert=(-60, 46), dxfattribs={"color": 1, "height": 5.0, "width": 0.7, "style": self.gost_style_name, "halign": 1, "valign": 1})

        self.block.add_attdef(tag="НАЗВАНИЕ_ПРОЕКТА_СТРОКА1", insert=(-60, 40.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 1, "valign": 1})
        self.block.add_attdef(tag="НАЗВАНИЕ_ПРОЕКТА_СТРОКА2", insert=(-60, 35.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 1, "valign": 1})
        self.block.add_attdef(tag="НАЗВАНИЕ_ПРОЕКТА_СТРОКА3", insert=(-60, 30.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 1, "valign": 1})

        self.block.add_attdef(tag="НАЗВАНИЕ_ОБЪЕКТА_СТРОКА1", insert=(-85, 25.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 1, "valign": 1})
        self.block.add_attdef(tag="НАЗВАНИЕ_ОБЪЕКТА_СТРОКА2", insert=(-85, 20.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 1, "valign": 1})
        self.block.add_attdef(tag="НАЗВАНИЕ_ОБЪЕКТА_СТРОКА3", insert=(-85, 15.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 1, "valign": 1})

        self.block.add_attdef(tag="НАЗВАНИЕ_ЧЕРТЕЖА_СТРОКА1", insert=(-85, 10.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 1, "valign": 1})
        self.block.add_attdef(tag="НАЗВАНИЕ_ЧЕРТЕЖА_СТРОКА2", insert=(-85, 5.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 1, "valign": 1})
        self.block.add_attdef(tag="НАЗВАНИЕ_ЧЕРТЕЖА_СТРОКА3", insert=(-85, 0.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 1, "valign": 1})

        self.block.add_attdef(tag="РАЗРАБОТАЛ", insert=(-163.5, 27.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 0, "valign": 2})
        self.block.add_attdef(tag="ПРОВЕРИЛ", insert=(-163.5, 22.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 0, "valign": 2})
        self.block.add_attdef(tag="НАЧ.ОТДЕЛА", insert=(-163.5, 17.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 0, "valign": 2})
        self.block.add_attdef(tag="ТЕХКОНТРОЛЬ", insert=(-163.5, 12.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 0, "valign": 2})
        self.block.add_attdef(tag="Н.КОНТРОЛЬ", insert=(-163.5, 7.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 0, "valign": 2})
        self.block.add_attdef(tag="ГИП", insert=(-163.5, 2.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 0, "valign": 2})

        self.block.add_attdef(tag="СТАДИЯ", insert=(-43, 17.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 1, "valign": 1})
        self.block.add_attdef(tag="ЛИСТ", insert=(-28.5, 17.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 1, "valign": 1})
        self.block.add_attdef(tag="ЛИСТОВ", insert=(-10.5, 17.5), dxfattribs={"color": 1, "height": 2.5, "width": 0.7, "style": self.gost_style_name, "halign": 1, "valign": 1})

    def add_attributes(self):
        self.stamp_ref.add_auto_attribs({
            "НАЗВАНИЕ_ЧЕРТЕЖА": "612-00-ИОС7.1",
            "НАЗВАНИЕ_ПРОЕКТА_СТРОКА1": "Склад горюче-смазочных материалов(топливозаправочный комплекс)",
            "НАЗВАНИЕ_ПРОЕКТА_СТРОКА2": "\"Левашово\"",
            "НАЗВАНИЕ_ПРОЕКТА_СТРОКА3": "",
            "НАЗВАНИЕ_ОБЪЕКТА_СТРОКА1": "",
            "НАЗВАНИЕ_ОБЪЕКТА_СТРОКА2": "",
            "НАЗВАНИЕ_ОБЪЕКТА_СТРОКА3": "",
            "НАЗВАНИЕ_ЧЕРТЕЖА_СТРОКА1": "НАЗВАНИЕ_ЧЕРТЕЖА_СТРОКА1",
            "НАЗВАНИЕ_ЧЕРТЕЖА_СТРОКА2": "НАЗВАНИЕ_ЧЕРТЕЖА_СТРОКА2",
            "НАЗВАНИЕ_ЧЕРТЕЖА_СТРОКА3": "НАЗВАНИЕ_ЧЕРТЕЖА_СТРОКА3",
            "РАЗРАБОТАЛ": "Фамилия",
            "ПРОВЕРИЛ": "Фамилия",
            "НАЧ.ОТДЕЛА": "Фамилия",
            "ТЕХКОНТРОЛЬ": "Фамилия",
            "Н.КОНТРОЛЬ": "Фамилия",
            "ГИП": "Фамилия",
            "СТАДИЯ": "П",
            "ЛИСТ": 1,
            "ЛИСТОВ": "X",
            "МАРКА1": "",
            "ФАМИЛИЯ1": "",
            "МАРКА2": "",
            "ФАМИЛИЯ2": "",
            "МАРКА3": "",
            "ФАМИЛИЯ3": "",
            "МАРКА4": "",
            "ФАМИЛИЯ4": "",
            "МАРКА5": "",
            "ФАМИЛИЯ5": "",
            "МАРКА6": "",
            "ФАМИЛИЯ6": "",
            "МАРКА7": "",
            "ФАМИЛИЯ7": "",
            "МАРКА8": "",
            "ФАМИЛИЯ8": "",
            "МАРКА9": "",
            "ФАМИЛИЯ9": "",
            "МАРКА10": "",
            "ФАМИЛИЯ10": "",
            "МАРКА11": "",
            "ФАМИЛИЯ11": "",
        })

    def text_main_table(self):
        self.block.add_mtext("Изм.", dxfattribs={"char_height": 2.5, "color": 1, "attachment_point": 2, "style": self.gost_style_name}).set_location((-180, 33.65))
        self.block.add_mtext("Кол.уч.", dxfattribs={"char_height": 2.5, "color": 1, "attachment_point": 2, "style": self.gost_style_name}).set_location((-170, 33.65))
        self.block.add_mtext("Лист", dxfattribs={"char_height": 2.5, "color": 1, "attachment_point": 2, "style": self.gost_style_name}).set_location((-160, 33.65))
        self.block.add_mtext("N док.", dxfattribs={"char_height": 2.5, "color": 1, "attachment_point": 2, "style": self.gost_style_name}).set_location((-150, 33.65))
        self.block.add_mtext("Подпись", dxfattribs={"char_height": 2.5, "color": 1, "attachment_point": 2, "style": self.gost_style_name}).set_location((-137.5, 33.65))
        self.block.add_mtext("Дата", dxfattribs={"char_height": 2.5, "color": 1, "attachment_point": 2, "style": self.gost_style_name}).set_location((-125, 33.65))

        self.block.add_mtext("Разработал", dxfattribs={"char_height": 2.5, "color": 1, "attachment_point": 1, "style": self.gost_style_name}).set_location((-183.5, 28.65))
        self.block.add_mtext("Проверил", dxfattribs={"char_height": 2.5, "color": 1, "attachment_point": 1, "style": self.gost_style_name}).set_location((-183.5, 23.65))
        self.block.add_mtext("Нач.отдела", dxfattribs={"char_height": 2.5, "color": 1, "attachment_point": 1, "style": self.gost_style_name}).set_location((-183.5, 18.65))
        self.block.add_mtext("Техконтроль", dxfattribs={"char_height": 2.5, "color": 1, "attachment_point": 1, "style": self.gost_style_name}).set_location((-183.5, 13.65))
        self.block.add_mtext("Н.контроль", dxfattribs={"char_height": 2.5, "color": 1, "attachment_point": 1, "style": self.gost_style_name}).set_location((-183.5, 8.65))
        self.block.add_mtext("ГИП", dxfattribs={"char_height": 2.5, "color": 1, "attachment_point": 1, "style": self.gost_style_name}).set_location((-183.5, 3.65))

        self.block.add_mtext("Стадия", dxfattribs={"char_height": 2.5, "color": 1, "attachment_point": 2, "style": self.gost_style_name}).set_location((-42, 28.65))
        self.block.add_mtext("Лист", dxfattribs={"char_height": 2.5, "color": 1, "attachment_point": 2, "style": self.gost_style_name}).set_location((-28.5, 28.65))
        self.block.add_mtext("Листов", dxfattribs={"char_height": 2.5, "color": 1, "attachment_point": 2, "style": self.gost_style_name}).set_location((-10.5, 28.65))

        for i in range(6):
            self.msp.add_mtext("xx.xx.25",
                           dxfattribs={"char_height": 2, "color": 7, "attachment_point": 5,
                                       "style": self.gost_style_name}).set_location((((self.max_x - self.min_x) + self.width) / 2 - 125, ((self.max_y - self.min_y) + self.height) / 2 + (i * 5 + 2.5)))

if __name__ == "__main__":
    doc = ezdxf.new('R2010', setup=True)
    doc.units = ezdxf.units.MM
    msp = doc.modelspace()
    e = Stamp(doc, msp, [150, -100, 150, -100])
    doc.saveas("11.dxf")
    print("Файл fixed_blocks.dxf успешно создан")
# create_block_with_attributes()
