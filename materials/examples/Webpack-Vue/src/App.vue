<template>
  <div id="app">
    <h1>{{ title + '!' }}</h1>
    <filter-form v-model="filterText" />
    <todo-list
      :todos="filteredTodos"
      @toggle="filteredTodos[$event.index].done = $event.done"
    />
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue';
import FilterForm from './components/FilterForm.vue';

export default {
  components: {
    TodoList,
    FilterForm,
  },

  data() {
    return {
      filterText: '',
      title: 'Hello, PSU',
      todos: [
        { title: 'Do HW', done: false, color: 'red' },
        { title: 'Feed a cat', done: true, color: 'green' },
        { title: 'Prepare for a lecture', done: false, color: 'green' },
      ],
    };
  },

  computed: {
    filteredTodos() {
      return this.todos.filter((todo) => todo.title.includes(this.filterText));
    },
  },
};
</script>

<style></style>
