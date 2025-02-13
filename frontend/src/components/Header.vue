<script setup>
import { onMounted, computed } from 'vue';
import { useAuthStore } from '@/store/useAuthStore';
import { useRouter, useRoute } from "vue-router";

const router = useRouter();
const route = useRoute();
const authStore = useAuthStore();

const currentPath = computed(() => route.path);

onMounted(async() => {
  await authStore.checkAuth();
});
</script>

<template>
  <header class="bg-purple-900 text-white flex items-center justify-between p-4">
    <!-- Logo Section -->
    <div class="flex items-center space-x-4">
      <img src="@/assets/logo2.png" alt="QuizMaster Logo" class="h-14 md:h-16 transition-transform transform hover:scale-105" />
      <h1 class="text-2xl md:text-3xl font-semibold">QuizMaster</h1>
    </div>

    <!-- Navigation Menu -->
    <nav class="flex space-x-6">
      <router-link to="/" class="text-lg hover:text-yellow-400 transition duration-300" :class="{'opacity-50 pointer-events-none': currentPath === '/'}">Home</router-link>
      <router-link to="/dashboard" class="text-lg hover:text-yellow-400 transition duration-300" v-if="currentPath !== '/dashboard'">Dashboard</router-link>

      <!-- Show Login/Register if unauthenticated -->
      <template v-if="!authStore.authUser">
        <router-link to="/login" class="text-lg hover:text-yellow-400 transition duration-300" v-if="currentPath !== '/login'">Login</router-link>
        <router-link to="/register" class="text-lg hover:text-yellow-400 transition duration-300" v-if="currentPath !== '/register'">Register</router-link>
      </template>

    </nav>
  </header>
</template>

<style>
/* Additional custom styles if needed */
</style>
