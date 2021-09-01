import Vue from 'vue';
import VueRouter from 'vue-router';
import { store } from '@/store';

Vue.use(VueRouter);

export const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: () =>
        import(/* webpackChunkName: 'todos-page' */ '@/views/TodosListPage'),
      meta: {
        requireAuth: true,
      },
    },
    // {
    //   path: '/todos/:todoId(\\d+)',
    //   component: () =>
    //     import(/* webpackChunkName: 'todo-page' */ '@/views/TodoPage'),
    // },
    {
      path: '/login',
      component: () => import('@/views/LoginPage'),
    },
    {
      path: '/registration',
      component: () => import('@/views/RegistrationPage'),
    },
  ],
});

router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    if (store.user) {
      next();
    } else {
      next('/login');
    }
  } else {
    next();
  }
});
