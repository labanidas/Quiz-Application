<script setup>
import { useQuizStore } from '@/store/useQuizStore';
import { ref, defineEmits } from 'vue';

const quizStore = useQuizStore();
const emit = defineEmits(['submit']);

const amounts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50];
const categories = ["Any Category", "General Knowledge", "Geography", "Science: Computers"];
const difficulties = ["easy", "medium", "hard"];
const types = { "Multiple": "multiple", "True/False": "boolean" };

const form = ref({
  amount: amounts[0],
  category: categories[0],
  difficulty: difficulties[0],
  type: types["Multiple"]
});

// Handle form submission
const handleSubmit = () => {
  quizStore.fetchQuestions(form.value);
  emit('submit'); // Notify parent component to close modal and navigate
};
</script>

<template>
  <form @submit.prevent="handleSubmit" class="space-y-6">
    <div>
      <label class="block text-lg font-semibold text-gray-700">📌 Number of Questions</label>
      <select v-model="form.amount" class="mt-2 p-3 w-full border rounded-xl focus:ring-purple-500">
        <option v-for="value in amounts" :key="value" :value="value">{{ value }}</option>
      </select>
    </div>

    <div>
      <label class="block text-lg font-semibold text-gray-700">📂 Category</label>
      <select v-model="form.category" class="mt-2 p-3 w-full border rounded-xl focus:ring-purple-500">
        <option v-for="category in categories" :key="category" :value="category">{{ category }}</option>
      </select>
    </div>

    <div>
      <label class="block text-lg font-semibold text-gray-700">🎯 Difficulty</label>
      <select v-model="form.difficulty" class="mt-2 p-3 w-full border rounded-xl focus:ring-purple-500">
        <option v-for="level in difficulties" :key="level" :value="level">{{ level }}</option>
      </select>
    </div>

    <div>
      <label class="block text-lg font-semibold text-gray-700">✅ Question Type</label>
      <select v-model="form.type" class="mt-2 p-3 w-full border rounded-xl focus:ring-purple-500">
        <option v-for="(value, key) in types" :key="key" :value="value">{{ key }}</option>
      </select>
    </div>

    <button type="submit"
      class="w-full py-3 bg-purple-600 text-white font-semibold rounded-lg hover:bg-purple-700 transition">
      🚀 Start Quiz
    </button>
  </form>
</template>
