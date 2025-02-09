import { createRouter, createWebHistory } from 'vue-router';
import Register from '@/pages/Register.vue'; 
import Login from '@/pages/Login.vue'; 
import Dashboard from '@/pages/Dashboard.vue'; 
import QuizExam from '@/pages/QuizExam.vue'; 

const routes = [
  {
    path: '/register', 
    name: 'Register',
    component: Register, 
  },
  {
    path: '/login', 
    name: 'Login',
    component: Login, 
  },
  {
    path: '/dashboard', 
    name: 'Dashboard',
    component: Dashboard, 
  },
  {
    path: '/quiz', 
    name: 'QuizExam',
    component: QuizExam, 
  },
];

const router = createRouter({
  history: createWebHistory(), // Use the browser's history API for clean URLs
  routes,
});

export default router;
