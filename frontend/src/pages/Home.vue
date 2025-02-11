<script setup>
// import 
</script>

<template>
    <div class="bg-gray-100 min-h-screen">
        <!-- Hero Section -->
        <section class="bg-purple-600 text-white h-screen flex flex-col justify-center items-center px-4 text-center">
            <h1 class="text-5xl md:text-6xl font-bold mb-4">Welcome to Quiz Master</h1>
            <p class="text-xl md:text-2xl mb-6 max-w-3xl">Test your knowledge, earn certifications, and track your
                progress with customized quizzes in various categories.</p>
            <router-link to="/login"
                class="bg-yellow-500 text-black px-8 py-3 rounded-lg font-semibold text-lg hover:bg-yellow-400 transition duration-300">Get
                Started</router-link>
        </section>

        <!-- Features Section -->
        <section class="py-16 bg-white text-center">
            <h2 class="text-4xl font-semibold text-gray-800 mb-8">Features</h2>
            <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-12 px-4">
                <div class="bg-gray-50 p-8 rounded-xl shadow-lg">
                    <h3 class="text-2xl font-semibold text-purple-600 mb-4">Customizable Quizzes</h3>
                    <p class="text-lg text-gray-600">Choose your preferred quiz category, difficulty, and number of
                        questions for a personalized experience.</p>
                </div>
                <div class="bg-gray-50 p-8 rounded-xl shadow-lg">
                    <h3 class="text-2xl font-semibold text-purple-600 mb-4">Results & Certifications</h3>
                    <p class="text-lg text-gray-600">Track your quiz scores and receive certificates for successful
                        completion of the quizzes.</p>
                </div>
                <div class="bg-gray-50 p-8 rounded-xl shadow-lg">
                    <h3 class="text-2xl font-semibold text-purple-600 mb-4">Progress Reports</h3>
                    <p class="text-lg text-gray-600">Keep track of your quiz history and see your performance over time
                        with detailed reports.</p>
                </div>
            </div>
        </section>

        <!-- Call to Action Section -->
        <section class="py-16 bg-purple-600 text-white text-center">
            <h2 class="text-3xl font-semibold mb-4">Ready to Test Your Knowledge?</h2>
            <p class="text-lg mb-8">Join Quiz Master and start your journey towards mastering new topics with fun
                quizzes.</p>
            <router-link to="/login"
                class="bg-yellow-500 text-black px-8 py-3 rounded-lg font-semibold text-lg hover:bg-yellow-400 transition duration-300">Get
                Started</router-link>
        </section>
    </div>

</template>

<style></style>
