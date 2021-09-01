<template>
  <form @submit.prevent="handleSubmit">
    <p>
      <label> Email: <input type="email" v-model="email" /> </label>
    </p>
    <p>
      <label> Password: <input type="password" v-model="password" /> </label>
    </p>
    <button type="submit">Login</button>
  </form>
</template>

<script>
import { store } from '@/store';

export default {
  name: 'LoginPage',

  data() {
    return {
      email: '',
      password: '',
    };
  },

  methods: {
    async handleSubmit() {
      // Валидация!
      try {
        const response = await fetch('/api/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password,
          }),
        });

        if (response.ok) {
          store.user = await response.json();
          return this.$router.push('/');
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
