---
theme: gaia
paginate: true
backgroundColor: #fff
footer: Лекция №12: NodeJS / Курс Web-программирования 2020 / ПГНИУ
style: |
    section {
      font-family: "Open Sans", "Tahoma", "apple color emoji", "segoe ui emoji", "segoe ui symbol", "noto color emoji";
      font-size: 32px;
      letter-spacing: unset;
    }
    header,
    footer {
      font-size: 50%;
    }
    section::after {
      content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
    }
---

<!-- _class: lead -->

# **Лекция 12: NodeJS**

![w:500](https://nodejs.org/static/images/logos/nodejs-new-pantone-black.svg)

Web-программирование / ПГНИУ

---

# JavaScript

- Мульти-парадигменный (объектно-ориентированный, императивный, функциональный)
- Интерпретируемый (или JIT-компилируемый)
- Прототипно-ориентированный
- Событийно-ориентированный
- Динамическая слабая типизация
- Автоматическое управление памятью
- C-подобный синтаксис

---

# NodeJS

- **Node** или **Node.js** — программная платформа, основанная на движке V8, превращающая JavaScript из узкоспециализированного языка в язык общего назначения. (wikipedia)
- **NodeJS** – среда исполнения JavaScript и API для взаимодействия с ОС
- Позволяет писать на **JS** консольные утилиты, серверную часть, десктопные приложения, serverless и т.д.

---

# NodeJS для Full-Stack разработка

- Один язык
- Одна экосистема (npm, eslint и т.д.)
- Переиспользование кода
- SSR - Server-Side Rendering
- **Back-End For Frontend**

---

# NodeJS в нагруженном приложении

- За счёт асинхронности держит высокую нагрузку на I/O
- Отлично справляется с realtime приложениями
- Лёгкий runtime, легко масштабируется экземплярами приложения

---

# Проблемы NodeJS на Back-End

- Не для тяжёлых операций
- Молодой, экосистема развивается
    - Нет одного "default" фреймворка
    - Нет фреймворка, где всё, что можно из коробки
    - Все ОРМ не идеальные
    - Язык развивается быстрее библиотек

---

# Основные фреймворки

- Микрофреймворки
    - **Express**
    - Koa
    - Fastify
- Фреймворки
    - **Nest**
    - Loopback
    - Adonis

---

# Express

- Fast, unopinionated, minimalist web framework
- Самое популярное решение под NodeJS
- Микрофреймворк
- Основа - роутинг + посредники
- Посредник меняет объект запроса и ответа

---

# Express и экосистема

- express
- body-parser, multer
- express-session, cookie-parser
- passport
- csurf, helmet, morgan

---

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log(`Listening at http://localhost:${port}`);
});
```

---

# ![h:1em](https://docs.nestjs.com/assets/logo-small.svg) Nest

- Фреймворк, предоставляющий из коробки архитектуру для построения тестируемых, масштабируемых слабо-связанных и хорошо поддерживаемых приложений.
- Вдохновлён Angular (и переиспользует его модули)
- Работает как поверх Express, так и поверх Fastify
- DataBase Agnostic
- CLI
- TypeScript
- Rx.js

---

# ![h:1em](https://docs.nestjs.com/assets/logo-small.svg) Nest: основные компоненты

- **Контроллер** - HTTP роутинг
- **Сервис** - компонент, решающий бизнес-задачи
- **Провайдер** - поставщик услуги, внедряемый в другие компоненты приложения (DI)
- **Модуль** - основная единица структуры приложения

---

![bg contain](https://docs.nestjs.com/assets/Components_1.png)

---

```typescript
import { Injectable } from '@nestjs/common';
import { Cat } from './interfaces/cat.interface';

@Injectable()
export class CatsService {
  private readonly cats: Cat[] = [];

  create(cat: Cat) {
    this.cats.push(cat);
  }

  findAll(): Cat[] {
    return this.cats;
  }
}
```

---

![bg contain](https://docs.nestjs.com/assets/Controllers_1.png)

---

```typescript
import { Controller, Get, Post, Body } from '@nestjs/common';
import { CreateCatDto } from './dto/create-cat.dto';
import { CatsService } from './cats.service';
import { Cat } from './interfaces/cat.interface';

@Controller('cats')
export class CatsController {
  constructor(private catsService: CatsService) {}

  @Post()
  async create(@Body() createCatDto: CreateCatDto) {
    this.catsService.create(createCatDto);
  }

  @Get()
  async findAll(): Promise<Cat[]> {
    return this.catsService.findAll();
  }
}
```

---

![bg contain](https://docs.nestjs.com/assets/Modules_1.png)

---

```typescript
import { Module } from '@nestjs/common';
import { CatsController } from './cats.controller';
import { CatsService } from './cats.service';

@Module({
  controllers: [CatsController],
  providers: [CatsService],
})
export class CatsModule {}
```

---

# ![h:1em](https://docs.nestjs.com/assets/logo-small.svg) Nest: другие компоненты

- Модули для организации аутентификации и авторизации 
- Кэширование, валидация, конфигурация, логгирование
- GraphQL
- WebSockets (обёртки над socket.io и ws)
- Микросервисы: gRPC, Redis, MQTT, NATS, RabbitMQ, Kafka
- Генерация документации приложения
- Генерация Swagger документации API

---

![bg contain](https://docs.nestjs.com/assets/documentation-compodoc-1.jpg)

---

![bg contain](https://docs.nestjs.com/assets/swagger-cats.png)

---

# ORM

- Sequelize 
- TypeORM
- Objection
- Mikro-ORM

---

# Headless CMS

- Strapi
- Keystone

---

# Ссылки

- NodeJS: [https://nodejs.org/en/](https://nodejs.org/en/)
- [The Back-end for Front-end Pattern (BFF)](https://philcalcado.com/2015/09/18/the_back_end_for_front_end_pattern_bff.html)
- Express: [http://expressjs.com](http://expressjs.com)
- NestJS: [https://nestjs.com](https://nestjs.com)
- HolyJS 2018 Moscow | [Kamil Myśliwiec — Revealing framework fundamentals: NestJS behind the curtain](https://www.youtube.com/watch?v=jo-1EUxMmxc)
- Sequelize: [https://sequelize.org](https://sequelize.org)
- Objection: [https://vincit.github.io/objection.js/](https://vincit.github.io/objection.js/)
- Mikro-ORM: [http://mikro-orm.io](http://mikro-orm.io)
