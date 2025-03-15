import ezdxf
from ezdxf import units

class Wardrobe:
    def __init__(self, msp, x, y):
        """
        Инициализация объекта Wardrobe.
        :param msp: Modelspace, где будет происходить рисование.
        :param x: Координата X середины верхней стороны прямоугольника.
        :param y: Координата Y середины верхней стороны прямоугольника.
        """
        self.msp = msp
        self.x = x
        self.y = y
        self.length = 6  # Длина прямоугольника
        self.height = 3  # Высота прямоугольника
        self.draw()

    def draw(self):
        """
        Рисует прямоугольник и закрашивает две области в красный цвет.
        """
        # Вычисляем координаты углов прямоугольника
        half_length = self.length / 2
        half_height = self.height / 2

        # Координаты вершин прямоугольника
        top_left = (self.x - half_length, self.y)
        top_right = (self.x + half_length, self.y)
        bottom_left = (self.x - half_length, self.y - self.height)
        bottom_right = (self.x + half_length, self.y - self.height)

        # Рисуем прямоугольник
        rect = self.msp.add_lwpolyline(
            [top_left, top_right, bottom_right, bottom_left, top_left],
            close=True
        )
        rect.dxf.color = 1

        # Рисуем линии от середины верхней стороны к нижним углам
        self.msp.add_line((self.x, self.y), bottom_left)
        self.msp.add_line((self.x, self.y), bottom_right)

        # Создаем две закрашенные области (hatch)
        hatch1 = self.msp.add_hatch(color=1)  # Красный цвет (индекс 1)
        hatch1.paths.add_polyline_path([top_left, (self.x, self.y), bottom_left, top_left], is_closed=True)

        hatch2 = self.msp.add_hatch(color=1)  # Красный цвет (индекс 1)
        hatch2.paths.add_polyline_path([top_right, (self.x, self.y), bottom_right, top_right], is_closed=True)

# Пример использования
def main():
    # Создаем новый DXF документ
    doc = ezdxf.new('R2010', setup=True)
    doc.units = units.MM  # Устанавливаем единицы измерения (миллиметры)

    # Получаем Modelspace
    msp = doc.modelspace()

    # Создаем объект Wardrobe и рисуем его
    wardrobe = Wardrobe(msp, x=10, y=10)
    wardrobe.draw()

    # Сохраняем DXF файл
    doc.saveas("wardrobe.dxf")

if __name__ == "__main__":
    main()