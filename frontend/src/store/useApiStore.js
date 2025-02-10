// src/store/useApiStore.js
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { axiosInstance } from '../lib/axios'; 
import { useToast } from 'vue-toast-notification';  

export const useApiStore = defineStore('apiStore', () => {
  const message = ref(''); 
  const toast = useToast(); 

  // API call method using Axios
  const fetchMessage = async () => {
    try {
      const response = await axiosInstance.get('/'); 
      message.value = response.data.message;


      toast.success(message.value, {
        position: 'top-right', 
        timeout: 3000, 
      });
    } catch (error) {
      toast.error(error.message || 'Something went wrong!', {
        position: 'top-right',
        timeout: 3000,
      });
    }
  };

  return { message, fetchMessage }; // Return the reactive state and method
});
