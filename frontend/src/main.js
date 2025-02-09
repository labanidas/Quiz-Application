// src/main.js
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import './style.css'
import VueToast from 'vue-toast-notification';  
import 'vue-toast-notification/dist/theme-sugar.css';

const app = createApp(App);

// Install Pinia as a plugin
app.use(createPinia());

app.use(VueToast);

app.mount('#app');
