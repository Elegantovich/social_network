# social_network

### Tech
Python 3.7, Django 3.2, Rest Framework 3.13, Docker, PostgreSQL, nginx

## Описание.

Проект **social_network** является REST API для приложения формата соц. сети с пользователями и постами.

## Установка на локальном компьютере.
Эти инструкции помогут вам создать копию проекта и запустить ее на локальном компьютере для целей разработки и тестирования.

### Установка Docker.
Установите Docker, используя инструкции с официального сайта:
- для [Windows и MacOS](https://www.docker.com/products/docker-desktop)
- для [Linux](https://docs.docker.com/engine/install/ubuntu/). Отдельно потребуется установть [Docker Compose](https://docs.docker.com/compose/install/)

### Запуск проекта.
Склонируйте этот репозиторий в текущую папку
```
git clone https://github.com/Elegantovich/social_network/
```
Перейдите в папку 'dev'
```
cd dev
```
Создайте файл `.env` командой
```
touch .env
```
и добавьте в него переменные окружения для работы с базой данных:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432 
DJANGO_KEY='your_key'
```
Запустите docker-compose:
```
docker-compose up -d --build
```
Накатите миграции:
```
docker-compose exec web python manage.py migrate
```
Создайте суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
Соберите статику в единую папку:
```
docker-compose exec web python manage.py collectstatic --no-input
```


### Поддерживаемые endpoints:

| URL| Method | Description |
| ------ | ------ | ------ |
| http://localhost/api/auth/ | POST | Получить токен |
| http://localhost/api/users/ | POST, GET | Создать, просмотреть пользователя(-ей) |
| http://localhost/api/posts/ | POST, GET | Создать пост или получить все посты|
| http://localhost/api/posts/<post_id>/ | GET | Получить нужный блог |
| http://localhost/api/posts/<post_id>/favorite/ | POST, DELETE | Добавить (удалить) пост в избранное |
| http://localhost/api/posts/favorite/ | GET | Получить все избранные посты |


### Авторы:

[Хачатрян Максим](https://github.com/Elegantovich)<br>
