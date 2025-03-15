import subprocess
import os

class DxfToDwgConverter:
    def __init__(self, oda_converter_path, input_dxf, output_dwg, version="ACAD2007"):
        """
        Инициализация конвертера.

        :param oda_converter_path: Путь к ODAFileConverter.exe
        :param input_dxf: Путь к входному DXF-файлу
        :param output_dwg: Путь к выходному DWG-файлу
        :param version: Версия DWG (например, ACAD2018, ACAD2021 и т.д.)
        """
        self.oda_converter_path = oda_converter_path
        self.input_dxf = input_dxf
        self.output_dwg = output_dwg
        self.version = version

    def convert(self):
        """
        Конвертирует DXF в DWG с использованием ODA File Converter.
        """
        # Проверяем, существует ли входной файл
        if not os.path.exists(self.input_dxf):
            raise FileNotFoundError(f"Входной файл {self.input_dxf} не найден.")

        # Проверяем, существует ли ODA File Converter
        if not os.path.exists(self.oda_converter_path):
            raise FileNotFoundError(f"ODA File Converter не найден по пути {self.oda_converter_path}.")

        # Формируем команду для конвертации
        command = [
            self.oda_converter_path,
            self.input_dxf,  # Входной файл
            self.output_dwg,  # Выходной файл
            self.version,     # Версия DWG
            "DWG",           # Тип входного файла
            "0",             # Рекурсивный режим (0 — нет, 1 — да)
            "0"              # Перезаписать выходной файл, если он существует (1 — да)
        ]

        # Выполняем команду
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print("Конвертация завершена успешно.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("Ошибка при конвертации:")
            print(e.stderr)

# Пример использования
if __name__ == "__main__":
    # Укажите путь к ODAFileConverter.exe
    oda_converter_path = r"C:\Users\1\Desktop\ODA File Converter 22.6.0 Portable\ODFC226\ODA File Converter 22.6.0.exe"

    # Укажите путь к входному DXF-файлу
    input_dxf = r"C:\Users\1\Desktop\pythonTransform\input"

    # Укажите путь для сохранения выходного DWG-файла
    output_dwg = r"C:\Users\1\Desktop\pythonTransform\output"

    # Создаем экземпляр конвертера
    converter = DxfToDwgConverter(oda_converter_path, input_dxf, output_dwg, version="ACAD2007")

    # Запускаем конвертацию
    converter.convert()
