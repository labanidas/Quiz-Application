<script setup>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <Header />
  <!-- <div class="min-h-screen bg-gray-100 flex flex-col justify-center items-center">
    content
  </div> -->
  <!-- <router-link to="/register">Go to Register</router-link> -->
  <router-view></router-view> 
  <Footer />
</template>

<style>
/* Custom styles or scoped styles if needed */
</style>
