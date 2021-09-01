# TODO: Добавить проверку на уникальность пользователя и / или обработку ошибок БД

import sqlite3
from pathlib import Path
from werkzeug.security import check_password_hash, generate_password_hash
from ..entities import User, Todo

# Подключаемся к БД
db = sqlite3.connect(Path(__file__).parent / '..' / '..' / 'db' / 'database.sqlite', check_same_thread=False)


class Storage:

    @staticmethod
    def add_user(user):
        # Вместо пароля сохраняем хэш пароля
        # https://werkzeug.palletsprojects.com/en/0.16.x/utils/#werkzeug.security.generate_password_hash
        db.execute('INSERT INTO users (email, password) VALUES (?, ?)', (user.email, generate_password_hash(user.password)))
        db.commit()

    @staticmethod
    def get_user_by_email_and_password(email, password_hash):
        user_data = db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        # Не проверяем явно равенство паролей, а проверяем через его хэш
        # https://werkzeug.palletsprojects.com/en/0.16.x/utils/#werkzeug.security.check_password_hash
        if user_data and check_password_hash(user_data[2], password_hash):
            return User(*user_data)
        else:
            return None

    @staticmethod
    def get_user_by_id(user_id):
        user_data = db.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
        if user_data:
            return User(*user_data)
        else:
            return None

    @staticmethod
    def get_user_todos(user_id):
        todos = db.execute('SELECT id, title, user_id, done FROM todos WHERE user_id = ?', (user_id,)).fetchall()
        return map(lambda todo: Todo(*todo), todos)

    @staticmethod
    def add_todo(todo):
        todo_id = db.execute('INSERT INTO todos (title, user_id) VALUES (?, ?)', (todo.title, todo.user_id)).lastrowid
        db.commit()
        todo = db.execute('SELECT id, title, user_id, done FROM todos WHERE id = ?', (todo_id,)).fetchone()
        return Todo(*todo)

    @staticmethod
    def delete_todo(todo_id):
        db.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
        db.commit()
