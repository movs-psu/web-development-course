import Vue from 'vue';
import App from './App.vue';
import { router } from '@/router';
import { store } from './store';

Vue.config.productionTip = false;

async function initApp() {
  const response = await fetch('/api/me');

  if (response.ok) {
    store.user = await response.json();
  }

  new Vue({
    router,
    render: h => h(App),
  }).$mount('#app');
}

initApp().catch(e => alert(e.message));
