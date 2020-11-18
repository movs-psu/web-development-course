---
theme: gaia
paginate: true
backgroundColor: #fff
footer: Лекция №10: Vue / Курс Web-программирования 2020 / ПГНИУ
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

# **Лекция №10: Vue**

![](https://vuejs.org/images/logo.png)

Web-программирование / ПГНИУ

---

# Vue

* Open-Source JavaScript Framework
* Progressive JavaScript Framework
* Фреймворк для разработки интерфейса веб-приложений на принципах реактивности и одностраничных приложений
 
---

# История

- Разработан **Even You** в **2013** году
- Эван Ю был сотрудником Google и работал над **Angular.js**
- Основными фреймворками были большие **Angular.js** и **Blackbone.js** 
- **React** вышел в 2013 году и был на ранней стадии
- Не было простого фремворка для быстрой разработки, прототипирования, миграций
- В **2015** вышла версия **1.0**, а в **2016** версия **2.0**, основная на сегодня
- В **2020** начал выходить **Vue 3**

---

# Экосистема Vue

* Vue - не фреймворк в привычном смысле
* Vue масштабируется от **небольшой подключаемой к странице библиотеки** до **фреймворка** для создания SPA приложений
    - `vue-router` - роутинг в SPA
    - `vuex` - центральное Flux хранилище
    - `Vue/CLI` - прототипирование, сборка и разработка
    - `vue-dev-tools`- инструменты разработки в браузере
    - `vue-ssr` - серверный рендеринг
    - `vue-test-utils` - тестирование

--- 

# Vue.js

* Реализует MVVM в компонентном подходе
* Компонент имеет данные (состояние)
* Компонент имеет шаблон
* Vue рендерит компонент по шаблону
* При изменении данные компонент автоматически ререндерится
* Эффетикный ререндеринг на основе **VirtualDOM**

---

```javascript
// Компонент описывается его опциями
const App = {
  // Шаблон компонента
  template: `<ul>
    <li v-for="todo in doneTodos">{{ todo.title }}</li>
  </ul>`,
    
  // Данные состояния приложения (реактивные)
  data: () => ({
    todos: [{ title: 'Task 1', done: true }],  
  }),
  
  // Вычисляемые свойства, значение которых вычисляется на основе других свойств
  computed: {
    doneTodos() {
      return this.todos.filter(todo => todo.done);
    }
  },
  
  // Различные методы: обработчики событий и другие функции
  methods: {
    handleClick() {},
    loadTodos() {},
  },
};

// Создаём приложение на корневом компоненте и монтируем на страницу в #app
new Vue(App).$mount('#app');
```

---

# Реактивность

* Работает за счёт переопределения свойств объектов с геттерами и сеттерами, а также патчинга прототипа массива
* Геттеры помогают определять зависимости в приложении
* Сеттеры позволяют реагировать на изменение значений
* ```javascript
  this.todos.push(newTodo);
  this.todos[0].title = 'New Title';
  this.todos = newTodosList;
  ```

---

# Шаблон

- Описывает узлы компонента в привязке к его данным
- Вывод выражений в содержимом узлов через ``{{ expression }}``
- Определение поведения узлов через директивы `v-*`
- Компилируется в render функцию с помощью `vue-template-compiler` на этапе сборки или в браузере
---

# Выражения
```html
<!-- Вывод содержимого узлов -->

<p>{{ propertyFromData }}</p>
<p>{{ todos }}</p>
<p>{{ todos[0].title + '!' }} - {{ todos[1].title + '!' }}</p>
<p>{{ new Date(todos[0].date).toLocalDateString() }}</p>
```
---

# Директивы ветвления
```html
<div v-if="x === 1">X is 1</div>
<div v-else-if="x === 2">X is 2</div>
<div v-else>X is not 1 or 2</div>
``` 
---

# Директива цикла
```html
<p v-for="item in list">
  <b>{{ item }}</b>
</p>

<p v-for="(item, index) in list">
  <b>{{ index }}:</b> {{ item }}
</p>

<p v-for="(value, key) in object">
  <b>{{ key }}:</b> {{ value }}
</p>
```

---

# Привязка значений

```html
<!-- Значение атрибута привязываетсяк значению выражения -->
<a v-bind:href="todo.link">{{ todo.title }}</a>

<!-- Короткая форма -->
<a :href="todo.link">{{ todo.title }}</a>

<!-- JS выражение, а не просто свойство -->
<a :href="'/todos/' + todo.id">{{ todo.title }}</a>

<!-- С классами и стилями есть особые удобные формы -->
<div :class="['class1', todo.class]">{{ todo.title }}</div>
<div :class="{ 'todo__done': todo.done }">{{ todo.title }}</div>
<div :style="{ color: todo.color }">{{ todo.title }}</div>
```

---

# Обработка событий

```html
<!-- handler - методы компонента -->
<button v-on:click="handler">Click Me!</button>

<!-- Короткая форма --> 
<button @click="handler">Click Me!</button>

<!-- Обработчик - не только метод, но и JS выражение -->
<!-- $event - полезная нагрузка события --> 
<button @click="deleteTodo(todo.id)">Delete Todo</button>
<input @change="todo.text = $event.target.value">Delete Todo</input>

<!-- Модификаторы события -->
<form @submit.prevent="submitForm">...</input>
```

---

# Двусторонняя привязка - модель

```html
<!-- Значение поля ввода определяется свойством text -->
<!-- При вводе оно обновляется -->
<input :value="text" @input="text = $event.target.value" />

<!-- Коротка форма - директива модели -->
<input v-model="text" />
```

---

# Формы

```html
<!-- Boolean -->
<input type="checkbox" v-model="todo.done"> Done? 

<!-- Array -->
<input type="checkbox" v-model="selectedFruits" value="apple"> Apple
<input type="checkbox" v-model="selectedFruits" value="banana"> Banana

<input type="radio" v-model="selectedFruit" value="apple"> Apple
<input type="radio" v-model="selectedFruit" value="banana"> Banana

<textarea v-model="text"></textarea>

<select v-model="selectedFruit">
  <option value="apple">Apple</option>
  <option value="banana">Banana</option>
</select>
```

---

# Компоненты

* В компонентном подходе приложение представляется как иерархия компонентов
* После регистрации компонент в шаблоне используется, как новый элемент 

---

![bg contain](https://vuejs.org/images/components.png)

---
```javascript
const PageTitle = {
  template: '<h1>Title!</h1>',
};

const App = {
  template: `<div>
    <main-logo />
    <the-title />
  </div>`,
  
  // Локальная регистрация
  components: {
    // Имя компонента : Реализация компонента
    TheTitle: PageTitle,
  },
};

// Глобальная регистрация
Vue.component('main-logo', {
  template: '<img src="main-logo.jpeg" />',
});
```

---

# Взаимодействие компонентов

* Компонент имеет входные параметры
* В компонент можно передавать содержимое
* Компонент может порождать события (Event Emitter)
* Родитель может подписываться на эти события
* **One-way dataflow** - данные передаются от дочернему компоненту; дочерний компонент не меняет эти, а только сообщает о такой необходимости

---

```javascript
const TodoItem = {
  template: `<div class="todo" :class="{ 'todo__done': done }">
    {{ title }} 
    <button @click="handleDoneClick">Done</button> 
  </div>`,

  // Описываем входные параметры
  props: {
    done: {
      type: Boolean,
      default: false,
    },
    title: {
      type: String,
      required: true,
    },
  },
  
  methods: {
    handleDoneClick() {
      // Сообщаем родителю о том, что тудушке поменяли статус выполнения
      this.$emit('toggle-done', !this.done); 
    },
  },
};
```

---

```javascript
const app = {
  template: `<todo-item 
                :title="todo.item"
                :done="todo.done"
                @toggle-done="todo.done = $event"
             />`,

  components: { TodoItem },

  data: () => ({
    todo: { title: 'title', done: false }
  }),
};
```

---

# Слоты 

```javascript
// В карточку можно передать содержимое
const SimpleCard = {
  template: `<div class="card">
    <slot></slot>
  </div>`,
};

// Содержимое - любая разметка (шаблон)
const App = {
  template: `<simple-card>
    <h3>Title</h3>
    <p>Text</p>
  </simple-card>`,

  components: { SimpleCard },
};
```

---

```javascript
// Может быть несколько слотов с разными именами
const ComplexCard = {
  template: `<div class="card">
    <header class="card-header">
      <slot name="header"></slot>
    </header>
  
    <div class="card-body">
      <slot></slot>
    </div>
  </div>`,
};

// Передаются через <template> и дериктиву v-slot:slotName
// Короткая запись #slotName
// Имя слота по умолчанию - default
const App = {
  template: `<complex-card>
    <template v-slot:header>
      <h3>Title</h3>
    </template>
  
    <template #default>
      <div>Content</div>
    </template>
  </complex-card>`,

  components: { ComplexCard },
};
```

---

# SPA: vue-router

* `vou-router` позволяет легко реализовать SPA на Vue
* Создаётся конфиг роутера, где определяются все маршруты и компоненты, которые за них отвечают
* В компоненте `<router-view>` выводится компонент текущего маршрута
* Для программного перехода между маршрутами вместо ссылок используются компоненты `<router-link to="/todos">Todos</router-link>`
* К роутеру можно обращаться программно через `this.$router` или прямым импортом, а к текущему маршруту через `this.$route` 

---

# vue-router: другие возможности

* Работает как с `hash`, так и на основе `HTML5 History API`
* Маршруты могут быть вложенными в иерархию
* У маршрута может быть несколько компонентов
* У маршрутов могут быть guard-ы, определяющие, можно ли переходить, и выполняющие подготовительные действия до перехода

---

```javascript
const App = {
  template: `<div>
    <nav>
      <router-link to="/todos">Todos List</router-link>
      <router-link to="/todos/1">First Todo</router-link> 
    </nav>
    <router-view />
  </div>`,
};

const router = new VueRouter({
  mode: history,
  routes: [
    {
      path: '/todos',
      component: TodosPageComponent,
    },
    {
      path: '/todos/:id',
      component: TodoPageComponent,
    },
  ],
});
```

---

# Vuex

* Центральное хранилище - источник истиности состояния приложения
* Реализует Flux архитектуру
* Глобальное состояние реактивное, как и данные компонентов Vue
* Глобальное состояние меняется через диспетчер путём применения синхронных мутаций
* Хранилище описывается состоянием, мутациями, геттерами и действиями (асинхронными функциями для сложных действий)
* Хранилище разбивается на модули

---

![bg contain](https://vuex.vuejs.org/vuex.png)

---

# vue-dev-tools

* Расширение браузера для разработки на Vue
* Дерево компонентов и их параметры
* События компонентов
* Хранилище и история его изменения
* Производительность

---

![bg contain](https://raw.githubusercontent.com/vuejs/vue-devtools/dev/media/screenshot-shadow.png)

---

# SFC

- Single-File-Component - Однофайловые компоненты
- Возможность описать в одном файле отдельно шаблон, скрипт и инкапсулированные стили компонента
- Работает при сборке через `vue-loader` 

---

![bg contain](https://vuejs.org/images/vue-component.png)

---

# Vue/cli

1) Генерация новых проектов по шаблонам: не просто один шаблон проекта, а интерактивный инструмент с выбором нужных компонентов и генерация на основе плагинов, в том числе в уже созданном проекте
2) Сборка и разработка приложения:
    - `vue-cli-service` - обёртка над `Webpack` с хорошим Production-ready конфигом
    - Сборка как веб-приложения, так и библиотеки с Vue-компонентом или Web-компонентом
3) **Vue UI** - графический интерфейс для создания и сборки проектов

---

# SSR

- Серверный рендеринг предусмотрен из коробки.
- Компоненты можно рендерить на стороне сервера
- Полная реализация приложения с SSR трудоёмкая, но есть готовые фреймворки над Vue, например, `Nuxt`

---

# Сильные стороны

* Достаточно простой для освоения
* Эффективная и простая реактивность
* Элегантные шаблоны
* Быстрое прототипирование
* Подходит как для использования у существующих проектах и миграции, так и для разработки с нуля

---

# Слабые стороны

* Очень плохая поддержка TypeScript
* Есть сложности с переиспользованием логики
* "Микрофреймворк". не даёт архитектуру приложения
* Разные подходы в сообществе для решения одних и тех же задач

---

# Vue 3

* Переписан на TypeScript и должен его лучше поддерживать
* Новая эффективная реактивность на основе `Proxy`
* Новый эффективный ренедринг
* Новый подход к переиспользованию логики на основе Composition API

---

# Ссылки

- Vue: https://vuejs.org
- Vue/Cli: https://cli.vuejs.org
- Vue Router: https://router.vuejs.org
- Vuex: https://vuex.vuejs.org
- vue-dev-tools: https://github.com/vuejs/vue-devtools
- vue-ssr: https://ssr.vuejs.org
- vue-test-utils: https://vue-test-utils.vuejs.org
- vue-loader: https://vue-loader.vuejs.org/
- Nuxt: https://nuxtjs.org
