# where_to_go

<b>Интерактивная карта города с интересными местами и их описанием</b>

![preview](https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/.gitbook/assets/site.png)
# Запуск
Скачайте код к себе на компьютер

Перейдите в папку с проектом и создайте виртуальное окружение, а затем активируйте его:
```
python3 -m venv venv
source venv/bin/activate
```

Установите зависимости командой
```
pip install -r requirements.txt
```

Запустите миграции:
```
python manage.py migrate
```

Создайте суперпользователя:
```
python manage.py createsuperuser
```
Локальный сервер запускается командой:
```
python manage.py runserver
```
Чтобы добавить свои места на карту создайте файл `db.sqlite3` рядом с файлом manage.py.<br>
Теперь вы можете добавлять описания и фотографии ваших мест и они будут отображаться на карте

Сайт будет доступен по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Админка: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
