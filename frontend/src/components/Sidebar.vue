<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const isOpen = ref(true);
const router = useRouter();

const toggleSidebar = () => {
  isOpen.value = !isOpen.value;
};
</script>

<template>
  <div class="relative">
    <!-- Sidebar -->
    <div :class="isOpen ? 'w-64' : 'w-20'"
      class="bg-gradient-to-b from-indigo-900 to-purple-800 text-white min-h-screen fixed top-0 left-0 shadow-xl transition-all duration-300 z-50 flex flex-col overflow-hidden">
      
      <!-- Sidebar Header -->
      <div class="flex items-center justify-between p-4 border-b border-gray-700">
        <div class="flex items-center">
          <img src="https://img.icons8.com/ios-filled/50/ffffff/brainstorm-skill.png" alt="Logo" class="w-8 h-8" />
          <span v-if="isOpen" class="ml-3 text-xl font-bold tracking-wide">QuizMaster</span>
        </div>
        <button @click="toggleSidebar"
          class="text-gray-300 hover:text-white transition-all duration-300 p-2 rounded-full bg-gray-700 hover:bg-indigo-600">
          <svg v-if="isOpen" xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 rotate-180" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
          </svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
          </svg>
        </button>
      </div>

      <!-- Sidebar Navigation -->
      <nav class="flex-1 mt-4">
        <ul>
          <!-- Dashboard Button -->
          <li>
            <router-link to="/dashboard"
              class="flex items-center p-4 hover:bg-indigo-700 transition duration-300 rounded-lg"
              :class="{ 'bg-indigo-700': $route.path === '/dashboard' }">
              <svg class="w-6 h-6 text-gray-300" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h18M3 10h18M3 15h18"></path>
              </svg>
              <span v-if="isOpen" class="ml-4">Dashboard</span>
            </router-link>
          </li>

          <!-- Reports Button -->
          <li>
            <router-link to="/reports"
              class="flex items-center p-4 hover:bg-indigo-700 transition duration-300 rounded-lg"
              :class="{ 'bg-indigo-700': $route.path === '/reports' }">
              <svg class="w-6 h-6 text-gray-300" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v12l7-4 7 4V3"></path>
              </svg>
              <span v-if="isOpen" class="ml-4">Reports</span>
            </router-link>
          </li>

          <!-- Settings Button -->
          <li>
            <router-link to="/settings"
              class="flex items-center p-4 hover:bg-indigo-700 transition duration-300 rounded-lg"
              :class="{ 'bg-indigo-700': $route.path === '/settings' }">
              <svg class="w-6 h-6 text-gray-300" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2 2 4-4 6 6 8-8"></path>
              </svg>
              <span v-if="isOpen" class="ml-4">Settings</span>
            </router-link>
          </li>
        </ul>
      </nav>

      <!-- Logout Button -->
      <div class="p-4 border-t border-gray-700">
        <button @click="() => router.push('/logout')"
          class="flex items-center p-4 hover:bg-red-700 transition duration-300 rounded-lg w-full">
          <svg class="w-6 h-6 text-gray-300" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5h6M9 12h6M9 19h6"></path>
          </svg>
          <span v-if="isOpen" class="ml-4">Logout</span>
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Prevent hover effects from breaking layout */
li {
  overflow: hidden; /* Prevent child hover scaling from affecting layout */
}

li:hover {
  transform: none; /* Disable transform affecting overflow */
}
</style>
