---
theme: gaia
paginate: true
backgroundColor: #fff
footer: Практика №4: UI-Фреймворки / Курс Web-программирования 2020 / ПГНИУ
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

# **Практика №4: UI-Фреймворки**

Web-программирование / ПГНИУ

---

## Верстать сложно

![bg right contain](img/css-sucks-griffin.gif)

Блочная модель, Flex, адаптивность, кросс-браузерность, доступность... 

Бывает, что:
- Не требуется уникальный дизайн
- Интерфейс состоит из стандартных элементов
- Прототипирование, MVP

---

# UI Фреймворки

- UI Фреймворк (UI kit, **CSS фреймворк**) - библиотека для быстрой вёрстки веб-страниц, готовые CSS стили и компоненты
- CSS файлы и иногда JS скрипты для интерактивных компонентов 
- Иногда следуют дизайн системе
- Часто имеет возможности конфигурирования, расширения и создания тем
    
---

# Примеры

- UI-фреймворки:
    - Twitter Bootstrap
    - Material, MaterializeCSS
    - Zurb Foundation
    - Bulma
    - Semantic UI
    - UIKit
- Микро-фреймворки: Yahoo PureCSS, Milligram
- CSS Utility: Tailwind CSS 

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

# ![h:1em](img/bootstrap-logo.png) Twitter Bootstrap 

```html
<div class="container">
    <div class="row">
        <div class="col"></div>
        <div class="col"></div>    
    </div>
</div>

<a class="btn btn-danger btn-lg"></a>
```

---

![bg](black)
![bg contain](img/bootstrap-1.png)

---

![bg](black)
![bg contain](img/bootstrap-2.png)

---

![bg](black)
![bg contain](img/bootstrap-3.png)

---

![bg](black)
![bg contain](img/bootstrap-4.png)

---

![bg](black)
![bg contain](img/bootstrap-5.png)

---

![bg](black)
![bg contain](img/bootstrap-6.png)

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

- https://purecss.io, https://milligram.io
- https://getbootstrap.com
- https://materializecss.com 
- https://getuikit.com 
- https://semantic-ui.com
- https://foundation.zurb.com
- https://bulma.io
- https://fontawesome.com 
- https://tailwindcss.com 
