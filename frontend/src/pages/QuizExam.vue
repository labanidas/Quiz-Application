<script setup>
import { generate_result } from "@/lib/utils";
import { useQuizStore } from "@/store/useQuizStore";
import { useRouter } from "vue-router";
import { ref, onMounted } from "vue";

const router = useRouter();
const loading = ref(false);
const isFetching = ref(true); // Track quiz loading state

const navigateToDashboard = () => {
  loading.value = true;
  setTimeout(() => {
    router.push("/dashboard");
  }, 1500);
};

const quizStore = useQuizStore();
const { quiz_questions } = quizStore;

const result = ref(null);
const submittedAnswers = ref([]);

// Simulate fetching data
onMounted(() => {
  setTimeout(() => {
    isFetching.value = false; // Fake delay to show loader
  }, 2000);
});

const shuffleOptions = (options) => {
  return options.sort(() => Math.random() - 0.5);
};

const handleChange = (index, option) => {
  submittedAnswers.value[index] = option;
};

const handleSubmit = () => {
  result.value = generate_result(quiz_questions, submittedAnswers.value);
};
</script>

<template>
  <!-- Show Loader While Fetching Quiz Questions -->
  <div v-if="isFetching" class="flex items-center justify-center py-20">
    <div class="flex flex-col items-center">
      <!-- Spinner -->
      <svg
        class="animate-spin h-16 w-16 text-purple-600"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
      >
        <circle
          class="opacity-25"
          cx="12"
          cy="12"
          r="10"
          stroke="currentColor"
          stroke-width="4"
        ></circle>
        <path
          class="opacity-75"
          fill="currentColor"
          d="M4 12a8 8 0 018-8v4l3-3-3-3v4a8 8 0 11-8 8z"
        ></path>
      </svg>
      <!-- Loading Text -->
      <p class="mt-4 text-lg font-semibold text-gray-700">
        Loading Quiz Questions...
      </p>
    </div>
  </div>

  <!-- Main Content -->
  <div
    v-else
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
          @click="navigateToDashboard"
          :disabled="loading"
          class="px-5 py-2.5 bg-gradient-to-r from-purple-500 via-violet-600 to-indigo-700 text-white font-bold rounded-full shadow-md flex items-center gap-2 text-base transition-all duration-300 ease-in-out transform hover:scale-105 hover:shadow-lg hover:from-indigo-700 hover:via-purple-600 hover:to-purple-500 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <span v-if="!loading" class="text-yellow-300 text-lg drop-shadow-md"
            >🔙</span
          >
          <svg
            v-else
            class="animate-spin h-5 w-5 text-yellow-300"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle
              class="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              stroke-width="4"
            ></circle>
            <path
              class="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8v4l3-3-3-3v4a8 8 0 11-8 8z"
            ></path>
          </svg>
          <span>{{ loading ? "Redirecting..." : "Back to Dashboard" }}</span>
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
