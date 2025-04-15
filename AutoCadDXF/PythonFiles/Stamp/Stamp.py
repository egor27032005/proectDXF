# import random
#
# import ezdxf
# from ezdxf.math import Vec2
# from typing import List, Dict, Tuple
# class Stamp:
#     def __init__(self,doc,msp,points):
#         self.doc=doc
#         self.msp=msp
#         self.block = self.doc.blocks.new(name='штамп')
#         self.points=[int(i) for i in points]
#         self.max_y, self.min_y, self.max_x, self.min_x = self.points[0], self.points[1], self.points[2], self.points[-1]
#         self.stamp_ref = self.msp.add_blockref('штамп', insert=(0, 0), dxfattribs={'layer': "F_TitleBox"})
#         self.attributes = []
#         self.labels = []
#         self.sheet_sizes = {
#     'A4': (210, 297),
#     'A3': (297, 420),
#     'A2': (420, 594),
#     'A1': (594, 841),
# }
#         self.get_size()
#         self.draw()
#         self.add_attribute("NAME", "Name:", (0, 0))
#         values = {
#             "NAME": "Object",
#         }
#         self.insert_block(
#             (10, 20),
#             values,
#             rotation=15,
#             scale=0.8 + 15 * 0.2
#         )
#
#
#     def get_size(self):
#         self.size_x=int(self.max_x-self.min_x)
#         self.size_y=int(self.max_y-self.min_y)
#         self.drawing_long,self.drawing_short=self.find_minimal_paper_size(self.size_x,self.size_y)
#         ots_x=(self.drawing_long-self.size_x)//2
#         ots_y=(self.drawing_short-self.size_y)//2
#         if ots_y>55 or ots_x>185:
#             self.zero_x=self.min_x-ots_x
#             self.zero_y=self.min_y-ots_y
#             print(1)
#         else:
#             self.zero_x = self.min_x-20
#             self.zero_y = self.min_y-20
#             print(2)
#
#     def find_minimal_paper_size(self, x_size, y_size):
#         """
#         Возвращает размеры минимального холста из стандартных листов,
#         на который поместится чертеж размером (x_size, y_size) с учетом таблички 55x185 в правом нижнем углу.
#         """
#
#         STANDARD_SIZES = [
#             (210, 297),  # A4
#             (297, 420),  # A3
#             (420, 594),  # A2
#             (594, 841),  # A1
#             (841, 1189)  # A0
#         ]
#         TABLE_WIDTH = 55
#         TABLE_HEIGHT = 185
#         MARGIN = 5  # Защитный отступ от таблички
#         drawing_long = max(x_size, y_size)
#         drawing_short = min(x_size, y_size)
#         for width, height in sorted(STANDARD_SIZES, key=lambda x: min(x)):
#             # Доступная область (лист минус табличка с отступом)
#             available_width = width - TABLE_WIDTH - MARGIN
#             available_height = height - TABLE_HEIGHT - MARGIN
#
#             # Проверяем, помещается ли чертеж в доступную область
#             # Вариант 1: книжная ориентация
#             if (drawing_short <= available_width and drawing_long <= height) or \
#                     (drawing_short <= available_height and drawing_long <= width):
#                 return (width, height)
#
#             if drawing_short <= height:
#                 num_sheets_width = (drawing_long + available_width - 1) // available_width
#                 return (width * num_sheets_width, height)
#
#             # Вариант 3: соединение листов по высоте
#             if drawing_long <= width:
#                 num_sheets_height = (drawing_short + available_height - 1) // available_height
#                 return (width, height * num_sheets_height)
#         required_width = drawing_long + TABLE_WIDTH + MARGIN
#         required_height = drawing_short + TABLE_HEIGHT + MARGIN
#         return (required_width, required_height)
#
#
#     def draw(self):
#         x1=self.zero_x
#         y1=self.zero_y
#         x2=self.zero_x+self.drawing_long
#         y2=self.zero_y+self.drawing_short
#
#         self.block.add_lwpolyline(
#             points=[(x1, y1), (x1,y2), (x2,y2), (x2,y1), (x1,y1)],
#             close=True,
#             dxfattribs={'layer': "F_TitleBox",'color': 4}
#         )
#         polyline = self.block.add_lwpolyline(
#             points=[(x1+20, y1+5), (x1+20, y2-5), (x2-5, y2-5), (x2-5, y1+5), (x1+20, y1+5)],
#             close=True,
#             dxfattribs={'layer': "F_TitleBox", 'color': 2}
#         )
#         polyline.dxf.const_width = 0.4
#
#     def add_attribute(self,
#                       tag: str,
#                       label: str,
#                       position: Tuple[float, float],
#                       label_offset: float = 1.0,
#                       height: float = 0.5,
#                       color: int = 3) -> None:
#         """
#         Добавляет атрибут с подписью в блок
#         :param tag: имя атрибута (например, "XPOS")
#         :param label: подпись (например, "X Position:")
#         :param position: позиция (x, y)
#         :param label_offset: расстояние между подписью и значением
#         :param height: высота текста
#         :param color: цвет
#         """
#         x, y = position
#
#         # Добавляем подпись
#         self.block.add_text(label, dxfattribs={
#             'height': height,
#             'color': color,
#             'insert': (x, y)
#         })
#
#         # Добавляем атрибут
#         self.block.add_attdef(tag, (x + label_offset, y), dxfattribs={
#             'height': height,
#             'color': color
#         })
#
#         self.attributes.append(tag)
#         self.labels.append(label)
#     def insert_block(self,
#                      insert_point: Tuple[float, float],
#                      values: Dict[str, str],
#                      rotation: float = 0,
#                      scale: float = 1.0) -> None:
#         """
#         Вставляет блок в указанную точку
#         :param msp: пространство модели
#         :param insert_point: точка вставки (x, y)
#         :param values: значения атрибутов
#         :param rotation: угол поворота
#         :param scale: масштаб
#         """
#         blockref = self.msp.add_blockref(self.block.name, insert_point, dxfattribs={
#             'rotation': rotation
#         }).set_scale(scale)
#         blockref.add_auto_attribs(values)
#
#
#
#
#
#
import random
import ezdxf
from ezdxf.math import Vec2
from typing import List, Dict, Tuple


