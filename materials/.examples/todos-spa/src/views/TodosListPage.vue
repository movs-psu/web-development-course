<template>
  <div>
    <h2>Todos List Page</h2>
    <ul v-if="todos">
      <li v-for="todo in todos" :key="todo.id">
        <router-link :to="`/todos/${todo.id}`">
          #{{ todo.id }}: {{ todo.title }}
        </router-link>
      </li>
    </ul>
    <div v-else>Todos are loading...</div>
  </div>
</template>

<script>
export default {
  name: 'TodosListPage',

  data() {
    return {
      todos: null,
    };
  },

  async mounted() {
    this.todos = await this.fetchTodos();
  },

  methods: {
    async fetchTodos() {
      try {
        const response = await fetch(
          'https://jsonplaceholder.typicode.com/todos',
        );
        if (response.ok) {
          return response.json();
        }
        return null;
      } catch (e) {
        alert(e.message);
      }
    },
  },
};
</script>

<style scoped></style>
