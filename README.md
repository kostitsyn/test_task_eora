# Test task EORA


## Инструкция по запуску.

1. Создаём образ на основе Dockerfile:

`docker build -t my_container`

2. Запускаем контейнер на основе созданного образа:

`docker run -d --rm --name my_container -p 9000:9000 my_container`

Схема БД в файле **db_visualized.png**