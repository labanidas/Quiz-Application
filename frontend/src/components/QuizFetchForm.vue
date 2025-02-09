<script setup>
import { useQuizStore } from '@/store/useQuizStore';
import { ref } from 'vue';

const quizStore = useQuizStore();

const amounts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50];
const categories = ["Any Category", "General Knowledge", "Geography", "Science: Computers"];
const difficulties = ["easy", "medium", "hard"];
const types = {
    "Multiple": "multiple",
    "True/False": "boolean"
}

const form = ref({
    amount: amounts[0],
    category: categories[0],
    difficulty: difficulties[0],
    type: types["Multiple"]
});

// Handle form submission
const handleSubmit = () => {
    quizStore.fetchQuestions(form.value);
};
</script>

<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-100">
        <div class="bg-white p-8 rounded-lg shadow-lg max-w-sm w-full">
            <h2 class="text-2xl font-semibold text-center text-gray-800 mb-6">Select Your Preferences</h2>

            <form @submit.prevent="handleSubmit" class="space-y-6">

                <!-- Amount Selection -->
                <div>
                    <label for="amount" class="block text-sm font-semibold text-gray-700">Amount</label>
                    <select id="amount" v-model="form.amount"
                        class="mt-2 p-3 w-full border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500">
                        <option v-for="value in amounts" :key="value" :value="value">{{ value }}</option>
                    </select>
                </div>

                <!-- Category Selection -->
                <div>
                    <label for="category" class="block text-sm font-semibold text-gray-700">Category</label>
                    <select id="category" v-model="form.category"
                        class="mt-2 p-3 w-full border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500">
                        <!-- <option v-for="(value, key) in categories" :key="key" :value="value">{{ key }}</option> -->
                        <option v-for="category in categories" :key="category" :value="category">{{ category }}</option>
                    </select>
                </div>

                <!-- Difficulty Selection -->
                <div>
                    <label for="difficulty" class="block text-sm font-semibold text-gray-700">Difficulty</label>
                    <select id="difficulty" v-model="form.difficulty"
                        class="mt-2 p-3 w-full border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500">
                        <option v-for="level in difficulties" :key="level" :value="level">{{ level }}</option>
                    </select>
                </div>

                <!-- Type Selection -->
                <div>
                    <label for="type" class="block text-sm font-semibold text-gray-700">Type</label>
                    <select id="type" v-model="form.type"
                        class="mt-2 p-3 w-full border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500">
                        <option v-for="(value, key) in types" :key="key" :value="value">{{ key }}</option>
                    </select>
                </div>

                <!-- Submit Button -->
                <div>
                    <button type="submit"
                        class="w-full py-3 bg-indigo-600 text-white font-semibold rounded-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out">
                        Submit
                    </button>
                </div>

            </form>
        </div>
    </div>
</template>