---
theme: gaia
paginate: true
backgroundColor: #fff
footer: Лекция №8: Современный Front-End / Курс Web-программирования 2020 / ПГНИУ
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

# **Лекция №8: Современный Front-End**

Web-программирование / ПГНИУ

---

## CSS-препроцессоры

- CSS препроцессоры – инструменты трансляции (пред-обработки) более высокоуровневых языков в CSS
- SASS (SCSS), LESS, Stylus
- Переменные, вычисления, переиспользование (миксины, модули), функции, условия, циклы и т.д.

![](img/less-logo.png) ![](img/sass-logo.png)

---

# PostCSS ![h:1em](img/postcss-logo.jpg)

- Программа, которая автоматизирует рутинные операции с CSS с помощью расширений, написанных на языке JavaScript.
- Конвейер для унифицированных плагинов, выполняющих некоторые операции с CSS
- **autoprefixer** – автоматически добавляет вендорные префиксы
- **postcss-preset-env** – позволяет писать на современном CSS
- **cssnano** – оптимизация и сжатие css

---

![](img/autoprefixer-1.png)
![bg right h:80%](img/autoprefixer-2.png)

---

![](img/cssnano-1.png)
![bg right w:80%](img/cssnano-2.png)

---

# PostHTML ![h:1em](img/posthtml-logo.png)

- Программа, которая автоматизирует рутинные операции с HTML с помощью расширений, написанных на языке JavaScript
- **posthtml-md**
- **posthtml-img-autosize**
- **posthtml-w3c**

---

# Babel ![h:1em](img/babel-logo.png)

- **JavaScript компилятор (транспайлер)**
- Toolchain для компиляции множеством плагинов
- **Транспайлер** — тип компилятора, который использует исходный код программы, написанной на одном языке программирования, в качестве исходных данных и производит эквивалентный исходный код на другом языке программирования
- Переводит современный JS в старый

---

![bg](black)
![bg contain](img/babel-example-1.png)

---

![](img/babel-example-2.png)
![bg right contain](img/babel-example-3.png)

---

# Другие языки

- TypeScript ![h:1em](img/typescript-logo.png)
- Dart
- Elm
- Reason
- Kotlin.js
- Scala.js

![bg right contain](img/typescript-example.png)

---

# Другие задачи

- Минификация - уменьшение размера кода
- Обфускация - запутывание кода
- Оптимизация кода - замена конструкций на более эффективные эквивалентные 

---

![](img/min-1.png)
![bg right auto](img/min-2.png)

---

# Browserslist ![h:1em](img/browserslist-logo.png)

- Как понять, в какую версию ES нам транспайлить код?
- Какие нужны полифилы? Префиксы в CSS?
- Нужно проверять всё на caniuse.com?

![](img/browserslist-example.png)

---

# Качество кода

**Линтер** – инструмент анализа кода, соблюдение стиля кода и поиска проблемных мест.
Самый популярный - **eslint** ![h:2em](img/eslint-logo.png) 

**Форматер** – инструмент, форматирующий код по определённым правилам.
Самый популярный - **prettier** ![h:2em](img/prettier-logo.png) 

---

# NodeJS

- Node или Node.js — программная платформа, основанная на движке V8, превращающая JavaScript из узкоспециализированного языка в язык общего назначения. (wikipedia)
- NodeJS – среда исполнения JavaScript и API для взаимодействия с ОС
- Позволяет писать на JS консольные утилиты, серверную часть, десктопные приложения, serverless и т.д.

![](img/nodejs-logo.png)

---

![bg](black)
![bg contain](img/mem-1.png)

---

# Проблема управлением зависимостями

- Есть куча библиотек, каждую надо найти на её сайте (вспомнив или найдя сайт) и скачать / подключить 
- Иногда надо проверять, а не вышла ли новая версия
- Обновили – всё сломалось, ведь какой-то другой библиотеке была нужна обязательно старая версия
- Решение - управление зависимостями через пакетный менеджер

---

# ![h:1em](img/npm-logo.png) npm
- **NodeJS Package Manager**
- Приложение = пакет. Его описание хранится в `package.json`
    - `scripts` - различные скрипты, команды, использующиеся при разработке пакета
    - `dependencies` - зависимости
    - `devDependencies` - зависимости для разработки
- `node_modules` - директория, в которой хранятся установленные зависимости

---

# Команды npm

```bash
# Основные команды
$ npm init`
$ npm install
$ npm install <package> [ <package>]
$ npm install --save-dev <package> [ <package>]
$ npm install --global <package>
$ npm uninstall <package> [ <package>]
$ npm run <script name>
$ npx <bin>

