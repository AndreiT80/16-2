#Домашнее задание по теме "Валидация данных".module_16_2.py

from fastapi import FastAPI, Path
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app=FastAPI()

# Определение базового маршрута
@app.get('/')
async def main_page():
    return 'Главная страница'

# Создаem маршрут к странице администратора - "/user/admin".
@app.get('/user/admin')
async def admin_page():
    return 'Вы вошли как администратор'

# GET-запрос — получение данных:
@app.get('/user/{user_id}')
async def user_page_id(user_id: Annotated[int,Path(ge=1,
                                                   le=100,
                                                   description='Enter User ID', example='1')]):
    return f'Вы вошли как пользователь № {user_id}'

# GET-запрос — получение данных:
@app.get('/user/{username}/{age}')
async def user_page(username: Annotated[str,Path(min_length=5, max_length=20,
                                      description='Enter username', example='UrbanUser')],
                    age: Annotated[int,Path(ge=18, le=120, description='Enter age', example='24')]):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

# Запуск  uvicorn module_16_2:app --reload