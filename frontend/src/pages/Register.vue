<script setup>
import { useAuthStore } from '@/store/useAuthStore';
import { ref } from 'vue';

// Reactive form data
const email = ref('');
const password = ref('');
const role = ref('user'); // Default role is 'user'

// Access the auth store
const authStore = useAuthStore();

// Handle form submission
const handleSubmit = () => {
  // Creating formData to send
  const formData = {
    email: email.value,
    password: password.value,
    role: role.value
  };

  // Call the register method from the store
  authStore.register(formData);

  // Clear the form after submission
  clearForm();
};

// Reset form fields
const clearForm = () => {
  email.value = '';
  password.value = '';
  role.value = 'user'; // Reset role to default 'user'
};
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-r from-indigo-600 to-blue-500">
    <div class="bg-white p-8 rounded-lg shadow-lg max-w-sm w-full space-y-6">
      <h2 class="text-3xl font-bold text-center text-gray-800 mb-6">Create an Account</h2>

      <!-- Form -->
      <form @submit.prevent="handleSubmit" class="space-y-6">

        <!-- Email Field -->
        <div>
          <label for="email" class="block text-sm font-semibold text-gray-700">Email</label>
          <input id="email" type="email" v-model="email" placeholder="Enter your email"
            class="mt-2 p-3 w-full border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
            required />
        </div>

        <!-- Password Field -->
        <div>
          <label for="password" class="block text-sm font-semibold text-gray-700">Password</label>
          <input id="password" type="password" v-model="password" placeholder="Enter your password"
            class="mt-2 p-3 w-full border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
            required />
        </div>

        <!-- Role Selection Dropdown -->
        <div>
          <label for="role" class="block text-sm font-semibold text-gray-700">Role</label>
          <select id="role" v-model="role"
            class="mt-2 p-3 w-full border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500">
            <option value="user">User</option>
            <option value="admin">Admin</option>
          </select>
        </div>

        <!-- Submit Button -->
        <div>
          <button type="submit"
            class="w-full py-3 bg-indigo-600 text-white font-semibold rounded-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out">
            Register
          </button>
        </div>

      </form>

      <!-- Sign In Link -->
      <div class="text-center">
        <p class="text-sm text-gray-600">
          Already have an account?
          <a href="/login" class="text-indigo-600 font-semibold hover:text-indigo-700">Sign In</a>
        </p>
      </div>
    </div>
  </div>

</template>

<style scoped>
/* Add custom styles if necessary */
</style>
