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


# Добавляем атрибут текста в блок
tag_name = "TEXT_ATTR"
block.add_text(
    tag_name,  # Название тега
    dxfattribs={
        'layer': layer_name,
        'height': 3,
        'insert': (stamp_width / 2 - 20, stamp_height / 2 + 10),
    }
)

# Создаем таблицу внутри блока
# create_table_in_block(
#     block=block,
#     layer_name=layer_name,
#     start_x=table_start_x,
#     start_y=table_start_y,
#     col_w=column_width,
#     row_h=row_height
# )

# Вставляем блок в модельное пространство
stamp_ref = msp.add_blockref('штамп', insert=(0, 0), dxfattribs={'layer': layer_name})
stamp_ref.add_attrib(tag_name, default_text)

# Сохраняем файл
doc.saveas('stamp_with_table_and_tag12.dxf')