class Stamp:
    def __init__(self, doc, msp, points):
        self.doc = doc
        self.msp = msp
        self.block = self.doc.blocks.new(name='штамп')
        self.points = [int(i) for i in points]
        self.max_y, self.min_y, self.max_x, self.min_x = self.points[0], self.points[1], self.points[2], self.points[-1]
        self.stamp_ref = self.msp.add_blockref('штамп', insert=(0, 0), dxfattribs={'layer': "F_TitleBox"})
        self.attributes = []
        self.labels = []
        self.sheet_sizes = {
            'A4': (210, 297),
            'A3': (297, 420),
            'A2': (420, 594),
            'A1': (594, 841),
        }
        self.get_size()
        self.draw()

        # Добавляем точку в блок "штамп" (в начало координат блока)
        self.block.add_point((0, 0), dxfattribs={'color': 1, 'layer': 'POINTS'})

        self.add_attribute("NAME", "Name:", (0, 0))
        values = {
            "NAME": "Object",
        }
        self.insert_block(
            (10, 20),
            values,
            rotation=15,
            scale=0.8 + 15 * 0.2
        )

    def get_size(self):
        self.size_x = int(self.max_x - self.min_x)
        self.size_y = int(self.max_y - self.min_y)
        self.drawing_long, self.drawing_short = self.find_minimal_paper_size(self.size_x, self.size_y)
        ots_x = (self.drawing_long - self.size_x) // 2
        ots_y = (self.drawing_short - self.size_y) // 2
        if ots_y > 55 or ots_x > 185:
            self.zero_x = self.min_x - ots_x
            self.zero_y = self.min_y - ots_y
            print(1)
        else:
            self.zero_x = self.min_x - 20
            self.zero_y = self.min_y - 20
            print(2)

    def find_minimal_paper_size(self, x_size, y_size):
        STANDARD_SIZES = [
            (210, 297),  # A4
            (297, 420),  # A3
            (420, 594),  # A2
            (594, 841),  # A1
            (841, 1189)  # A0
        ]
        TABLE_WIDTH = 55
        TABLE_HEIGHT = 185
        MARGIN = 5
        drawing_long = max(x_size, y_size)
        drawing_short = min(x_size, y_size)

        for width, height in sorted(STANDARD_SIZES, key=lambda x: min(x)):
            available_width = width - TABLE_WIDTH - MARGIN
            available_height = height - TABLE_HEIGHT - MARGIN

            if (drawing_short <= available_width and drawing_long <= height) or \
                    (drawing_short <= available_height and drawing_long <= width):
                return (width, height)

            if drawing_short <= height:
                num_sheets_width = (drawing_long + available_width - 1) // available_width
                return (width * num_sheets_width, height)

            if drawing_long <= width:
                num_sheets_height = (drawing_short + available_height - 1) // available_height
                return (width, height * num_sheets_height)
        required_width = drawing_long + TABLE_WIDTH + MARGIN
        required_height = drawing_short + TABLE_HEIGHT + MARGIN
        return (required_width, required_height)

    def draw(self):
        x1 = self.zero_x
        y1 = self.zero_y
        x2 = self.zero_x + self.drawing_long
        y2 = self.zero_y + self.drawing_short

        self.block.add_lwpolyline(
            points=[(x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)],
            close=True,
            dxfattribs={'layer': "F_TitleBox", 'color': 4}
        )
        polyline = self.block.add_lwpolyline(
            points=[(x1 + 20, y1 + 5), (x1 + 20, y2 - 5), (x2 - 5, y2 - 5), (x2 - 5, y1 + 5), (x1 + 20, y1 + 5)],
            close=True,
            dxfattribs={'layer': "F_TitleBox", 'color': 2}
        )
        polyline.dxf.const_width = 0.4

    def add_attribute(self,
                      tag: str,
                      label: str,
                      position: Tuple[float, float],
                      label_offset: float = 1.0,
                      height: float = 0.5,
                      color: int = 3) -> None:
        x, y = position
        self.block.add_text(label, dxfattribs={
            'height': height,
            'color': color,
            'insert': (x, y)
        })
        self.block.add_attdef(tag, (x + label_offset, y), dxfattribs={
            'height': height,
            'color': color
        })
        self.attributes.append(tag)
        self.labels.append(label)

    def insert_block(self,
                     insert_point: Tuple[float, float],
                     values: Dict[str, str],
                     rotation: float = 0,
                     scale: float = 1.0) -> None:
        blockref = self.msp.add_blockref(self.block.name, insert_point, dxfattribs={
            'rotation': rotation
        }).set_scale(scale)
        blockref.add_auto_attribs(values)


