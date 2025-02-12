<script setup>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div class="min-h-screen flex flex-col">
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
