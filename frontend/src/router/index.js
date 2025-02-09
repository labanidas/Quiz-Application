import { createRouter, createWebHistory } from 'vue-router';
import Register from '@/pages/Register.vue'; // Import the Register component

const routes = [
  {
    path: '/register', 
    name: 'Register',
    component: Register, 
  },
];

const router = createRouter({
  history: createWebHistory(), // Use the browser's history API for clean URLs
  routes,
});

export default router;
