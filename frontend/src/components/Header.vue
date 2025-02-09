<script setup>
// import { onMounted } from 'vue';
// import { useApiStore } from '@/store/useApiStore'; 

// const apiStore = useApiStore(); 


// onMounted(() => {
//   apiStore.fetchMessage(); 
// });
</script>

<template>
  <header class="bg-gray-800 text-white flex items-center p-4">
    <img src="@/assets/logo2.png" alt="QuizMaster Logo" class="h-12 mr-4" />
    <h1 class="text-xl font-semibold">QuizMaster</h1>
  </header>
  <!-- <h1>{{ apiStore.message }}</h1>  -->
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style>
/* Additional custom styles if needed */
</style>
