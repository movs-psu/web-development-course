<template>
  <section>
    <h2>Todo Page</h2>
    <template v-if="todo">
      <h3>#{{ todo.id }}: {{ todo.title }}</h3>
      <p>{{ todo.description }}</p>
    </template>
    <div v-else>Todo is loading</div>
  </section>
</template>

<script>
export default {
  name: 'TodoPage',

  data() {
    return {
      todo: null,
    };
  },

  async mounted() {
    this.todo = await this.fetchTodo(this.$route.params.todoId);
  },

  methods: {
    async fetchTodo(id) {
      try {
        const response = await fetch(
          `https://jsonplaceholder.typicode.com/todos/${id}`,
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
