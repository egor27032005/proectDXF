from flask import Flask, request, send_file
import io
import ezdxf
import pandas as pd
import os
import logging

from PythonFiles.FullPreparation.StartPreparation import StartPreparation

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(level=logging.ERROR)

@app.route('/health')
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
        # Читаем Excel файл с помощью pandas
        # df = pd.read_excel(file, header=None)

        # Преобразуем DataFrame в список списков (переменная data)
        # data = df.values.tolist()
        # sheets_dict = pd.read_excel(file, engine="openpyxl", sheet_name=None)

        # Чтение Excel-файла в словарь DataFrame'ов
        sheets_dict = pd.read_excel(file, engine="openpyxl", sheet_name=None)

        # Преобразование каждого DataFrame в список списков (построчно)
        result_dict = {
            sheet_name: df.values.tolist()
            for sheet_name, df in sheets_dict.items()
        }

        result_dict_with_headers = {
            sheet_name: [df.columns.tolist()] + df.values.tolist()
            for sheet_name, df in sheets_dict.items()
        }

        sheet_names = list(sheets_dict.keys())
        ind_tit=sheet_names.index("титульник") if "титульник" in sheet_names else None
        first_non_title = next((i for i, x in enumerate(sheet_names) if x != "титульник"), -1)
        data=result_dict_with_headers[sheet_names[first_non_title]]
        doc = ezdxf.new("R2000")
        msp = doc.modelspace()

        if ind_tit is None:
            st = StartPreparation(data, option, msp, doc)
        else:
            tit = result_dict_with_headers[sheet_names[ind_tit]]
            st=StartPreparation(data, option, msp, doc,tit)

        # Временный файл для сохранения DXF
        temp_file = "temp_output.dxf"
        doc.saveas(temp_file)  # Сохраняем DXF файл на диск

        # Читаем временный файл в байтовый поток
        with open(temp_file, "rb") as f:
            dxf_stream = io.BytesIO(f.read())

        # Удаляем временный файл
        os.remove(temp_file)

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
    app.run(host='0.0.0.0', port=5000)