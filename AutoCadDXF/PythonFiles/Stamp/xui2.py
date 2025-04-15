import random
import ezdxf

doc = ezdxf.new('R2010')
msp = doc.modelspace()

def get_random_point():
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    return x, y

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

doc.saveas("1qblockfgfg_with_labels.dxf")