# Алиасы
npm i === npm install
npm i -D == npm install --save-dev
npm i -g == npm install --global
npm start === npm run start
```

---

![bg](white)
![bg contain](img/node_modules-mem-6.png)

---

![bg](black)
![bg contain](img/node_modules-mem-1.png)

---

![bg](white)
![bg contain](img/node_modules-mem-2.png)

---

![bg](black)
![bg contain](img/node_modules-mem-3.png)

---

![bg](black)
![bg contain](img/node_modules-mem-4.png)

---

![bg](black)
![bg contain](img/node_modules-mem-5.png)

---

# Запуск задач

- Системы автоматизации задач
- `$ gulp js`

![](img/gulp-logo.png)

![bg right contain](img/gulp-example.png)

---

# Webpack ![h:1em](img/webpack-logo.png)

- Сборщик модулей JavaScript приложения
- Не только js модулей, но и других зависимостей приложения
- Исследование графа зависимостей, разделение бандла на части (chunks), TreeShaking
- webpack-dev-server
    - Локальный сервер с хостингом файлов
    - Прокси к API
    - Hot Module Replacement

---

![bg contain](img/webpack-example-1.png)

---

# Правила (rules)

Правило определяется файлами, на которые оно действует (test) и списком загрузчиков (use), которые обрабатывают файлы

![](img/webpack-example-2.png)

---

# Загрузчики (loaders)

- style-loader, css-loader
- less-loader, sass-loader, postcss-loader
- babel-loader, ts-loader
- json-loader, file-loader, csv-loader
- posthtml-loader
- eslint-loader

---

# Плагины

Переиспользуемые модули, имеющие ту же систему конфигурации, что и сам webpack

- clean-webpack-plugin
- mini-css-extract-plugin
- hot-module-replacement-plugin
- uglifyjs-webpack-plugin

---

```jsx
/* JSX */

class TodoApp extends React.Component {
  //...
  render() {
    return (
      <div>
        <h3>Список дел</h3>
        <TodoList items={this.state.items} />
        <form onSubmit={this.handleSubmit}>
          <label htmlFor="new-todo"> Что нужно сделать? </label>
          <input id="new-todo" onChange={this.handleChange} value={this.state.text} />
          <button> Добавить #{this.state.items.length + 1}</button>
        </form>
      </div>
    );
  }
}

class TodoList extends React.Component {
  render() {
    return (
      <ul>
        {this.props.items.map(item => (
          <li key={item.id}>{item.text}</li>
        ))}
      </ul>
    );
  }
}
```

---

![bg contain](img/sfc.png)

---

# Source Map

Специальные файлы, которые позволяют в процессе разработки и отладки соотносить исполняемый код и исходный код.

---

# Ссылки: интересные статьи

- Каково оно учить JavaScript в 2016:  
[https://habr.com/ru/post/312022/](https://habr.com/ru/post/312022/)
- Объясняем современный JavaScript динозавру:  
[https://habr.com/ru/company/mailru/blog/340922/](https://habr.com/ru/company/mailru/blog/340922/)

---

# Ссылки: доклады

- HolyJS 2017 Moscow | Михаил Башуров – Yarn, npm v5 или pnpm — кто круче?  
[https://www.youtube.com/watch?v=hq-gIihAs5A](https://www.youtube.com/watch?v=hq-gIihAs5A)
- HolyJS 2017 Moscow | Модульный CSS — Андрей Оконечников:  
[https://www.youtube.com/watch?v=vYmSYsj-s5w](https://www.youtube.com/watch?v=vYmSYsj-s5w) 
- HolyJS 2018 Moscow | Стас Курилов — Глубокое погружение в webpack:  
[https://www.youtube.com/watch?v=aiYkJOPD9v8](https://www.youtube.com/watch?v=aiYkJOPD9v8)
- HolyJS 2019 Moscow | Nicolò Ribaudo — @babel/how-to:  
[https://www.youtube.com/watch?v=UeVq_U5obnE](https://www.youtube.com/watch?v=UeVq_U5obnE)

---

# Ссылки: инструменты

- NodeJS: [https://nodejs.org/](https://nodejs.org/)
- NPM: [https://www.npmjs.com/](https://www.npmjs.com/)
    - Документация по package.json: [https://docs.npmjs.com/configuring-npm/package-json.html](https://docs.npmjs.com/configuring-npm/package-json.html)
    - Документация по CLI: [https://docs.npmjs.com/cli-documentation/cli](https://docs.npmjs.com/cli-documentation/cli)
- LESS, SASS: [http://lesscss.org/](http://lesscss.org/), [https://sass-lang.com/](https://sass-lang.com/)
- PostCSS: [https://postcss.org/](https://postcss.org/), [https://github.com/postcss/postcss](https://github.com/postcss/postcss)
- Babel: [https://babeljs.io/](https://babeljs.io/)

---

# Ссылки: инструменты

- Browserslist: [https://github.com/browserslist/browserslist](https://github.com/browserslist/browserslist), [https://browserl.ist/](https://browserl.ist/)
- Webpack: [https://webpack.js.org/](https://webpack.js.org/)
- Webpack DevServer: [https://webpack.js.org/configuration/dev-server/](https://webpack.js.org/configuration/dev-server/)
- ESLint: [https://eslint.org/](https://eslint.org/)
- Prettier: [https://prettier.io/](https://prettier.io/)
- core-js: [https://www.npmjs.com/package/core-js](https://www.npmjs.com/package/core-js)
