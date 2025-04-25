# treeview_menu
### Установка
```
git clone https://github.com/TaPPa45/treeview_menu.git
```

#### Создать .env
```
SECRET_KEY= some key
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1,[::1]

DATABASE_URL=sqlite:///app/db/db.sqlite3

LANGUAGE_CODE=ru-ru
TIME_ZONE=Europe/Moscow

STATIC_ROOT=/app/staticfiles
```
### Запуск
```docker-compose up --build -d```

```docker-compose exec web python manage.py createsuperuser```


Приложение будет доступно по адресу: http://localhost:8000

Админка доступна по URL: http://localhost:8000/admin/
