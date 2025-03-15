import ezdxf
from ezdxf import units
import math

class El_dvig:
    def __init__(self, msp, x, y):
        """
        Инициализация объекта El_dvig.
        :param msp: Modelspace, где будет происходить рисование.
        :param x: Координата X верхней точки окружности.
        :param y: Координата Y верхней точки окружности.
        """
        self.msp = msp
        self.x = x
        self.y = y
        self.radius = 6  # Радиус окружности
        self.m_height = 3  # Высота буквы "М"
        self.wave_length = 5  # Длина волнистой линии

    def draw(self):
        circle = self.msp.add_circle(center=(self.x, self.y - self.radius), radius=self.radius)
        circle.dxf.color = 2  # Жёлтый цвет (индекс 2)
        insertion_point_text = (self.x, self.y-4)
        mtext_content="М"
        self.msp.add_mtext(mtext_content, dxfattribs={
            'insert': insertion_point_text,
            'char_height': 2.5,
            'color': 1,
            'style': 'RomansStyle',
            'attachment_point': 2
        })
        wave_start_x = self.x - self.wave_length / 2  # Начало волнистой линии (центрирование)
        wave_start_y = self.y - self.radius + 1  # Смещение вниз от верхней точки окружности
        wave_points = []
        num_points = 100  # Количество точек для плавности
        for i in range(num_points + 1):
            t = i / num_points * self.wave_length
            x = wave_start_x + t
            y = wave_start_y + 0.5 * math.sin(2 * math.pi * t / self.wave_length)  # Синусоида для плавности
            wave_points.append((x, y))

        self.msp.add_lwpolyline(wave_points)

# Пример использования
def main():
    # Создаем новый DXF документ
    doc = ezdxf.new('R2010', setup=True)
    doc.units = units.MM  # Устанавливаем единицы измерения (миллиметры)

    # Получаем Modelspace
    msp = doc.modelspace()

    # Создаем объект El_dvig и рисуем его
    el_dvig = El_dvig(msp, x=10, y=10)
    el_dvig.draw()

    # Сохраняем DXF файл
    doc.saveas("el_dvig5.dxf")

if __name__ == "__main__":
    main()