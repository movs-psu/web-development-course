<template>
  <div id="app">
    <nav v-if="!user">
      <router-link to="/login">Login</router-link> |
      <router-link to="/registration">Registration</router-link>
    </nav>
    <nav v-else>
      {{ user.email }}
      <button @click="logout">Logout</button>
    </nav>
    <header>
      <h1>Todos SPA</h1>
    </header>
    <hr />
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
import { store } from '@/store';

export default {
  name: 'App',

  computed: {
    user() {
      return store.user;
    },
  },

  methods: {
    async logout() {
      try {
        const response = await fetch('/api/logout', {
          method: 'POST',
        });
        if (response.ok) {
          location.reload();
        } else {
          alert(await response.text());
        }
        return null;
      } catch (e) {
        alert(e.message);
      }
    },
  },
};
</script>

<style></style>
