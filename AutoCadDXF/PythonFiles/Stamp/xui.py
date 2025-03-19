import ezdxf

# Создаем новый документ DXF
doc = ezdxf.new()

# Получаем модельное пространство
msp = doc.modelspace()

# Запрашиваем параметры у пользователя
layer_name = "F_TitleBox"
layer_color = 4
default_text = "Фамилия"

doc.layers.add(name=layer_name, color=layer_color)

# Параметры штампа
stamp_width = 100
stamp_height = 50

# Создаем блок для штампа
block = doc.blocks.new(name='штамп')

# Добавляем прямоугольник штампа в блок
block.add_lwpolyline(
    points=[(0, 0), (stamp_width, 0), (stamp_width, stamp_height), (0, stamp_height), (0, 0)],
    close=True,
    dxfattribs={'layer': layer_name}
)

# Добавляем атрибут текста в блок
tag_name = "TEXT_ATTR"  # Название тега
# block.add_attdef(
#     tag=tag_name,
#     prompt="Введите текст штампа:",
#     default=default_text,
#     dxfattribs={
#         'layer': layer_name,
#         'height': 5,
#         'insert': (stamp_width / 2, stamp_height / 2),
#         'align': 'MIDDLE_CENTER'
#     }
# )

# Добавляем название тега рядом с текстом по умолчанию
block.add_text(
    tag_name,  # Название тега
    dxfattribs={
        'layer': layer_name,
        'height': 3,
        'insert': (stamp_width / 2 - 20, stamp_height / 2 + 10),  # Позиция рядом с текстом
    }
)


# Функция для создания таблицы внутри блока
def create_table_in_block(block, layer_name, start_x, start_y, col_w, row_h):
    headers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
    data = [
        ["Изм.", "Кол.уч", "Лист", "№ док", "Подпись", "Дата"],
        ["Разработал", "Фамилия", "", "", "", "", "Стадия", "Лист", "Листов"],
        ["Проверил", "Фамилия"],
        ["Нач. отдела", "Фамилия"],
        ["Тхконтроль", "Фамилия"],
        ["Н.контроль", "Фамилия"],
        ["ГИП", "Фамилия"],
        ["Формат", "Файл"]
    ]

    # Вертикальные линии
    for col in range(15):
        x = start_x + col * col_w
        block.add_line(
            start=(x, start_y),
            end=(x, start_y - 12 * row_h),
            dxfattribs={'layer': layer_name}
        )

    # Горизонтальные линии
    for row in range(13):
        y = start_y - row * row_h
        block.add_line(
            start=(start_x, y),
            end=(start_x + 14 * col_w, y),
            dxfattribs={'layer': layer_name}
        )

    # Заголовки
    for idx, header in enumerate(headers):
        block.add_text(
            header,
            dxfattribs={
                'layer': layer_name,
                'height': 3,
                'insert': (start_x + idx * col_w + 2, start_y - 2)
            }
        )

    # Данные
    for row_num, row_data in enumerate(data):
        y_pos = start_y - (row_num + 1) * row_h - 2
        for col_num, text in enumerate(row_data):
            block.add_text(
                text,
                dxfattribs={
                    'layer': layer_name,
                    'height': 3,
                    'insert': (start_x + col_num * col_w + 2, y_pos)
                }
            )


# Параметры таблицы
table_start_x = 0  # Стартовая позиция X
table_start_y = -stamp_height - 20  # Смещение ниже штампа
column_width = 15
row_height = 10

# Создаем таблицу внутри блока
create_table_in_block(
    block=block,
    layer_name=layer_name,
    start_x=table_start_x,
    start_y=table_start_y,
    col_w=column_width,
    row_h=row_height
)

# Вставляем блок в модельное пространство
stamp_ref = msp.add_blockref('штамп', insert=(0, 0), dxfattribs={'layer': layer_name})
stamp_ref.add_attrib(tag_name, default_text)

# Сохраняем файл
doc.saveas('stamp_with_table_and_tag.dxf')


