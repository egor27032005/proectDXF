from pyautocad import Autocad, APoint
import comtypes

class Rider:
    def __init__(self, acad):
        self.acad = acad

    def extract_text_with_coordinates(self, single_line_file, multi_line_file):
        """
        Читает текст (включая многострочный) и его координаты из AutoCAD
        и сохраняет в два разных файла: для однострочного и многострочного текста.
        После чтения многострочный текст удаляется из AutoCAD.
        """
        try:
            with open(multi_line_file, 'w', encoding='utf-8') as multi_file:
                mtext_entities = list(self.acad.iter_objects('MText'))  # Собираем все MText объекты
                for entity in mtext_entities:
                    try:
                        text = entity.TextString.replace('|', ' ')  # Заменяем разделитель в тексте
                        insertion_point = entity.InsertionPoint  # Координаты вставки текста
                        x, y, z = insertion_point
                        multi_file.write(f"{text}|{x}|{y}|{z}\n")  # Используем | как разделитель

                        # Удаляем многострочный текст после чтения
                        entity.Delete()
                        print(f"Многострочный текст удален: {text}")
                    except comtypes.COMError as e:
                        print(f"Ошибка при обработке многострочного текста: {e}. Пропуск объекта.")
                        continue
            # Обрабатываем обычный текст (Text)
            with open(single_line_file, 'w', encoding='utf-8') as single_file:
                for entity in self.acad.iter_objects('Text'):
                    try:
                        text = entity.TextString.replace('|', ' ')  # Заменяем разделитель в тексте
                        insertion_point = entity.InsertionPoint  # Координаты вставки текста
                        x, y, z = insertion_point
                        single_file.write(f"{text}|{x}|{y}|{z}\n")  # Используем | как разделитель
                    except comtypes.COMError as e:
                        print(f"Ошибка при обработке текстового объекта: {e}. Пропуск объекта.")
                        continue

            # Обрабатываем многострочный текст (MText)

            print(f"Однострочный текст сохранен в файл: {single_line_file}")
            print(f"Многострочный текст сохранен в файл: {multi_line_file}")

        except Exception as e:
            print(f"Произошла ошибка: {e}")


class Printer:
    def __init__(self, acad):
        self.acad = acad

    def draw_text_from_files(self, single_line_file, multi_line_file, text_height):
        """
        Читает текст и координаты из двух файлов
        и рисует текст в AutoCAD на прежних местах.
        """
        try:
            # Рисуем однострочный текст
            with open(single_line_file, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split('|')
                    if len(parts) == 4:  # Проверяем, что строка содержит текст и координаты
                        text, x, y, z = parts
                        try:
                            insert_point = APoint(float(x), float(y), float(z))  # Координаты вставки
                            self.acad.model.AddText(text, insert_point, text_height)  # Рисуем текст
                        except ValueError as e:
                            print(f"Ошибка при обработке координат: {e}. Пропуск строки: {line}")

            # Рисуем многострочный текст
            with open(multi_line_file, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split('|')
                    if len(parts) == 4:  # Проверяем, что строка содержит текст и координаты
                        text, x, y, z = parts
                        try:
                            insert_point = APoint(float(x), float(y), float(z))  # Координаты вставки
                            self.acad.model.AddMText(insert_point, text_height * 10, text)  # Рисуем MText
                        except ValueError as e:
                            print(f"Ошибка при обработке координат: {e}. Пропуск строки: {line}")

            print("Текст из файлов нарисован в AutoCAD на прежних местах.")

        except Exception as e:
            print(f"Произошла ошибка: {e}")


# Пример использования
if __name__ == "__main__":
    try:
        # Инициализация AutoCAD
        acad = Autocad(create_if_not_exists=True)
        print("Подключение к AutoCAD успешно установлено.")

        # Создаем объекты Rider и Printer
        rider = Rider(acad)
        # printer = Printer(acad)

        # Извлекаем текст и координаты из AutoCAD и сохраняем в два файла
        single_line_file = 'single_line_text.txt'
        multi_line_file = 'multi_line_text.txt'
        rider.extract_text_with_coordinates(single_line_file, multi_line_file)

        # Рисуем текст из файлов в AutoCAD на прежних местах
        text_height = 2.5  # Высота текста
        # printer.draw_text_from_files(single_line_file, multi_line_file, text_height)

        # with open('Telegram/lines.txt', 'r') as file:
        #     lines = [list(map(float, line.split())) for line in file]
        # for line in lines:
        #     color = line[0]
        #     point1 = APoint(line[1], line[2])
        #     point2 = APoint(line[3], line[4])
        #     lin = acad.model.AddLine(point1, point2)
        #     lin.color = color


    except comtypes.COMError as e:
        print(f"Ошибка COM: {e}. Убедитесь, что AutoCAD запущен и доступен.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")