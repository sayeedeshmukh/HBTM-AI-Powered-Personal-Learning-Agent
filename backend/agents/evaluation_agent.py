from agents.quiz_agent import quiz_agent


class EvaluationAgent:

    def evaluate(self, data):

        score = 0

        total = len(data.answers)

        wrong_questions = []

        for user_answer in data.answers:

            for quiz in quiz_agent.current_quiz:

                if quiz["id"] == user_answer.question_id:

                    if quiz["answer"] == user_answer.selected_option:

                        score += 1

                    else:

                        wrong_questions.append({

                            "question": quiz["question"],

                            "correct_answer": quiz["answer"],

                            "your_answer": user_answer.selected_option

                        })

        percentage = round((score / total) * 100, 2) if total else 0

        if percentage >= 80:

            level = "Excellent"

        elif percentage >= 60:

            level = "Good"

        elif percentage >= 40:

            level = "Average"

        else:

            level = "Needs Improvement"

        return {

            "topic": data.topic,

            "score": score,

            "total_questions": total,

            "percentage": percentage,

            "performance": level,

            "incorrect_answers": wrong_questions

        }


evaluation_agent = EvaluationAgent()