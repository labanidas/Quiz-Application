<script setup>
import { generate_result } from "@/lib/utils";
import { useQuizStore } from "@/store/useQuizStore";
import { ref } from "vue";

const quizStore = useQuizStore();
// const { quiz_questions } = quizStore;

const quiz_questions = [
  {
    question: "What is the capital of France?",
    correct_answer: "Paris",
    incorrect_answers: ["Lyon", "Marseille", "Nice"],
  },
  {
    question: "What is the largest planet in our solar system?",
    correct_answer: "Jupiter",
    incorrect_answers: ["Saturn", "Neptune", "Earth"],
  },
  {
    question: "What year did the Titanic sink?",
    correct_answer: "1912",
    incorrect_answers: ["1910", "1914", "1916"],
  },
  {
    question: "Which element has the chemical symbol 'O'?",
    correct_answer: "Oxygen",
    incorrect_answers: ["Gold", "Silver", "Iron"],
  },
  {
    question: "Who wrote 'Hamlet'?",
    correct_answer: "William Shakespeare",
    incorrect_answers: ["Charles Dickens", "J.K. Rowling", "Leo Tolstoy"],
  },
];

const result = ref(null);
const submittedAnswers = ref([]);

const shuffleOptions = (options) => {
  return options.sort(() => Math.random() - 0.5); // Shuffle options
};

const handleChange = (index, option) => {
  submittedAnswers.value[index] = option;
};
// Handle form submission
const handleSubmit = () => {
  result.value = generate_result(quiz_questions, submittedAnswers.value);
};
</script>

<template>
  <div
    class="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-purple-50 via-indigo-50 to-white px-4"
  >
    <!-- Result Section -->
    <div
      v-if="result"
      class="p-8 rounded-3xl shadow-xl w-full max-w-3xl bg-gradient-to-br from-purple-100 via-purple-200 to-purple-300 border border-purple-400"
    >
      <h2 class="text-3xl font-extrabold text-center text-purple-900 mb-8">
        🎉 Quiz Summary
      </h2>

      <!-- Display Result -->
      <div class="space-y-6 text-lg text-center">
        <div class="font-semibold text-purple-800">
          📌 Total Questions:
          <span class="text-purple-900 font-bold">{{
            result.total_questions
          }}</span>
        </div>
        <div class="font-semibold text-purple-800">
          ✅ Attended:
          <span class="text-purple-900 font-bold">{{ result.attended }}</span>
        </div>
        <div class="font-semibold text-purple-800">
          📊 Percentage:
          <span class="text-purple-900 font-bold"
            >{{ result.percentage }}%</span
          >
        </div>
        <div class="font-semibold text-purple-800">
          🎯 Remark:
          <span
            :class="{
              'text-green-800 font-bold bg-green-200 px-3 py-1 rounded-lg':
                result.remark === 'pass',
              'text-red-800 font-bold bg-red-200 px-3 py-1 rounded-lg':
                result.remark === 'fail',
            }"
          >
            {{ result.remark.toUpperCase() }}
          </span>
        </div>
      </div>

      <!-- Navigate to Dashboard Button -->
      <div class="mt-8 flex justify-center">
        <button
          @click="$router.push('/dashboard')"
          class="px-5 py-2.5 bg-gradient-to-r from-purple-500 via-violet-600 to-indigo-700 text-white font-bold rounded-full shadow-md flex items-center gap-2 text-base transition-all duration-300 ease-in-out transform hover:scale-105 hover:shadow-lg hover:from-indigo-700 hover:via-purple-600 hover:to-purple-500"
        >
          <span class="text-yellow-300 text-lg drop-shadow-md">🔙</span>
          <span>Back to Dashboard</span>
        </button>
      </div>
    </div>

    <!-- Quiz Form -->
    <div v-else class="bg-white p-8 rounded-3xl shadow-lg w-full max-w-3xl">
      <h2 class="text-3xl font-extrabold text-center text-indigo-900 mb-8">
        Quiz Time
      </h2>

      <form @submit.prevent="handleSubmit" class="space-y-8">
        <!-- Loop through each quiz question -->
        <div
          v-for="(question, index) in quiz_questions"
          :key="index"
          class="p-4 border border-gray-200 rounded-2xl shadow-md"
        >
          <!-- Question -->
          <div class="text-lg md:text-xl font-bold text-gray-800 mb-4">
            {{ question.question }}
          </div>

          <!-- Options -->
          <div class="space-y-2">
            <div
              v-for="(option, idx) in shuffleOptions([
                question.correct_answer,
                ...question.incorrect_answers,
              ])"
              :key="idx"
              class="flex items-center space-x-3"
            >
              <input
                type="radio"
                :name="'question_' + index"
                :value="option"
                class="h-5 w-5 border-gray-300 text-indigo-600 focus:ring-indigo-500"
                @change="handleChange(index, option)"
              />
              <label class="text-gray-700 font-medium cursor-pointer">{{
                option
              }}</label>
            </div>
          </div>
        </div>

        <!-- Submit Button -->
        <div class="flex justify-center">
          <button
            type="submit"
            class="w-full md:w-1/2 py-3 bg-indigo-600 text-white font-bold rounded-lg shadow-md hover:bg-indigo-700 transition duration-300 ease-in-out"
          >
            Submit Answers
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
/* Custom styles for quiz elements */
</style>
