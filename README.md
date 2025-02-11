

# **Quiz Master - Project Documentation**

**Quiz Master** is an online platform for taking quizzes, testing knowledge, and receiving certifications. Users can select their preferred quiz category, difficulty, and number of questions. After submitting their quiz answers, users receive a result, and those who pass can download a certification.

---

## **API Source**

- **Quiz API:** [Open Trivia Database](https://opentdb.com/)
- **Quiz Fetch URL:**  
  `https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean`

---

## **Project Schema**

- **USER:**  
  - emailId  
  - password  
  - timestamps  
  - role (user/admin)

- **QUIZ:**  
  - quizAPI (URL to the quiz API)  
  - userId (foreign key, links to USER)  
  - many-to-many relation (user can take many quizzes)

- **RESULT:**  
  - quizID (foreign key, links to QUIZ)  
  - total_questions  
  - correct_answers  
  - percentage  
  - cert_number (unique certificate ID)

---

## **Directory Structure**

### **Backend Structure**

```plaintext
backend/
├── app/
│   ├── controllers/                # Controllers handle business logic
│   │   ├── auth_controller.py      # Authentication-related logic
│   │   ├── quiz_controller.py      # Quiz fetching logic
│   │   ├── user_controller.py      # User-related operations
│   ├── middleware/                 # Middleware functions (authentication, validation, etc.)
│   │   ├── auth_middleware.py      # Middleware for token verification
│   ├── models/                     # Database-related logic
│   │   ├── user_model.py           # User model functions
│   ├── routes/                     # API route definitions
│   │   ├── auth_routes.py          # Routes for authentication
│   │   ├── quiz_routes.py          # Routes for quiz fetching
│   │   ├── user_routes.py          # Routes for user operations
│   ├── utils/                      # Utility functions
│   │   ├── validation.py           # Validation functions (email, password, etc.)
│   │   ├── response.py             # Response formatting
│   │   ├── helpers.py              # Miscellaneous helper functions
├── .env                            # Environment variables
├── config.py                       # Application configurations
├── requirements.txt                # Python dependencies
├── run.py                          # Main entry point for the backend
```

### **Frontend Structure**

```plaintext
frontend/
├── node_modules/            # Dependencies installed via npm/yarn
├── public/                  # Static assets (index.html, etc.)
│   └── index.html           # Root HTML template
├── src/                     # Source files
│   ├── assets/              # Static assets (images, fonts, etc.)
│   ├── components/          # Vue components
│   │   └── Header.vue       # Header component
│   ├── pages/               # Vue page components (for routing)
│   ├── router/              # Vue Router configuration
│   ├── store/               # Vuex store (state management)
│   ├── App.vue              # Main Vue component
│   └── main.js              # Main entry file
├── .gitignore               # Git ignore file
├── package.json             # Project dependencies and scripts
├── vite.config.js           # Vite configuration (if using Vite)
└── README.md                # Project documentation
```

---

## **Features**

### **User Features**

- **Authentication System:**  
  Users can log in and choose their role (User/Admin). The system supports:
  - User role (access to quiz and results)
  - Admin role (access to manage users, generate certificates)
  
- **Quiz Customization:**  
  Users can customize their quiz experience by selecting:
  - Category
  - Difficulty level
  - Type (e.g., multiple-choice, true/false)
  - Number of questions
  
- **Result & Certification:**  
  After completing the quiz, users will see:
  - Total number of questions
  - Correct answers
  - Percentage score
  - A certification if they pass the quiz (users can download it from their dashboard)

- **Progress Report:**  
  Users can view a history of all quizzes they’ve attended and see their progress over time.

### **Admin Features**

- **User Management:**  
  Admins can view all users and their associated quizzes and results.

- **Progress Reports:**  
  Admins can access detailed reports of each user's performance across quizzes.

- **Certificate Generation:**  
  Only admins can generate and issue certificates for users who pass their quizzes.

---

<!-- ## **Screenshots**

### **1. Dashboard**

![Dashboard Screenshot](path/to/dashboard-screenshot.png)

### **2. Quiz Selection Screen**

![Quiz Selection Screenshot](path/to/quiz-selection-screenshot.png)

### **3. Result Screen**

![Result Screenshot](path/to/result-screenshot.png)

--- -->

## **Technologies Used**

- **Backend:** Python, Flask
- **Frontend:** Vue.js, Vite
- **State Management:** Vuex
- **API:** Open Trivia Database
- **Database:** MongoDb
  
---

## **Installation Guide**

### **Backend Setup**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/quiz-master-backend.git
   ```
   
2. Navigate to the backend folder:
   ```bash
   cd backend
   ```

3. Install required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the backend server:
   ```bash
   python run.py
   ```

### **Frontend Setup**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/quiz-master-frontend.git
   ```

2. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```

3. Install required dependencies:
   ```bash
   npm install
   ```

4. Run the frontend development server:
   ```bash
   npm run dev
   ```

---

## **Contributing**

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make changes and commit (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

---

