FROM python:3.10

# Устанавливаем переменную окружения PYTHONUNBUFFERED для предотвращения буферизации вывода
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /code

# Копируем зависимости проекта и устанавливаем их через pip
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все содержимое текущей директории в рабочую директорию контейнера
COPY . /code/