# import ezdxf
# from ezdxf import units
#
# class Wardrobe:
#     def __init__(self, msp, x, y):
#         """
#         Инициализация объекта Wardrobe.
#         :param msp: Modelspace, где будет происходить рисование.
#         :param x: Координата X середины верхней стороны прямоугольника.
#         :param y: Координата Y середины верхней стороны прямоугольника.
#         """
#         self.msp = msp
#         self.x = x
#         self.y = y
#         self.length = 6  # Длина прямоугольника
#         self.height = 3  # Высота прямоугольника
#         self.draw()
#
#     def draw(self):
#         """
#         Рисует прямоугольник и закрашивает две области в красный цвет.
#         """
#         # Вычисляем координаты углов прямоугольника
#         half_length = self.length / 2
#         half_height = self.height / 2
#
#         # Координаты вершин прямоугольника
#         top_left = (self.x - half_length, self.y)
#         top_right = (self.x + half_length, self.y)
#         bottom_left = (self.x - half_length, self.y - self.height)
#         bottom_right = (self.x + half_length, self.y - self.height)
#
#         # Рисуем прямоугольник
#         rect = self.msp.add_lwpolyline(
#             [top_left, top_right, bottom_right, bottom_left, top_left],
#             close=True
#         )
#         rect.dxf.color = 1
#
#         # Рисуем линии от середины верхней стороны к нижним углам
#         self.msp.add_line((self.x, self.y), bottom_left)
#         self.msp.add_line((self.x, self.y), bottom_right)
#
#         # Создаем две закрашенные области (hatch)
#         hatch1 = self.msp.add_hatch(color=1)  # Красный цвет (индекс 1)
#         hatch1.paths.add_polyline_path([top_left, (self.x, self.y), bottom_left, top_left], is_closed=True)
#
#         hatch2 = self.msp.add_hatch(color=1)  # Красный цвет (индекс 1)
#         hatch2.paths.add_polyline_path([top_right, (self.x, self.y), bottom_right, top_right], is_closed=True)
#
# # Пример использования
# def main():
#     # Создаем новый DXF документ
#     doc = ezdxf.new('R2010', setup=True)
#     doc.units = units.MM  # Устанавливаем единицы измерения (миллиметры)
#
#     # Получаем Modelspace
#     msp = doc.modelspace()
#
#     # Создаем объект Wardrobe и рисуем его
#     wardrobe = Wardrobe(msp, x=10, y=10)
#     wardrobe.draw()
#
#     # Сохраняем DXF файл
#     doc.saveas("wardrobe.dxf")
#
# if __name__ == "__main__":
#     main()
import ezdxf
from ezdxf import units

class Wardrobe:
    BLOCK_NAME = "шкаф"  # Фиксированное имя блока

    def __init__(self, doc, msp, x, y):
        """
        Инициализация объекта Wardrobe.
        :param doc: DXF документ
        :param msp: Modelspace, где будет размещен блок
        :param x: Координата X точки вставки блока
        :param y: Координата Y точки вставки блока
        """
        self.doc = doc
        self.msp = msp
        self.x = x
        self.y = y
        self.length = 6  # Длина прямоугольника
        self.height = 3  # Высота прямоугольника
        self.create_block()
        self.insert_block()

    def create_block(self):
        """Создает определение блока 'шкаф' с красной сплошной заливкой"""
        # Проверяем, не создан ли уже блок
        if self.BLOCK_NAME in self.doc.blocks:
            return

        # Создаем новый блок
        block = self.doc.blocks.new(name=self.BLOCK_NAME)

        # Вычисляем координаты относительно центра блока
        half_length = self.length / 2
        half_height = self.height / 2

        # Координаты вершин прямоугольника
        top_left = (-half_length, 0)
        top_right = (half_length, 0)
        bottom_left = (-half_length, -self.height)
        bottom_right = (half_length, -self.height)

        # 1. Сначала создаем полилинию (контур)
        rect = block.add_lwpolyline(
            [top_left, top_right, bottom_right, bottom_left, top_left],
            close=True,
            dxfattribs={'color': 1}  # Красный цвет контура
        )

        # 2. Добавляем линии от центра верха к нижним углам
        block.add_line((0, 0), bottom_left, dxfattribs={'color': 1})
        block.add_line((0, 0), bottom_right, dxfattribs={'color': 1})

        # 3. Добавляем СПЛОШНУЮ КРАСНУЮ ЗАЛИВКУ для левой части
        hatch_left = block.add_hatch()
        hatch_left.set_solid_fill(color=1)  # Сплошная заливка красным
        hatch_left.paths.add_polyline_path(
            [top_left, (0, 0), bottom_left, top_left],
            is_closed=True
        )

        # 4. Добавляем СПЛОШНУЮ КРАСНУЮ ЗАЛИВКУ для правой части
        hatch_right = block.add_hatch()
        hatch_right.set_solid_fill(color=1)  # Сплошная заливка красным
        hatch_right.paths.add_polyline_path(
            [top_right, (0, 0), bottom_right, top_right],
            is_closed=True
        )

    def insert_block(self):
        """Вставляет блок в указанные координаты"""
        self.msp.add_blockref(
            name=self.BLOCK_NAME,
            insert=(self.x, self.y),
            dxfattribs={'layer': '0'}
        )

# Пример использования
def main():
    # Создаем новый DXF документ
    doc = ezdxf.new('R2010', setup=True)
    doc.units = units.MM  # Устанавливаем единицы измерения (миллиметры)

    # Получаем Modelspace
    msp = doc.modelspace()

    # Создаем и вставляем блок "шкаф"
    wardrobe = Wardrobe(doc, msp, x=10, y=10)

    # Можно вставить несколько экземпляров блока
    Wardrobe(doc, msp, x=20, y=10)
    Wardrobe(doc, msp, x=30, y=10)

    # Сохраняем DXF файл
    doc.saveas("wardrobe_solid_fill.dxf")
    print("Файл 'wardrobe_solid_fill.dxf' успешно создан")

if __name__ == "__main__":
    main()