# Лабораторная работа № 5: API

> _Максимум 10 баллов. Часть контрольной точки 3._

## Задача

**Требуется реализовать API веб-cайта "Мини-почта".**

Спецификация доступна в формате **Swagger**:
- [swagger.json](https://minimail.web.shgk.me/swagger.json)
- [swagger.yml](https://minimail.web.shgk.me/swagger.yml)

Документация:
- [ReDoc UI](https://redocly.github.io/redoc/?url=https://minimail.web.shgk.me/swagger.json&nocors)
- [Swagger UI](https://petstore.swagger.io/?url=https://minimail.web.shgk.me/swagger.json)

## Критерии

- `1б` Реализован `GET /messages`
- `1б` Реализован `GET /messages/:messageID`
- `1б` Реализован `POST /messages`
- `1б` Реализован `POST /messages/:messageID/claps`
- `1б` Реализована валидация и проверка на существование сообщения
- `5б` Список сообщений хранится в БД и не теряется при перезапуске сервера