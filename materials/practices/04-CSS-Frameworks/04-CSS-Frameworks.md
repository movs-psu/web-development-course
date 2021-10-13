---
theme: gaia
paginate: true
backgroundColor: #fff
footer: Практика №4: CSS-Фреймворки / Курс Web-программирования 2021 / ПГНИУ
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

# **Практика №4: CSS-Фреймворки**

Web-программирование / ПГНИУ

---

## Верстать сложно

![bg right contain](img/css-sucks-griffin.gif)

Flex, Grid, адаптивность, кросс-браузерность, доступность... 

Бывает, что:
- Не требуется уникальный дизайн
- Интерфейс состоит из стандартных элементов
- Прототипирование, MVP

---

# CSS-фреймворк

**CSS фреймворк** (UI kit, UI фреймворк) - библиотека для быстрой вёрстки веб-страниц
- Готовые CSS стили, часто компоненты
- CSS файлы, иногда JS скрипты для интерактивных компонентов 
- Иногда следуют дизайн системе
- Часто имеет возможности конфигурирования, расширения, создания тем

---

# Примеры

- Классические:
  - ![h:1em](https://getbootstrap.com/docs/5.1/assets/img/favicons/favicon-32x32.png) **Bootstrap**
  - ![h:1em](https://getmdl.io/assets/android-desktop.png) Material Design Lite, ![h:1em](https://materializecss.com/images/favicon/favicon-32x32.png) MaterializeCSS
  - ![h:1em](https://get.foundation/assets/img/icons/foundation-favicon.ico) Zurb Foundation
  - ![h:1em](https://bulma.io/favicons/favicon-32x32.png?v=201701041855) Bulma
  - ![h:1em](https://semantic-ui.com/images/logo.png) Semantic UI
  - ![h:1em](https://getuikit.com/images/favicon.png) UIKit
- Микро-фреймворки: ![h:1em](https://purecss.io/img/favicon.ico) Yahoo PureCSS, ![h:1em](http://getskeleton.com/dist/images/favicon.png) Skeleton
- Utility-first: ![h:1em](https://tailwindcss.com/favicon-32x32.png) **Tailwind CSS**, ![h:1em](https://windicss.org/assets/logo.svg) Windi CSS, Tachyons

---

# Основные концепции

- Подключаются CSS и JS файлы библиотеки
- Предустановлены стили "типографии": шрифт, текст, ссылки и др.
- Стили макета: сетка, контейнер, колонки
- Стили различных **компонентов**, их частей и их модификаторов
- Утилитные классы - классы отвечающие за определённые свойства, а не компоненты:
  `.text-center`, `.d-block`, `.p-absolute`, `.bg-dark`
- Конфигурация через CSS переменные, препроцессоры или системы сборки

---

# ![h:1em](img/bootstrap-logo.png) Bootstrap

- Самый популярный CSS фреймворк долгие годы
- Стили страницы, сетка
- Компоненты
- Интерактивные компоненты, валидация форм
- Утилитные классы
- Широкая кастомизация
- Большая экосистема тем

---

![](img/bootstrap-grid.png)

```html
<div class="container">
    <div class="row">
        <div class="col">Column</div>
        <div class="col">Column</div>
        <div class="col">Column</div>
    </div>
</div>
```

---

![bg](black)
![bg cover](img/bootstrap-navbars.png)

---

![bg](black)
![bg cover](img/bootstrap-album.png)

---

![bg](black)
![bg cover](img/bootstrap-form.png)

---

![bg](black)
![bg cover](img/bootstrap-blog.png)

---

![bg](black)
![bg contain](img/bootstrap-moodle.png)

---

## ![h:1em](img/materializecss-logo.png) MaterializeCSS 

Реализует **дизайн систему** Material Design

![bg right w:100%](img/materializecss-1.png)

---

![bg](black)
![bg contain](img/materializecss-2.png)

---

![bg](black)
![bg contain](img/materializecss-3.png)

---

# ![h:1em](img/uikit-logo.png) UIKit

```html
<div uk-alert>
    <a class="uk-alert-close" uk-close></a>
    <h3>Notice</h3>
    <p>Lorem ipsum...</p>
</div>
```

![](img/uikit-1.png)

---

# ![h:1em](img/semantic-ui-logo.png) Semantic UI / Fomatic UI

```html
<div class="ui three buttons">
    <a class="ui active button"></a>
    <a class="ui button"></a>
    <a class="ui button"></a>
</div>
```

![](img/semantic-ui-1.png)

---

![bg](black)
![bg contain](img/semantic-ui-2.png)

---

![bg](black)
![bg contain](img/semantic-ui-3.png)

---
![bg](rgb(247,250,252))
## ![h:1em](img/tailwindcss-logo.png) Utility-first CSS framework

![](img/tailwind-css.png)

---

# ![h:1em](img/fontawesome.png)

- 1500+ бесплатных иконок (svg, font)
- Эффект, комбинации, модификаторы

```html
<i class="far fa-user"></i>
<span class="fa-stack fa-2x">
    <i class="fas fa-camera fa-stack-1x"></i>
    <i class="fas fa-ban fa-stack-2x" style="color: Tomato"></i>
</span>
```

![](img/fa-1.png) ![](img/fa-2.png)

---

![bg](#f8f9fa)
![bg contain](img/fa-blender-phone.png)

---

# Ссылки

- https://purecss.io, http://getskeleton.com
- https://getbootstrap.com
- https://getmdl.io, https://materializecss.com 
- https://getuikit.com 
- https://semantic-ui.com
- https://get.foundation
- https://bulma.io
- https://fontawesome.com 
- https://tailwindcss.com, https://windicss.org, https://tachyons.io

---

# Пример

![bg right contain](img/replit-example.png)

https://replit.com/@ShGKme/Web-Bootstrap