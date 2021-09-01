<template>
  <form @submit.prevent="handleSubmit">
    <p>
      <label> Email: <input type="email" v-model="email" /> </label>
    </p>
    <p>
      <label> Password: <input type="password" v-model="password" /> </label>
    </p>
    <p>
      <label>
        Repeat password: <input type="password" v-model="repeatPassword" />
      </label>
    </p>
    <button type="submit">Register</button>
  </form>
</template>

<script>
export default {
  name: 'RegistrationPage',

  data() {
    return {
      email: '',
      password: '',
      repeatPassword: '',
    };
  },

  methods: {
    async handleSubmit() {
      // Валидация!
      try {
        const response = await fetch('/api/registration', {
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
          return this.$router.push('/login');
        } else {
          alert(await response.text());
        }
      } catch(e) {
        alert(e.message);
      }
    },
  },
};
</script>

<style scoped></style>
