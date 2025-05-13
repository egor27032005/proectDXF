import ezdxf
import pandas as pd


class Explication:
    def __init__(self, doc, msp, x, y, layer="Tehnolog"):
        self.doc = doc
        self.msp = msp
        self.x = x
        self.y = y
        self.data = pd.read_excel("D:/work/Шаблон.xlsm", sheet_name="Примечание", engine='openpyxl',
                                  header=None).to_numpy()[1:]
        self.create_style_text()
        self.header_table()
        self.display_elems()

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

    def header_table(self):
        """title"""
        self.msp.add_mtext("Экспликация оборудования и аппаратуры",
                           dxfattribs={"char_height": 7.0, "color": 7, "attachment_point": 5,
                                       "style": self.gost_style_name}).set_location((111.5 + self.x, 5 + self.y))
        """lines"""
        self.msp.add_lwpolyline(
            [(0 + self.x, 0 + self.y), (223 + self.x, 0 + self.y), (223 + self.x, -16 + self.y),
             (0 + self.x, -16 + self.y), (0 + self.x, 0 + self.y)],
            close=True, dxfattribs={'color': 7, 'const_width': 0.5})
        self.msp.add_lwpolyline([(25 + self.x, 0 + self.y), (25 + self.x, -16 + self.y)], close=False,
                                dxfattribs={'color': 7, 'const_width': 0.5})
        self.msp.add_lwpolyline([(50 + self.x, 0 + self.y), (50 + self.x, -16 + self.y)], close=False,
                                dxfattribs={'color': 7, 'const_width': 0.5})
        self.msp.add_lwpolyline([(115 + self.x, 0 + self.y), (115 + self.x, -16 + self.y)], close=False,
                                dxfattribs={'color': 7, 'const_width': 0.5})
        self.msp.add_lwpolyline([(125 + self.x, 0 + self.y), (125 + self.x, -16 + self.y)], close=False,
                                dxfattribs={'color': 7, 'const_width': 0.5})
        self.msp.add_lwpolyline([(180 + self.x, 0 + self.y), (180 + self.x, -16 + self.y)], close=False,
                                dxfattribs={'color': 7, 'const_width': 0.5})

        """headers"""
        self.msp.add_mtext("Позиция\nпо генплану", dxfattribs={"char_height": 3.0, "color": 7, "attachment_point": 5,
                                                               "style": self.gost_style_name}).set_location(
            (12.5 + self.x, -8 + self.y))
        self.msp.add_mtext("Обозначение", dxfattribs={"char_height": 3.0, "color": 7, "attachment_point": 5,
                                                      "style": self.gost_style_name}).set_location(
            (37.5 + self.x, -8 + self.y))
        self.msp.add_mtext("Наименование", dxfattribs={"char_height": 3.0, "color": 7, "attachment_point": 5,
                                                       "style": self.gost_style_name}).set_location(
            (82.5 + self.x, -8 + self.y))
        self.msp.add_mtext("Кол.", dxfattribs={"char_height": 3.0, "color": 7, "attachment_point": 5,
                                               "style": self.gost_style_name}).set_location((120 + self.x, -8 + self.y))
        self.msp.add_mtext("Характеристика", dxfattribs={"char_height": 3.0, "color": 7, "attachment_point": 5,
                                                         "style": self.gost_style_name}).set_location(
            (152.5 + self.x, -8 + self.y))
        self.msp.add_mtext("Примечание", dxfattribs={"char_height": 3.0, "color": 7, "attachment_point": 5,
                                                     "style": self.gost_style_name}).set_location(
            (201.5 + self.x, -8 + self.y))

    def display_elems(self):
        data = self.prepare_elems()
        line_num = 0
        x_values = [2 + self.x, 27 + self.x, 52 + self.x, 117 + self.x, 127 + self.x, 182 + self.x]
        for object in data:
            amount_of_lines = len(max(object, key=lambda x: len(x)))
            for y in range(amount_of_lines):
                for x in range(len(object)):
                    if len(object[x]) <= y or object[x][y] == "":
                        continue
                    else:
                        self.msp.add_mtext(object[x][y],
                                           dxfattribs={"char_height": 3.0, "color": 7, "attachment_point": 1,
                                                       "style": self.gost_style_name}).set_location(
                            (x_values[x], line_num * (-8) - 18 + self.y))
                if y == amount_of_lines - 1:
                    self.msp.add_lwpolyline([(0 + self.x, (line_num + 1) * (-8) - 16 + self.y),
                                             (223 + self.x, (line_num + 1) * (-8) - 16 + self.y)],
                                            dxfattribs={'color': 7, 'const_width': 0.5})
                else:
                    self.msp.add_line((0 + self.x, (line_num + 1) * (-8) - 16 + self.y),
                                      (180 + self.x, (line_num + 1) * (-8) - 16 + self.y),
                                      dxfattribs={'color': 7, 'lineweight': 30})
                line_num += 1

        self.msp.add_lwpolyline(
            [(0 + self.x, -16 + self.y), (0 + self.x, line_num * (-8) - 16 + self.y)],
            close=False,
            dxfattribs={'color': 7, 'const_width': 0.3}
        )

        self.msp.add_lwpolyline(
            [(25 + self.x, -16 + self.y), (25 + self.x, line_num * (-8) - 16 + self.y)],
            close=False,
            dxfattribs={'color': 7, 'const_width': 0.3}
        )

        self.msp.add_lwpolyline(
            [(50 + self.x, -16 + self.y), (50 + self.x, line_num * (-8) - 16 + self.y)],
            close=False,
            dxfattribs={'color': 7, 'const_width': 0.3}
        )

        self.msp.add_lwpolyline(
            [(115 + self.x, -16 + self.y), (115 + self.x, line_num * (-8) - 16 + self.y)],
            close=False,
            dxfattribs={'color': 7, 'const_width': 0.3}
        )

        self.msp.add_lwpolyline(
            [(125 + self.x, -16 + self.y), (125 + self.x, line_num * (-8) - 16 + self.y)],
            close=False,
            dxfattribs={'color': 7, 'const_width': 0.3}
        )

        self.msp.add_lwpolyline(
            [(180 + self.x, -16 + self.y), (180 + self.x, line_num * (-8) - 16 + self.y)],
            close=False,
            dxfattribs={'color': 7, 'const_width': 0.3}
        )

        self.msp.add_lwpolyline(
            [(223 + self.x, -16 + self.y), (223 + self.x, line_num * (-8) - 16 + self.y)],
            close=False,
            dxfattribs={'color': 7, 'const_width': 0.3}
        )

    def prepare_elems(self):
        all_lines = []
        for object in self.data:
            one_line = []
            sizes = [13, 13, 30, 5, 25, 22]
            for cell in range(len(object)):
                if type(object[cell]) != str and type(object[cell]) != int:
                    one_line.append([""])
                else:
                    if len(str(object[cell])) > sizes[cell]:
                        one_line.append(self.split_string_by_length(str(object[cell]), sizes[cell]))
                    else:
                        one_line.append([str(object[cell])])
            all_lines.append(one_line)
        return all_lines


    def split_string_by_length(self, text, max_length):
        words = text.split()  # Разбиваем строку по пробелам
        result = []
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + (1 if current_line else 0) <= max_length:
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


if __name__ == "__main__":
    doc = ezdxf.new('R2010', setup=True)
    doc.units = ezdxf.units.MM
    msp = doc.modelspace()
    e = Explication(doc, msp, 100, 100)
    doc.saveas("11.dxf")
    print("Файл fixed_blocks.dxf успешно создан")
