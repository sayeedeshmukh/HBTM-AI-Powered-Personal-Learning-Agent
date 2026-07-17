from typing import Dict


class IntentAgent:

    def __init__(self):

        self.skill_database = {
            "backend": [
                "Java",
                "Spring Boot",
                "SQL",
                "REST APIs",
                "Git",
                "Docker",
                "AWS"
            ],
            "frontend": [
                "HTML",
                "CSS",
                "JavaScript",
                "React",
                "TypeScript"
            ],
            "datascience": [
                "Python",
                "NumPy",
                "Pandas",
                "Machine Learning",
                "Deep Learning"
            ],
            "ai": [
                "Python",
                "Machine Learning",
                "Deep Learning",
                "LLMs",
                "Computer Vision",
                "NLP"
            ]
        }

    def detect_domain(self, goal: str):

        goal = goal.lower()

        if "backend" in goal:
            return "backend"

        if "frontend" in goal:
            return "frontend"

        if "data" in goal:
            return "datascience"

        if "ai" in goal or "machine learning" in goal:
            return "ai"

        return "general"

    def estimate_difficulty(self, level: str):

        level = level.lower()

        if level == "beginner":
            return "High"

        if level == "intermediate":
            return "Medium"

        return "Low"

    def estimate_timeline(self, hours: float):

        if hours < 1:
            return "12 Months"

        if hours < 2:
            return "9 Months"

        if hours < 4:
            return "6 Months"

        return "4 Months"

    def analyze(self, learner) -> Dict:

        domain = self.detect_domain(learner.goal)

        skills = self.skill_database.get(domain, [])

        return {
            "goal": learner.goal,
            "goal_category": "Career",
            "domain": domain.title(),
            "target_role": learner.goal,
            "current_skill_level": learner.skill_level,
            "difficulty": self.estimate_difficulty(
                learner.skill_level
            ),
            "deadline_feasible": True,
            "recommended_timeline": self.estimate_timeline(
                learner.daily_hours
            ),
            "required_skills": skills,
            "missing_prerequisites": [
                "Programming Fundamentals",
                "Problem Solving"
            ],
            "learning_constraints": [
                f"{learner.daily_hours} hours/day",
                learner.learning_style
            ],
            "priority_topics": skills[:3],
            "summary": f"Learner wants to become {learner.goal}."
        }


intent_agent = IntentAgent()