def get_random_point():
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    return x, y


# Создаем новый документ DXF
doc = ezdxf.new('R2010')
msp = doc.modelspace()

# Создаем блок FLAG
flag = doc.blocks.new(name='FLAG')

# Добавляем атрибуты с подписями
flag.add_text('NAME:', dxfattribs={
    'height': 0.5,
    'color': 3,
    'insert': (0, -0.5)
})
flag.add_attdef('NAME', (1.5, -0.5), dxfattribs={'height': 0.5, 'color': 3})

flag.add_text('XPOS:', dxfattribs={
    'height': 0.25,
    'color': 4,
    'insert': (0, -1.0)
})
flag.add_attdef('XPOS', (1.5, -1.0), dxfattribs={'height': 0.25, 'color': 4})

flag.add_text('YPOS:', dxfattribs={
    'height': 0.25,
    'color': 4,
    'insert': (0, -1.5)
})
flag.add_attdef('YPOS', (1.5, -1.5), dxfattribs={'height': 0.25, 'color': 4})

# Добавляем блоки в модель
placing_points = [get_random_point() for _ in range(50)]
all_points = [coord for point in placing_points for coord in point]

# Создаем штамп (теперь он содержит точку в (0,0))
stamp = Stamp(doc, msp, all_points)

for number, point in enumerate(placing_points):
    values = {
        'NAME': f"P({number + 1})",
        'XPOS': f"= {point[0]:.3f}",
        'YPOS': f"= {point[1]:.3f}"
    }
    random_scale = 0.5 + random.random() * 2.0
    blockref = msp.add_blockref('FLAG', point, dxfattribs={
        'rotation': 15
    }).set_scale(random_scale)
    blockref.add_auto_attribs(values)

doc.saveas("stamp_with_point_and_attributes.dxf")