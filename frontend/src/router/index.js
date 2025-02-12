// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/store/useAuthStore';
import Register from '@/pages/Register.vue'; 
import Login from '@/pages/Login.vue'; 
import Dashboard from '@/pages/Dashboard.vue'; 
import QuizExam from '@/pages/QuizExam.vue'; 
import Home from '@/pages/Home.vue'; 
import Page1 from '@/pages/Page1.vue'; 
import Page2 from '@/pages/Page2.vue'; 

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home, 
  },
  {
    path: '/register', 
    name: 'Register',
    component: Register, 
    beforeEnter: async (to, from, next) => {      
      const authStore = useAuthStore();
      // await authStore.checkAuth();  
      if (authStore.authUser) {
        next('/dashboard'); 
      } else {
        next(); 
      }
    }
  },
  {
    path: '/login', 
    name: 'Login',
    component: Login, 
    beforeEnter: async (to, from, next) => {  
      const authStore = useAuthStore();
      // await authStore.checkAuth();  
      if (authStore.authUser) { 
        next('/dashboard'); 
      } else {
        next(); // Otherwise, stay on login page
      }
    }
  },
  {
    path: '/dashboard', 
    name: 'Dashboard',
    component: Dashboard, 
    beforeEnter: async (to, from, next) => {
      const authStore = useAuthStore();
      // await authStore.checkAuth(); // Ensure the auth check is done
      if (!authStore.authUser) {
        next('/login'); 
      } else {
        next();
      }
    }
  },
  {
    path: '/quiz', 
    name: 'QuizExam',
    component: QuizExam, 
    beforeEnter: async (to, from, next) => {
      const authStore = useAuthStore();
      await authStore.checkAuth(); // Ensure auth check is done
      if (!authStore.authUser) {
        next('/login');
      } else {
        next();
      }
    }
  },
  {
    path: '/p1', 
    name: 'Page1',
    component: Page1, 
  },
  {
    path: '/p2', 
    name: 'Page2',
    component: Page2,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
