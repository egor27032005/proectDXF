import ezdxf

# Создаем новый DXF-документ
doc = ezdxf.new(dxfversion='R2010')

# Добавляем новый слой (опционально)
doc.layers.new(name='RectangleLayer', dxfattribs={'color': 2})

# Получаем модель пространства (Modelspace)
msp = doc.modelspace()

# Задаем координаты вершин прямоугольника
x = 0  # Пример значения для self.x
y = 0  # Пример значения для self.y
vertices = [
    (x - 3, y - 3),
    (x - 3, y - 6),
    (x + 3, y - 6),
    (x + 3, y - 3),
    (x - 3, y - 3)  # Замыкаем прямоугольник
]

# Добавляем полилинию (прямоугольник) в модель пространства
msp.add_lwpolyline(vertices)

# Создаем заливку (Hatch) для прямоугольника
hatch = msp.add_hatch(color=2)  # 2 — это желтый цвет в DXF
hatch.set_solid_fill()  # Устанавливаем сплошную заливку
hatch.paths.add_polyline_path(vertices)  # Задаем путь для заливки

# Сохраняем DXF-документ
doc.saveas('filled_rectangle.dxf')