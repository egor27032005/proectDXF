import ezdxf

def merge_into_block(input_file, output_file, block_name="MergedBlock"):
    """
    Объединяет всё содержимое DXF-файла, включая существующие блоки, в один блок.

    :param input_file: Путь к исходному DXF-файлу.
    :param output_file: Путь к выходному DXF-файлу.
    :param block_name: Имя создаваемого блока (по умолчанию "MergedBlock").
    """
    # Загружаем исходный DXF-файл
    doc = ezdxf.readfile(input_file)
    msp = doc.modelspace()  # Получаем пространство модели исходного файла

    # Создаем новый DXF-документ
    new_doc = ezdxf.new(setup=True)
    new_msp = new_doc.modelspace()  # Получаем пространство модели нового файла

    # Создаем новый блок
    block = new_doc.blocks.new(name=block_name)

    # Копируем все объекты из пространства модели исходного файла в блок
    for entity in msp:
        # Копируем объект
        new_entity = entity.copy()
        # Если это ссылка на блок (Block Reference), обрабатываем отдельно
        if entity.dxftype() == "INSERT":
            # Копируем блок, на который ссылается Block Reference
            block_def = doc.blocks.get(entity.dxf.name)
            if block_def:
                # Копируем определение блока в новый документ
                new_block = new_doc.blocks.new(name=block_def.name)
                for block_entity in block_def:
                    new_block.add_entity(block_entity.copy())
            # Добавляем Block Reference в новый блок
            block.add_entity(new_entity)
        else:
            # Добавляем обычный объект в блок
            block.add_entity(new_entity)

    # Копируем все блоки из исходного файла в новый документ
    for original_block in doc.blocks:
        # Пропускаем блоки, которые уже были скопированы через Block References
        if original_block.name not in new_doc.blocks:
            new_block = new_doc.blocks.new(name=original_block.name)
            for entity in original_block:
                new_block.add_entity(entity.copy())

    # Вставляем новый блок в пространство модели нового файла
    new_msp.add_blockref(block_name, insert=(0, 0))

    # Сохраняем новый DXF-файл
    new_doc.saveas(output_file)
    print(f"Файл успешно сохранен как {output_file}")



# Пример использования
input_file = "Чертеж3.dxf"
output_file = "output421.dxf"
merge_into_block(input_file, output_file, block_name="MergedBlock")