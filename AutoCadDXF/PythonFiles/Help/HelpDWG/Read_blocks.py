from pyautocad import Autocad, APoint
import math


def get_blocks_with_rotation_scale():
    # Подключаемся к активному экземпляру AutoCAD
    acad = Autocad(create_if_not_exists=True)

    # Создаем словарь для хранения блоков
    blocks_dict = {}

    # Получаем все объекты в текущем пространстве модели
    for entity in acad.iter_objects():
        # Проверяем, является ли объект блоком (Insert)
        if entity.EntityName == "AcDbBlockReference":
            block_name = entity.Name
            insertion_point = entity.InsertionPoint
            rotation_deg = math.degrees(entity.Rotation)  # Угол в градусах

            # Получаем масштабные коэффициенты по осям
            x_scale = entity.XScaleFactor
            y_scale = entity.YScaleFactor
            z_scale = entity.ZScaleFactor

            # Для простоты берем средний масштаб (или можно использовать x_scale как основной)
            scale_factor = (x_scale + y_scale + z_scale) / 3

            # Формируем данные: (поворот, масштаб, координаты)
            block_data = (
                rotation_deg,
                scale_factor,
                (insertion_point[0], insertion_point[1], insertion_point[2])
            )

            # Добавляем в словарь
            if block_name not in blocks_dict:
                blocks_dict[block_name] = []
            blocks_dict[block_name].append(block_data)

    return blocks_dict


if __name__ == "__main__":
    blocks = get_blocks_with_rotation_scale()
    print(blocks)

    for block_name, block_instances in blocks.items():
        print(f"Блок: {block_name}")
        for i, (rotation, scale, coords) in enumerate(block_instances, 1):
            print(f"  {i}. Поворот: {rotation:.2f}° | Масштаб: {scale:.2f} | "
                  f"Координаты: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")
        print()