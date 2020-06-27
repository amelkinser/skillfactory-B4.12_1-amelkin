##---------- B4.12 Домашнее задание № 1 --------------------------------------
##    Написать модуль users.py, который регистрирует новых пользователей
##    27.06.2020 г.
##    Группа: PWS-21.
##    Амелькин С.Б.
##----------------------------------------------------------------------------

# импортируем библиотеку sqlalchemy и некоторые функции из нее 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()

# Описывает структуру таблицы user для хранения регистрационных данных пользователей
class User(Base):
    
    # задаем название таблицы
    __tablename__ = 'user'

    # идентификатор пользователя, первичный ключ
    id = sa.Column(sa.INTEGER, primary_key=True)
    # имя 
    first_name = sa.Column(sa.Text)
    # фамилия 
    last_name = sa.Column(sa.Text)
    # пол
    gender = sa.Column(sa.Text)
    # адрес электронной почты 
    email = sa.Column(sa.Text)
    # День Рождения
    birthdate = sa.Column(sa.Text)
    #рост
    height = sa.Column(sa.Float)

# Устанавливает соединение к базе данных, создает таблицу,
# если её ещё нет и возвращает объект сессии 
def connect_db():
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанную таблицу
    Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()

# Запрашивает у пользователя данные и добавляет их в список users
def request_data():
    # выводим приветствие
    print("\nПожалуйста, введите свои данные")
    # запрашиваем у пользователя данные
    first_name = input("Имя: ")
    last_name = input("Фамилия: ")
    gender = input("Пол: ")
    email = input("e-mail: ")
    birthdate=input("День Рождения (ГГГГ-ММ-ДД): ")
    height = input("Рост (через точку): ")
    # создаем нового пользователя
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender, 
        email=email,
        birthdate=birthdate,
        height=height
    )
    # возвращаем созданного пользователя
    return user

# Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
def main():
    session = connect_db()
    # запрашиваем данные пользователя
    user = request_data()
    # добавляем нового пользователя в сессию
    session.add(user)
    # сохраняем все изменения, накопленные в сессии
    session.commit()
    print("Спасибо!!!")


if __name__ == "__main__":
    main()    
    
