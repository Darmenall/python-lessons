import sqlite3
from random import randint


global db
global cur
db = sqlite3.connect('server.db')
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash INT
)""")
db.commit()


def reg():
    user_login = input('Login: ')
    user_password = input('Password: ')

    cur.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if cur.fetchone() is None:
        cur.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
        db.commit()
        print('Зарегистрировано!')
    else:
        print('Такая запись уже тмеется!')

        for value in cur.execute("SELECT * FROM users"):
            print(value)


def delete_db(user_login):
    cur.execute(f"DELETE FROM users WHERE login = '{user_login}'")
    db.commit()
    print('Запись удалена!')


def casino():
    user_login = input('Log in: ')
    number = randint(1, 2)

    # for i in cur.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
    #     balance = i[0]

    cur.execute(f"SELECT cash FROM users WHERE login = '{user_login}'")
    balance = cur.fetchone()[0]


    cur.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    db.commit()
    if cur.fetchone() is None:
        print('Такого логина не существует. Зарегистрируйтесь')
        reg()
    else:
        if number == 1:
            cur.execute(f'UPDATE users SET cash = {balance + 1000} WHERE login = "{user_login}"')
            db.commit()
        else:
            print("Вы проиграли!")
            delete_db(user_login=user_login)


def enter():
    for i in cur.execute('SELECT login, cash FROM users'):
        print(i)


def main():
    casino()
    enter()


main()
