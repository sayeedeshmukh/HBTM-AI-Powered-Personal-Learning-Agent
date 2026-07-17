class NudgeAgent:

    def generate_nudge(self, data):
        message = (
            f"We noticed you've been away for {data.inactivity_days} days. "
            f"To keep your '{data.goal}' prep on track, let's review the '{data.topic}' section. "
            f"Shall we start with a short review session?"
        )

        return {
            "title": "Welcome Back!",
            "message": message,
            "topic": data.topic,
            "goal": data.goal
        }

nudge_agent = NudgeAgent()
