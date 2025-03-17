from flask import Flask, request, send_file
import io
import ezdxf
import os
import logging
import warnings
from waitress import serve
from openpyxl import load_workbook  # Импортируем openpyxl

from flask_cors import CORS

from PythonFiles.FullPreparation.StartPreparation import StartPreparation

# Игнорируем предупреждение о Data Validation
warnings.filterwarnings("ignore", category=UserWarning, message="Data Validation extension is not supported and will be removed")

app = Flask(__name__)
CORS(app)

# Настройка логирования
logging.basicConfig(level=logging.ERROR)
@app.route('/')
def health_check():
    return "OK", 200

@app.route('/process-excel', methods=['POST'])
def process_excel():
    # Проверяем, есть ли файл и параметр в запросе
    if 'file' not in request.files or 'option' not in request.form:
        return {"error": "No file or option provided"}, 400

    file = request.files['file']  # Получаем файл
    option = request.form['option']  # Получаем выбранный параметр

    # Проверяем, что файл был загружен
    if file.filename == '':
        return {"error": "No file selected"}, 400

    # Проверяем, что файл имеет корректный формат
    if not file.filename.endswith('.xlsx') and not file.filename.endswith('.xls'):
        return {"error": "Unsupported file format. Only .xlsx and .xls are supported"}, 400

    try:
        # Сохраняем файл временно на диск
        temp_excel_file = "temp_input.xlsx"
        file.save(temp_excel_file)

        # Читаем Excel файл с помощью openpyxl
        wb = load_workbook(filename=temp_excel_file)
        ws = wb.active

        # Преобразуем данные в список списков
        data = []
        for row in ws.iter_rows(values_only=True):
            data.append(list(row))

        # Удаляем временный Excel-файл
        os.remove(temp_excel_file)

        # Создаем DXF документ
        doc = ezdxf.new("R2000")
        msp = doc.modelspace()

        # Пример добавления текста в DXF файл
        st = StartPreparation(data, option, msp, doc)

        # Временный файл для сохранения DXF
        temp_dxf_file = "temp_output.dxf"
        doc.saveas(temp_dxf_file)  # Сохраняем DXF файл на диск

        # Читаем временный файл в байтовый поток
        with open(temp_dxf_file, "rb") as f:
            dxf_stream = io.BytesIO(f.read())

        # Удаляем временный DXF-файл
        os.remove(temp_dxf_file)

        # Перемещаем указатель в начало потока
        dxf_stream.seek(0)

        # Возврат файла
        return send_file(
            dxf_stream,
            mimetype='application/octet-stream',
            as_attachment=True,
            download_name='output.dxf'
        )

    except Exception as e:
        # Логируем ошибку и возвращаем сообщение об ошибке
        app.logger.error(f"Error processing file: {e}")
        return {"error": "Failed to process the file"}, 500


if __name__ == '__main__':
    # Запуск через Waitress для production
    serve(app, host="0.0.0.0", port=5000)