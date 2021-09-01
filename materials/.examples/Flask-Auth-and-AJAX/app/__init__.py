from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from .entities import User, Todo
from .storage import Storage

# Создаём приложение
app = Flask(__name__)

# Конфигурируем
# Устанавливаем ключ, необходимый для шифрования куки сессии
app.secret_key = b'super-secret-key'


# Статичные файлы (css, js) доступны по /static
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files


# Описываем основные маршруты и их обработчики
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing


# Главная страница
@app.route('/')
def home():
    # Пользователя получаем из сессии
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions
    # Здесь сессия - это зашифрованные данные, хранящиеся в куках. Так эти данные есть во всех запросах этого сеанса.
    # Хотя можно работать с куки напрямую
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies
    if 'user_id' in session:
        user_id = session['user_id']
        # Получили пользователя из БД по ID
        user = Storage.get_user_by_id(user_id)
        # Ренедрим страницу по шаблону
        # https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
        # https://jinja.palletsprojects.com/en/2.10.x/templates/
        return render_template('pages/index.html', user=user)
    else:
        # Если пользователь не авторизован - перебрасываем на login
        return redirect('/login')


# Страница с формой входа
@app.route('/login', methods=['GET'])
def login():
    # Если пользователь уже авторизован, перебросим на главную
    if 'user_id' in session:
        return redirect('/')
    return render_template('pages/login.html', page_title='Flask App')


# Обработка формы входа (не обязательно та же страница, но в этом случае так удобно вернуть ошибку)
# Шаблон с формой логина будет иметь не только форму, но и место для вывода ошибок
@app.route('/login', methods=['POST'])
def login_action():
    page_title = 'Вход | Flask App'

    # Введённые данные получаем из тела запроса
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data
    # Но сначала проверяем, что они вообще есть
    if not request.form['email']:
        return render_template('pages/login.html', page_title=page_title, error="Требуется ввести Email")
    if not request.form['password']:
        return render_template('pages/login.html', page_title=page_title, error="Требуется ввести пароль")

    # Ищем пользователя в БД с таким email и паролем
    user = Storage.get_user_by_email_and_password(request.form['email'], request.form['password'])

    # Неверный пароль
    if not user:
        return render_template('pages/login.html', page_title=page_title, error="Неверный пароль")

    # Сохраняем пользователя в сессии
    session['user_id'] = user.id

    # Перенаправляем на главную страницу
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/#redirects-and-errors
    # Перенаправлять можно не только по URL, но и по имени роута
    return redirect(url_for('home'))


# Форма регистрации
@app.route('/registration', methods=['GET'])
def registration():
    return render_template('pages/registration.html', page_title='Регистрация | Flask App')


# Обработка формы регистрации
@app.route('/registration', methods=['post'])
def registration_action():
    page_title = 'Регистрация | Flask App'
    error = None
    # Проверяем данные
    if not request.form['email']:
        error = "Требуется ввести Email"
    if not request.form['password']:
        error = "Требуется ввести пароль"
    if not request.form['password2']:
        error = "Требуется ввести повтор пароля"
    if request.form['password'] != request.form['password2']:
        error = "Пароли не совпадают"
    # В случае ошибки рендерим тот же самый шаблон, но с текстом ошибки
    if error:
        return render_template('pages/registration.html', page_title=page_title, error=error)
    # Добавляем пользователя
    Storage.add_user(User(None, request.form['email'], request.form['password']))
    # Делаем вид, что добавление всегда без ошибки
    # Перенаправляем на главную
    return redirect(url_for('home'))


# Выход пользователя
@app.route('/logout')
def logout():
    # Просто выкидываем его из сессии
    session.pop('user_id')
    return redirect(url_for('home'))


# Страница со списком тудушек
@app.route('/todos')
def todos():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = Storage.get_user_by_id(session['user_id'])
    todos = Storage.get_user_todos(user.id)
    return render_template('pages/todos.html', page_title='Тудушки | Flask App', user=user, todos=todos)


# Добавление тудушки обычной HTML формой
@app.route('/todos', methods=['POST'])
def add_todo():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = Storage.get_user_by_id(session['user_id'])
    Storage.add_todo(Todo(None, request.form['title'], user.id, None))
    todos = Storage.get_user_todos(user.id)
    return render_template('pages/todos.html', page_title='Тудушки | Flask App', user=user, todos=todos)


# API для добавление тудушки для AJAX
@app.route('/api/todos', methods=['POST'])
def add_todo_api():
    # Теперь в случае ошибок не выводим её на странице или перенаправляем, а возвращаем ошибку
    # 401 - Unauthorized
    if 'user_id' not in session:
        return 'Not authorized!', 401
    todo = Storage.add_todo(Todo(None, request.json['title'], session['user_id'], None))
    # Возвращаем данные, сериализованные в JSON
    # jsonify преобразует словарь в JSON и устанавливает заголовки Content-Type: application/json
    return jsonify(todo.__dict__)


# API для удаления тудушки для AJAX
# Маршрут с параметром. Параметр маршрута придёт в обработчик параметром функции
# В отличие от форм, через AJAX можно отправлять не только GET и POST запросы
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if 'user_id' not in session:
        return 'Not authorized!', 401
    Storage.delete_todo(todo_id)
    # Не возвращаем ничего, 200 - успешный ответ
    return '', 200
