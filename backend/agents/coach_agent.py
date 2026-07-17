class CoachAgent:

    def generate_feedback(self, data):

        if data.percentage >= 90:
            motivation = "Outstanding work! You have mastered this topic."
            next_step = "Move on to advanced concepts."

        elif data.percentage >= 75:
            motivation = "Great job! You have a solid understanding."
            next_step = "Revise the incorrect concepts once."

        elif data.percentage >= 50:
            motivation = "Good effort! You're making progress."
            next_step = "Review the weak concepts and attempt another quiz."

        else:
            motivation = "Don't worry. Every expert was once a beginner."
            next_step = "Study the basics again before taking another quiz."

        weak_topics = []

        for item in data.incorrect_answers:
            weak_topics.append(item.question)

        return {

            "topic": data.topic,

            "performance": data.performance,

            "score": f"{data.score}/{data.total_questions}",

            "percentage": data.percentage,

            "motivation": motivation,

            "weak_topics": weak_topics,

            "next_step": next_step,

            "recommended_action": "Visit the Resource Agent and revise these concepts before attempting another quiz."

        }


coach_agent = CoachAgent()