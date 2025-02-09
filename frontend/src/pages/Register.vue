<script setup>
import { useAuthStore } from '@/store/useAuthStore';
import { ref } from 'vue';

const email = ref('');
const password = ref('');

const handleSubmit = () => {
  // // Handle the registration logic here
  // console.log('Form submitted', { email: email.value, password: password.value });
  useAuthStore.register()
};
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="bg-white p-8 rounded-lg shadow-lg max-w-sm w-full">
      <h2 class="text-2xl font-semibold text-center text-gray-800 mb-6">Create an Account</h2>
      <!-- Your form elements go here, e.g., name, email, password -->
      <form @submit.prevent="handleSubmit">
        <!-- Form Fields Here -->
        <input type="email" v-model="email" placeholder="Email" class="mb-3 p-2 border rounded" />
        <input type="password" v-model="password" placeholder="Password" class="mb-3 p-2 border rounded" />
        <button type="submit" class="w-full py-2 bg-blue-500 text-white rounded">Register</button>
      </form>
    </div>
  </div>
</template>



<style scoped>
/* You can add custom styles here */
</style>