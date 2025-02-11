<script setup>
import { useAuthStore } from '@/store/useAuthStore';
const authStore = useAuthStore();
const authUser = authStore.authUser;

const logout = () => {
  authStore.authUser = null; 
  // authStore.checkAuth();  // Optionally trigger checkAuth to reset the state
}
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
      <router-link to="/" class="text-lg hover:text-yellow-400 transition duration-300">Home</router-link>
      <router-link to="/dashboard" class="text-lg hover:text-yellow-400 transition duration-300">Dashboard</router-link>
      <router-link to="/quiz" class="text-lg hover:text-yellow-400 transition duration-300">Quiz</router-link>

      <!-- Show Login/Register if unauthenticated -->
      <template v-if="!authUser">
        <router-link to="/login" class="text-lg hover:text-yellow-400 transition duration-300">Login</router-link>
        <router-link to="/register" class="text-lg hover:text-yellow-400 transition duration-300">Register</router-link>
      </template>

      <!-- Show Logout if authenticated -->
      <template v-if="authUser">
        <button @click="logout" class="text-lg hover:text-yellow-400 transition duration-300">Logout</button>
      </template>
    </nav>
  </header>
</template>

<style>
/* Additional custom styles if needed */
</style>
