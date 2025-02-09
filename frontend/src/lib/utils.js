export const generate_result = (quiz_questions, submittedAnswers) => {
    console.log(submittedAnswers);
    console.log(quiz_questions);

    let totalQuestions = quiz_questions.length;
    let attended = 0;
    let correctAnswers = 0;
  
    // Loop through all questions and check the submitted answers
    quiz_questions.forEach((question, index) => {
      if (submittedAnswers[index]) {
        attended++;
        console.log(attended)
        if (submittedAnswers[index] === question.correct_answer) {
          correctAnswers++;
        }
      }
    });
  
    // Calculate the percentage
    let percentage = (correctAnswers / totalQuestions) * 100;
  
    // Determine if the user passed or failed (assuming passing is 50%)
    let remark = percentage >= 30 ? 'pass' : 'fail';
  
    // Return the result
    return {
      total_questions: totalQuestions,
      attended: attended,
      percentage: percentage.toFixed(2), // Round percentage to 2 decimal places
      remark: remark
    };
  };
  