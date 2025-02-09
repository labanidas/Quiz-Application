<script setup>
import { useQuizStore } from '@/store/useQuizStore';
import { ref } from 'vue';

// Access the quiz store and questions
const quizStore = useQuizStore();
const { quiz_questions } = quizStore;

// Function to shuffle options (correct + incorrect answers)
const shuffleOptions = (options) => {
  return options.sort(() => Math.random() - 0.5); // Simple shuffle
};

// Handle form submission
const handleSubmit = () => {
  // You can implement form submission logic here if needed
  console.log('Submit the quiz answers');
};
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-2xl">
      <h2 class="text-2xl font-semibold text-center text-gray-800 mb-6">Quiz Time</h2>

      <!-- Loop through each quiz question -->
      <form @submit.prevent="handleSubmit" class="space-y-6">

        <div v-for="(question, index) in quiz_questions" :key="index" class="mb-6">
          
          <!-- Question -->
          <div class="text-lg font-semibold text-gray-800 mb-4">{{ question.question }}</div>

          <!-- Shuffle options (correct + incorrect answers) -->
          <div class="space-y-2">
            <div v-for="(option, idx) in shuffleOptions([question.correct_answer, ...question.incorrect_answers])" :key="idx" class="flex items-center space-x-2">
              <input 
                type="radio" 
                :name="'question_' + index" 
                :value="option" 
                class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500"
              />
              <label class="text-gray-700">{{ option }}</label>
            </div>
          </div>
        </div>

        <!-- Submit Button -->
        <div class="flex justify-center">
          <button type="submit" class="w-full py-3 bg-indigo-600 text-white font-semibold rounded-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out">
            Submit Answers
          </button>
        </div>

      </form>
    </div>
  </div>
</template>

<style scoped>
/* Custom styles for the quiz page if needed */
</style>
