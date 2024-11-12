# Тестовое задание для Backend разработчика


## Описание задания:
Написать сервис, который принимает запрос с указанием кадастрового номера, широты и долготы, эмулирует отправку запроса на внешний сервер, который может обрабатывать запрос до 60 секунд. Затем должен отдавать результат запроса. Считается, что внешний сервер может ответить `true` или `false`.
Данные запроса на сервер и ответ с внешнего сервера должны быть сохранены в БД. Нужно написать АПИ для получения истории всех запросов/истории по кадастровому номеру.
### Сервис должен содержать следующие эндпоинты:
- `"/query"` - принимает кадастровый номер
- `"/ping"` - проверка, что  сервер запустился
- `"/history"` - для получения истории запросов
- `"/result"` - эндпоинт эмулируемоего сервера, который возвращает `true` или `false`
Сервис завернуть в Dockerfile.
Составить README с запуском. Наставникам будет проще и быстрее проверить вашу работу.
### Необходимый стэк:
- FastAPI (async роуты)
- PostgreSQL
- SQLAlchemy (async запросы)
- Alembic
- Docker
- Docker Compose

## Запуск проекта

- Клонируйте репозиторий
```
git clone git@github.com:monter220/test_antipoff-it.git
```
- Перейдите в каталог с проектом
```
cd test_antipoff-it/
```
- Заполните .env в корне проекта по примеру ./env.example

- Установите Docker
```
sudo apt update
sudo apt install curl
curl -fSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
sudo apt-get install docker-compose-plugin
```
- Запустите проект
```
docker-compose -f docker-compose.yaml up -d --build
```