# FROM python:3.10-slim
#
# # Устанавливаем рабочую директорию
# WORKDIR /app
#
# # Копируем зависимости
# COPY requirements.txt .
#
# # Устанавливаем зависимости
# RUN pip install --no-cache-dir -r requirements.txt
#
# # Копируем исходный код
# COPY . .
# EXPOSE 5000
#
# # Указываем команду для запуска приложения
# CMD ["python", "PythonFiles/Exchanger/app.py"]
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask ezdxf openpyxl waitress
COPY . .
ENV PYTHONPATH="${PYTHONPATH}:/app"
EXPOSE 5000
CMD ["python", "PythonFiles/Exchanger/app.py"]