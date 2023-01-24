# API для Yatube
## Описание проекта

Учебный проект, выполненный в ходе прохождения курсов Яндекс.Практикума. В нём реализован REST API и CRUD для социальной сети Yatube, сделанной в ходе прохождения предыдущих спринтов Яндекс.Практикума.
Возможности API:
- аутентификация с помощью JWT-токенов, обновление токена;
- создание, просмотр, изменение, удаление постов;
- просмотр сообществ;
- создание, просмотр, изменение, удаление комментариев к любым постам;
- подписка на авторов.

## **Стек технологий**
![python version](https://img.shields.io/badge/Python-3.7.8-green) **and** ![python version](https://img.shields.io/badge/Python-3.9.9-green)
![django version](https://img.shields.io/badge/Django-3.2.16-green)
![djangorestframework version](https://img.shields.io/badge/djangorestframework-3.12.4-green)
![djangorestframework-simplejwt](https://img.shields.io/badge/djangorestframework_simplejwt-4.7.2-green)


## Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/ozzimyt/api_final_yatube
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
. venv/Scripts/activate
```
Установить зависимости из файла ```requirements.txt```:
```
pip install -r requirements.txt
```
Перейти в папку с фалом ```manage.py```:
```
cd yatube_api
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```

## Примеры запросов к API
***Полная документация по API Yatube доступна после запуска сервера, по адресу: `http://127.0.0.1:8000/redoc/`***
  
### Аутентификация:

**Получение токена:**

POST запрос по адресу ```/api/v1/jwt/create/```

    {

      "username": "string",

      "password": "string"

    }

**Пример ответа:**

    {

      "refresh": "string",

      "access": "string"

    }

Токен вернётся в поле access, а данные из поля refresh пригодятся для обновления токена. 
При отправке запроcов необходимо указать токен в заголовке Authorization: Bearer <токен>.

### Примеры запросов:

**Получение всех публикаций пользователей:**

GET запрос по адресу ```/api/v1/posts/```

**Пример ответа:**


    {

      "id": 0,

      "author": "string",

      "text": "string",

      "pub_date": "date",

      "image": "string",

      "group": 0

    }


**Подписка на пользователя(анонимные запросы запрещены):**

POST запрос по адресу ```/api/v1/follow/```

    {

      "following": "string"
      
    }

**Пример ответа:**

    {

      "user": "string",

      "following": "string"

    }
