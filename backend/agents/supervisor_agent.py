from models.resource import ResourceInput
from models.coach import CoachInput

from agents.resource_agent import resource_agent
from agents.coach_agent import coach_agent

from memory.learner_memory import learner_memory


class SupervisorAgent:

    def decide(self, data):

        # -------------------------------
        # Decision Logic
        # -------------------------------

        if data.percentage < 40:

            action = "REVISE_TOPIC"

            reason = (
                "Your understanding of this topic is weak. "
                "Study the learning resources before attempting the quiz again."
            )

        elif data.percentage < 70:

            action = "RETAKE_QUIZ"

            reason = (
                "You are close to mastering this topic. "
                "Practice once more before moving ahead."
            )

        else:

            action = "NEXT_TOPIC"

            reason = (
                "Excellent work! You can continue to the next topic."
            )

        # -------------------------------
        # Resources
        # -------------------------------

        resource_input = ResourceInput(
            topic=data.topic,
            skill_level=data.skill_level,
            learning_style=data.learning_style
        )

        resources = resource_agent.get_resources(resource_input)

        # -------------------------------
        # Coach
        # -------------------------------

        coach_input = CoachInput(
            topic=data.topic,
            score=int(data.percentage),
            total_questions=100,
            percentage=data.percentage,
            performance=data.performance,
            incorrect_answers=[]
        )

        coach = coach_agent.generate_feedback(coach_input)

        # -------------------------------
        # Next Topic
        # -------------------------------

        next_topic = None

        if action == "NEXT_TOPIC":

            if data.current_index + 1 < len(data.roadmap):

                next_topic = data.roadmap[data.current_index + 1]["title"]

        # -------------------------------
        # Response
        # -------------------------------

        return {

            "action": action,

            "reason": reason,

            "current_topic": data.topic,

            "next_topic": next_topic,

            "coach": coach,

            "resources": resources

        }


supervisor_agent = SupervisorAgent()