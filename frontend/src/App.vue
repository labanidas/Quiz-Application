<script setup>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div class="min-h-screen flex flex-col bg-gradient-to-br from-purple-100 via-violet-200 to-indigo-100">
    <!-- Header -->
    <Header />

    <!-- Main Content with dynamic growth -->
    <div class="flex-grow">
      <router-view></router-view> 
    </div>

    <!-- Footer -->
    <Footer />
  </div>
</template>


<style>
 /* Additional global styles if needed */
</style>
