# Test task EORA


## Инструкция по запуску.

1. Добавить в директорию проекта файл **secret.json**

2. Создаём образ на основе Dockerfile:

`docker build -t my_container .`

3.Запускаем контейнер на основе созданного образа:

`docker run -d --rm --name my_container -p 9000:9000 my_container`

Данные для входа в **админку**:

логин: *superuser*

пароль: *testtask*

Схема БД в файле **db_visualized.png**

База данных заполняется данными в файле миграций **0002_auto_20220202_1409.py**