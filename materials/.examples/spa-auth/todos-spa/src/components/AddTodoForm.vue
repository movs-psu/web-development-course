<template>
  <fieldset>
    <legend>Add todo</legend>
    <form @submit.prevent="handleSubmit">
      <p>
        <label> title: <input v-model="title" /> </label>
      </p>
      <button type="submit">Add</button>
    </form>
  </fieldset>
</template>

<script>
export default {
  name: 'AddTodoForm',

  data() {
    return {
      title: '',
    };
  },

  methods: {
    async handleSubmit() {
      try {
        const response = await fetch('/api/todos', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            title: this.title,
          }),
        });

        if (response.ok) {
          this.$emit('add-todo', await response.json());
          return;
        } else {
          alert(await response.text());
        }
      } catch (e) {
        alert(e.message);
      }
    },
  },
};
</script>

<style scoped></style>
