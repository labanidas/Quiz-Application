<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import Sidebar from "@/components/Sidebar.vue";
import QuizFetchForm from "@/components/QuizFetchForm.vue";

const showModal = ref(false);
const router = useRouter();

// Handle form submission and navigate to QuizExam
const handleFormSubmit = () => {
  showModal.value = false; // Close modal
  router.push("/quizExam"); // Navigate to quiz exam page
};
</script>

<template>
  <div
    class="flex flex-col md:flex-row min-h-screen bg-gradient-to-br from-indigo-50 via-purple-50 to-white"
  >
    <!-- Sidebar -->
    <Sidebar />

    <!-- Main Content -->
    <div class="flex-1 p-4 md:p-8 md:pl-72 relative">
      <!-- Artistic Background -->
      <div
        class="absolute inset-0 -z-10 bg-gradient-to-tr from-purple-100 to-indigo-100 opacity-20 rounded-lg"
      ></div>

      <!-- Top Navbar -->
      <div class="flex justify-between items-center mb-6 flex-wrap">
        <h1 class="text-2xl md:text-4xl font-extrabold text-indigo-900 mb-4 md:mb-0">
          Dashboard
        </h1>
        <button
          @click="showModal = true"
          class="px-4 py-2 md:px-6 md:py-3 bg-purple-600 text-white font-semibold rounded-lg shadow-md hover:bg-purple-700 transition-all duration-300"
        >
          🎯 Start a Quiz
        </button>
      </div>

      <!-- Dashboard Cards -->
      <div
        class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6"
      >
        <!-- Card 1 -->
        <div
          class="bg-white p-4 md:p-6 rounded-xl shadow-lg hover:shadow-2xl transform hover:scale-105 transition duration-300"
        >
          <div class="flex items-center md:flex-row flex-col">
            <div
              class="w-12 h-12 md:w-14 md:h-14 flex items-center justify-center rounded-full bg-indigo-100 text-indigo-700 text-xl md:text-2xl font-bold"
            >
              📊
            </div>
            <h3 class="text-xl md:text-2xl font-bold text-indigo-800 mt-4 md:mt-0 md:ml-4">
              Statistics
            </h3>
          </div>
          <p class="mt-2 text-sm md:text-base text-gray-600">
            Track your quiz performance and stats.
          </p>
        </div>

        <!-- Card 2 -->
        <div
          class="bg-white p-4 md:p-6 rounded-xl shadow-lg hover:shadow-2xl transform hover:scale-105 transition duration-300"
        >
          <div class="flex items-center md:flex-row flex-col">
            <div
              class="w-12 h-12 md:w-14 md:h-14 flex items-center justify-center rounded-full bg-purple-100 text-purple-700 text-xl md:text-2xl font-bold"
            >
              👤
            </div>
            <h3 class="text-xl md:text-2xl font-bold text-purple-800 mt-4 md:mt-0 md:ml-4">
              Users
            </h3>
          </div>
          <p class="mt-2 text-sm md:text-base text-gray-600">
            Manage your account and users.
          </p>
        </div>

        <!-- Card 3 -->
        <div
          class="bg-white p-4 md:p-6 rounded-xl shadow-lg hover:shadow-2xl transform hover:scale-105 transition duration-300"
        >
          <div class="flex items-center md:flex-row flex-col">
            <div
              class="w-12 h-12 md:w-14 md:h-14 flex items-center justify-center rounded-full bg-indigo-100 text-indigo-700 text-xl md:text-2xl font-bold"
            >
              ⚙️
            </div>
            <h3 class="text-xl md:text-2xl font-bold text-indigo-800 mt-4 md:mt-0 md:ml-4">
              Settings
            </h3>
          </div>
          <p class="mt-2 text-sm md:text-base text-gray-600">
            Personalize your quiz experience.
          </p>
        </div>
      </div>
    </div>

    <!-- Quiz Modal -->
    <div
      v-if="showModal"
      class="fixed inset-0 flex items-center justify-center z-50"
    >
      <!-- Beautiful Background -->
      <div
        class="absolute inset-0 bg-gradient-to-br from-blue-100 via-indigo-100 to-purple-100 opacity-90 blur-md"
      ></div>

      <!-- Modal Content -->
      <div
        class="bg-gradient-to-r from-white to-gray-100 p-6 md:p-8 rounded-2xl shadow-2xl max-w-xs md:max-w-md w-full relative z-10 border border-gray-200"
      >
        <!-- Close Button -->
        <button
          @click="showModal = false"
          class="absolute top-3 right-3 bg-gray-200 hover:bg-gray-300 text-gray-600 hover:text-gray-800 p-2 rounded-full shadow-md transition-all"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>

        <!-- Modal Title -->
        <h2 class="text-2xl md:text-3xl font-extrabold text-indigo-900 mb-4 md:mb-6">
          🎯 Customize Your Quiz
        </h2>

        <!-- Quiz Form -->
        <QuizFetchForm @submit="handleFormSubmit" />
      </div>
    </div>
  </div>
</template>
