// src/store/useApiStore.js
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { axiosInstance } from '../lib/axios'; // Import the axiosInstance

export const useApiStore = defineStore('apiStore', () => {
  const message = ref(''); 

  // API call method using Axios
  const fetchMessage = async () => {
    try {
      const response = await axiosInstance.get('/'); 
      message.value = response.data.message;
    } catch (error) {
      if (error.response) {
        console.error('Server Error:', error.response.data);
      } else if (error.request) {
        console.error('Network Error:', error.request);
      } else {
        console.error('Error:', error.message);
      }
    }finally{

    }
  };

  return { message, fetchMessage }; // Return the state and method
});
