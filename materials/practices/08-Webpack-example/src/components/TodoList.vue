<template>
  <ul>
    <todo-list-item
      v-for="(todo, index) in todos"
      :todo="todo"
      @toggle="$emit('toggle', { done: $event, index })"
      :key="todo.title"
    />
  </ul>
</template>

<script>
import TodoListItem from './TodoListItem.vue';

export default {
  components: {
    TodoListItem,
  },

  props: {
    todos: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped></style>
