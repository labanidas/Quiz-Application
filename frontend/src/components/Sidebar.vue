<template>
    <div class="w-64 bg-gray-800 text-white h-full flex flex-col">
      <div class="flex items-center justify-center p-6 border-b border-gray-700">
        <h2 class="text-2xl font-bold">Dashboard</h2>
      </div>
  
      <nav class="flex-1">
        <ul>
          <li>
            <a href="#" class="flex items-center p-4 hover:bg-gray-700 transition duration-200">
              <svg class="w-6 h-6 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h18M3 10h18M3 15h18M3 20h18"></path>
              </svg>
              <span class="ml-4">Dashboard</span>
            </a>
          </li>
          <li>
            <a href="#" class="flex items-center p-4 hover:bg-gray-700 transition duration-200">
              <svg class="w-6 h-6 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v12l7-4 7 4V3"></path>
              </svg>
              <span class="ml-4">Reports</span>
            </a>
          </li>
          <li>
            <a href="#" class="flex items-center p-4 hover:bg-gray-700 transition duration-200">
              <svg class="w-6 h-6 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2 2 4-4 6 6 8-8"></path>
              </svg>
              <span class="ml-4">Settings</span>
            </a>
          </li>
          <!-- Add more items as needed -->
        </ul>
      </nav>
  
      <div class="p-4 border-t border-gray-700">
        <a href="#" class="flex items-center p-4 hover:bg-gray-700 transition duration-200">
          <svg class="w-6 h-6 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5h6M9 12h6M9 19h6"></path>
          </svg>
          <span class="ml-4">Logout</span>
        </a>
      </div>
    </div>
  </template>
  
  <style scoped>
  /* Scoped styles for Sidebar */
  </style>
  