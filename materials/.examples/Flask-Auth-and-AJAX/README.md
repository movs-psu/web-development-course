# Традиционное приложение с аутентификацией, формами и AJAX на Python (Flask)

**Попробовать онлайн:** https://repl.it/@ShGKme/Web-Flask-with-auth-and-AJAX

Простейшее традиционное веб-приложение на Python
- Микрофреймворк Flask
- БД: SQLite
- Простая аутентификация на client-side сессии
- Никаких библиотек, кроме Flask
- HTML шаблоны с Jinja2, HTML формы
- AJAX

## Подготовка

1. Установите Python 3 (https://www.python.org)
2. Установите Flask. В терминале введите: `pip install flask`. Библиотека будет установлена глобально.

Установить зависимости можно также командой `pip install -r requirements.txt`, будут глобально установлены все зависимости, перечисленные в файле `requirements.txt`.

Чтобы не устанавливать зависимости глобально, можно использовать различные библиотеки для создания виртуального окружения, например, [`virtualenv`](https://virtualenv.pypa.io/en/latest/) ([DEV.TO: Dead Simple Python: Virtual Environments and pip](https://dev.to/codemouse92/dead-simple-python-virtual-environments-and-pip-5b56)).

## Запуск приложения

### Как Python приложение

В терминале в этой директории выполните:
```bash
python main.py
```

### При помощи Flask

См. https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application  
https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/#run-the-application

## База Данных

Используется SQLite СУБД - маленькая встраиваемая реляционная SQL СУБД.

Файл с БД: `db/database.sqlite`.

Схема БД: `db/schema.sql`.

Для пересоздания БД по схеме требуется вызывать скрипт:
```bash
python recreate_db.py
```

## Что дальше?

Это некоторый минимальный пример, цель которого - показать основные концепции традиционной серверной части и её реализации на Flask с применением минимального  количества сторонних библиотек.

Желательно ещё добавить:
- Разделить приложение на части через модули [`blueprint`](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
- Добавить валидацию данных, которые приходят от пользователя
- Добавить обработку ошибок, как в приложении (не удалось создать пользователя в БД), так и разработчика (всё упало)
- Добавить модуль конфигурации. В идеале через ENV переменные

## Полезные ссылки

- [Документация Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Quickstart по Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- [Документация по использованию шаблонизатора](https://flask.palletsprojects.com/en/1.1.x/templating/)
- [Документация по шаблонизатору Jinja2](https://jinja.palletsprojects.com/en/2.11.x/templates/)
- [Документация по blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
- [UI фреймворк - Bootstrap](https://getbootstrap.com)
- [Иконки - Fontawesome](https://fontawesome.com)
