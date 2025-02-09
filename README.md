
https://platform.openai.com/docs/guides/speech-to-text?utm_source=chatgpt.com

https://medium.com/towards-data-science/build-a-speech-to-text-web-app-using-node-js-210f8c054d79

https://opentdb.com/

https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean

{
  "amount": [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
  "category": {
    "Any Category": 0,
    "General Knowledge": 9,
    "Geography": 22,
    "Science: Computers": 18
  },
  "difficulty": ["easy", "medium", "hard"],
  "type": ["multiple", "boolean"]
}


schema

    USER = emailId, password, timestamps, role
    QUIZ = quizAPI, userId- foreignkey, (many-to many)
    result = quizID-foreign key, total_questions, correct_answers, percentage


backend/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── utils.py
├── .env
├── config.py
├── requirements.txt
└── run.py




