<template>
  <div>
    <h2>Todos List Page</h2>

    <add-todo-form @add-todo="handleAddTodo" />

    <hr />

    <ul v-if="todos">
      <li v-for="todo in todos" :key="todo.id">
        <div :to="`/todos/${todo.id}`">
          #{{ todo.id }}: {{ todo.title }}
          <button type="button" @click="deleteTodo(todo.id)">X</button>
        </div>
      </li>
    </ul>
    <div v-else>Todos are loading...</div>
  </div>
</template>

<script>
import AddTodoForm from "@/components/AddTodoForm";

export default {
  name: 'TodosListPage',

  components: { AddTodoForm },

  data() {
    return {
      todos: null,
    };
  },

  async mounted() {
    this.todos = (await this.fetchTodos()).todos;
  },

  methods: {
    async fetchTodos() {
      try {
        const response = await fetch('/api/todos');
        if (response.ok) {
          return response.json();
        } else {
          alert(await response.text());
        }
        return null;
      } catch (e) {
        alert(e.message);
      }
    },

    async deleteTodo(todoId) {
      try {
        const response = await fetch(`/api/todos/${todoId}`, {
          method: 'DELETE',
        });
        if (response.ok) {
          const index = this.todos.findIndex(todo => todo.id === todoId);
          this.todos.splice(index, 1);
        } else {
          alert(await response.text());
        }
        return null;
      } catch (e) {
        alert(e.message);
      }
    },

    handleAddTodo(todo) {
      this.todos.push(todo);
    },
  },
};
</script>

<style scoped></style>
