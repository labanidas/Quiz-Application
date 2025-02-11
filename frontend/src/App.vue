<script setup>
import { useAuthStore } from '@/store/useAuthStore';
import { onMounted } from 'vue';

import Header from './components/Header.vue'
import Footer from './components/Footer.vue'


const authStore = useAuthStore();

onMounted(() => {
  authStore.checkAuth();
});

</script>

<template>
  <Header />
  <router-view></router-view> 
  <Footer />
</template>

<style>
/* Custom styles or scoped styles if needed */
</style>
