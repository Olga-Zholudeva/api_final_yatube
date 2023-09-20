# Проект api_final_yatube

### Описание проекта:

Благодаря этому проекту зарегистрированные пользователи  могут:
 - создавать новые посты, комментировать посты других авторов, подписываться на любимых авторов
 - получать информацию о постах, группах постов и комментариев к постам, оставленные пользвателями
 - вносить изменения и удалять свои посты и комментарии

**Документация для API Yatube будет доступна по адресу http://127.0.0.1:8000/redoc/ после запуска проекта**

### Технологии:
- Python 3.7.9
- Django 2.2.16

### Запуск проекта:

- Клонируем репозиторий: **git clone [api_final_yatube](https://github.com/Olga-Zholudeva/api_final_yatube)**
- Cоздаем и активировируем виртуальное окружение: **python3 -m venv env source env/bin/activate**
- Устанавливаем зависимости из файла requirements.txt: **pip install -r requirements.txt**
- Переходим в папку yatube_api: **cd yatube_api**
- Создаем супер пользователя: **python manage.py createsuperuser**
- Запускаем проект на локальном устройстве: **python3 manage.py runserver**
- Использовать проект можно при помощи Postman

### Права доступа:
- GET запросы к БД постов, комментариев и групп доступны всем пользователям
- Остальные запросы доступны только для зарегистированных пользователей 
- Любые запросы к БД подпискчиков доступны только для зарегистрированных пользователей
- Создать пользователя в БД можно командой createsuperuser

<details open>
 <summary>Примеры запросов</summary>
 ### Примеры запросов для неавторизованных пользователей:
 - Пример GET-запроса на получение списка всех публикаций
 GET /api/v1/posts/
 - Пример ответа  
 {  
   "count": 123,  
   "next": "http://api.example.org/accounts/?offset=400&limit=100",  
   "previous": "http://api.example.org/accounts/?offset=200&limit=100",  
   "results": [  
               {  
                 "id": 0,  
                 "author": "string",  
                 "text": "string",  
                 "pub_date": "2021-10-14T20:41:29.648Z",  
                 "image": "string",  
                 "group": 0  
               }  
           ]  
 }  
 
 При указании параметров limit и offset выдача с пагинацией
 
 ### Примеры запросов для авторизованных пользователей:
 - Пример запроса на добавление новой публикации в коллекцию публикаций  
 POST /api/v1/posts/ ()  
 {  
   "text": "string",  
   "image": "string",  
   "group": 0  
 }  
 - Пример ответа
 {  
   "id": 0,  
   "author": "string",  
   "text": "string",
   "pub_date": "2019-08-24T14:15:22Z",  
   "image": "string",  
   "group": 0  
 }  
</details>

### Проект выполнила:

**Ольга Жолудева**
