<script setup>
import { generate_result } from "@/lib/utils";
import { useQuizStore } from '@/store/useQuizStore';
import { ref } from 'vue';

const quizStore = useQuizStore();
// const { quiz_questions } = quizStore;

const quiz_questions = [
  {
    question: "What is the capital of France?",
    correct_answer: "Paris",
    incorrect_answers: ["Lyon", "Marseille", "Nice"]
  },
  {
    question: "What is the largest planet in our solar system?",
    correct_answer: "Jupiter",
    incorrect_answers: ["Saturn", "Neptune", "Earth"]
  },
  {
    question: "What year did the Titanic sink?",
    correct_answer: "1912",
    incorrect_answers: ["1910", "1914", "1916"]
  },
  {
    question: "Which element has the chemical symbol 'O'?",
    correct_answer: "Oxygen",
    incorrect_answers: ["Gold", "Silver", "Iron"]
  },
  {
    question: "Who wrote 'Hamlet'?",
    correct_answer: "William Shakespeare",
    incorrect_answers: ["Charles Dickens", "J.K. Rowling", "Leo Tolstoy"]
  }
];


const result = ref(null);
const submittedAnswers = ref([]);

const shuffleOptions = (options) => {
  return options.sort(() => Math.random() - 0.5); // Shuffle options
};

const handleChange = (index, option) => {
  submittedAnswers.value[index] = option;
}
// Handle form submission
const handleSubmit = () => {
  result.value = generate_result(quiz_questions, submittedAnswers.value);
};
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div v-if="result" class="bg-white p-8 rounded-lg shadow-lg w-full max-w-2xl">
      <h2 class="text-2xl font-semibold text-center text-gray-800 mb-6">Your Result</h2>

      <!-- Display Result -->
      <div class="text-lg font-semibold text-gray-800 mb-4">Total Questions: {{ result.total_questions }}</div>
      <div class="text-lg font-semibold text-gray-800 mb-4">Attended: {{ result.attended }}</div>
      <div class="text-lg font-semibold text-gray-800 mb-4">Percentage: {{ result.percentage }}%</div>
      <div class="text-lg font-semibold text-gray-800 mb-4">Remark: <span
          :class="{ 'text-green-600': result.remark === 'pass', 'text-red-600': result.remark === 'fail' }">{{
            result.remark }}</span></div>

    </div>

    <!-- Display Quiz Form -->
    <div v-else class="bg-white p-8 rounded-lg shadow-lg w-full max-w-2xl">
      <h2 class="text-2xl font-semibold text-center text-gray-800 mb-6">Quiz Time</h2>

      <form @submit.prevent="handleSubmit" class="space-y-6">
        <!-- Loop through each quiz question -->
        <div v-for="(question, index) in quiz_questions" :key="index" class="mb-6">

          <!-- Question -->
          <div class="text-lg font-semibold text-gray-800 mb-4">{{ question.question }}</div>

          <!-- Shuffle options (correct + incorrect answers) -->
          <div class="space-y-2">
            <div v-for="(option, idx) in shuffleOptions([question.correct_answer, ...question.incorrect_answers])"
              :key="idx" class="flex items-center space-x-2">
              <input type="radio" :name="'question_' + index" :value="option"
                class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-500"
                @change= "handleChange(index, option)" />
              <label class="text-gray-700">{{ option }}</label>
            </div>
          </div>
        </div>

        <!-- Submit Button -->
        <div class="flex justify-center">
          <button type="submit"
            class="w-full py-3 bg-indigo-600 text-white font-semibold rounded-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out">
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
