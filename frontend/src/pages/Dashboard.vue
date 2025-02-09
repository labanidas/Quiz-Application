<script setup>
import Sidebar from '@/components/Sidebar.vue'
</script>

<template>
    <div class="flex min-h-screen bg-gray-100">
    <!-- Sidebar -->
    <Sidebar />

    <!-- Main content area -->
    <div class="flex-1 p-8">
      <h1 class="text-3xl font-bold text-gray-800">Dashboard</h1>
      <p class="mt-4 text-lg text-gray-600">Welcome to the admin dashboard. You can manage your settings here.</p>

      <!-- Additional content goes here -->
      <div class="mt-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Example Cards or Content -->
        <div class="bg-white p-6 rounded-lg shadow-md">
          <h3 class="text-xl font-semibold text-gray-800">Statistics</h3>
          <p class="mt-2 text-gray-600">Overview of your recent activity and stats.</p>
        </div>

        <div class="bg-white p-6 rounded-lg shadow-md">
          <h3 class="text-xl font-semibold text-gray-800">Users</h3>
          <p class="mt-2 text-gray-600">Manage your user accounts here.</p>
        </div>

        <div class="bg-white p-6 rounded-lg shadow-md">
          <h3 class="text-xl font-semibold text-gray-800">Settings</h3>
          <p class="mt-2 text-gray-600">Adjust your account and system settings.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* Custom styles or scoped styles if needed */
</style>
