// src/store/useQuizStore.js
import { defineStore } from "pinia";
import { ref } from "vue";
import { axiosInstance } from "../lib/axios";
import { useToast } from "vue-toast-notification";
import { useRouter } from "vue-router";

export const useQuizStore = defineStore('apiStore', () => {
  const router = useRouter();
  const toast = useToast();
  const quiz_questions = ref([]); 
  const isLoadingQuestions = ref(false);

  // API call method using Axios
  const fetchQuestions = async (data) => {
    isLoadingQuestions.value = true;
    try {
      const response = await axiosInstance.post('/quiz/fetch-questions', data); 
      quiz_questions.value = response.data.questions;  
      router.push("/quiz") 
    } catch (error) {
      toast.error(error.message || 'Something went wrong!', {
        position: 'top-right',
        timeout: 3000,
      });
    }finally{
      isLoadingQuestions.value = false;
    }
  };

  return {
    quiz_questions,
    isLoadingQuestions,
    fetchQuestions
  };
});
