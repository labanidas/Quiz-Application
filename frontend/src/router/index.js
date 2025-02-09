import { createRouter, createWebHistory } from 'vue-router';
import Register from '@/pages/Register.vue'; 
import Login from '@/pages/Login.vue'; 

const routes = [
  {
    path: '/register', 
    name: 'Register',
    component: Register, 
  },
  {
    path: '/Login', 
    name: 'Login',
    component: Login, 
  },
];

const router = createRouter({
  history: createWebHistory(), // Use the browser's history API for clean URLs
  routes,
});

export default router;
