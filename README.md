# where_to_go

<b>Интерактивная карта города с интересными местами и их описанием</b>

![preview](https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/.gitbook/assets/site.png)

# Демо-версией сайта: 

[https://elnarmengelbaev.pythonanywhere.com/](https://elnarmengelbaev.pythonanywhere.com/)

# Настройка переменных окружения
Создайте файл `.env` рядом с файлом `manage.py`

Придумайте или сгенерируйте секретный ключ и сохраните его в `.env`:

```
SECRET_KEY=<Ваш секретный ключ>
```
Если хотите включить режим отладки сохраните так же переменную `DEBUG`:

```
DEBUG=True
```

# Запуск
Скачайте код к себе на компьютер

Перейдите в папку с проектом и создайте виртуальное окружение, а затем активируйте его:
```
python3 -m venv venv
```

```
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

# Загрузка локаций

Для загрузки небольшого количества мест удобно использовать админку: 
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin), 
при большом числе локаций есть возможность добавить их в базу данных командой `load_place``.

Для этого сохраните данные о локациях в отдельных json файлах вида:

```js
{
    "title": "Эйфелева башня в Москве",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/8868d171420b5221f8f50af5e95a7b12.jpeg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/46cb25cf1719bf546c8bbcf1b51ba4f4.jpeg"
    ],
    "description_short": "Вы можете поехать в Париж и отстоять огромную очередь, 
    чтобы посетить главную его достопримечательность — великолепную Эйфелеву башню.
    А можете просто сесть в метро и, не выезжая за пределы МКАД, прикоснуться к точной 
    её копии.",
    "description_long": "<p><strong>Эйфелева башня в Москве</strong> находится 
    недалеко от станции метро «Авиамоторная» на территории одного из производственных
    предприятий — завода «Москабельмет». Соорудили точную копию мировой архитектурной 
    знаменитости сами рабочие этого завода. Высота заводской башни — 15 метров (для 
    справки — высота оригинальной, парижской Эйфелевой башни составляет 324 метра)."
    "coordinates": {
        "lng": "37.71241599999999",
        "lat": "55.74669399999998"
    }
}
```

Затем запустите команду заменив `<json_file_url>` на url вашего файла:
```
python manage.py load_place <json_file_url>
```
После окончания загрузки запустите сервер командой:
```
python manage.py runserver
```

Сайт будет доступен по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)



