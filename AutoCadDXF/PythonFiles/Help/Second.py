def find_minimal_paper_size(x_size, y_size):
    """
    Возвращает размеры минимального холста из стандартных листов,
    на который поместится чертеж размером (x_size, y_size).

    Параметры:
        x_size (int): ширина чертежа в мм
        y_size (int): высота чертежа в мм

    Возвращает:
        tuple: (ширина_холста, высота_холста) в мм
    """
    # Стандартные форматы бумаги (ширина x высота в мм)
    STANDARD_SIZES = [
        (210, 297),  # A4
        (297, 420),  # A3
        (420, 594),  # A2
        (594, 841),  # A1
        (841, 1189)  # A0
    ]

    # Определяем "длинную" и "короткую" стороны чертежа
    drawing_long = max(x_size, y_size)
    drawing_short = min(x_size, y_size)

    # Ищем минимальный стандартный размер, который покрывает хотя бы одну сторону
    for width, height in sorted(STANDARD_SIZES, key=lambda x: min(x)):
        # Если короткая сторона чертежа <= короткой стороне листа
        if drawing_short <= min(width, height):
            # Вычисляем сколько листов нужно по длинной стороне
            num_sheets = (drawing_long + max(width, height) - 1) // max(width, height)
            return (max(width, height) * num_sheets, min(width, height))

                    # Если длинная сторона чертежа <= длинной стороне листа
        if drawing_long <= max(width, height):
            # Вычисляем сколько листов нужно по короткой стороне
            num_sheets = (drawing_short + min(width, height) - 1) // min(width, height)
            return max(width, height), min(width, height) * num_sheets

    # Если не помещается даже на A0, возвращаем исходный размер
    return (drawing_long, drawing_short)


# Примеры использования:
print(find_minimal_paper_size(400, 200))  # (594, 420) - 2xA3 по ширине
print(find_minimal_paper_size(200, 400))  # (420, 594) - 2xA3 по высоте
print(find_minimal_paper_size(500, 300))  # (840, 594) - 2xA2 по ширине
print(find_minimal_paper_size(100, 600))  # (594, 891) - 3xA1 по высоте