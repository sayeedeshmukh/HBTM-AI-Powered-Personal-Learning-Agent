class PlannerAgent:

    def generate(self, learner):

        roadmap = []

        week = 1

        for skill in learner.required_skills:

            roadmap.append(
                {
                    "week": week,
                    "title": skill,
                    "topics": self.get_topics(skill),
                    "estimated_hours": 14,
                    "status": "Pending"
                }
            )

            week += 1

        return {

            "goal": learner.goal,

            "target_role": learner.target_role,

            "timeline": learner.recommended_timeline,

            "total_weeks": len(roadmap),

            "roadmap": roadmap,

            "milestones": [

                {
                    "week": 2,
                    "goal": "Complete Programming Basics"
                },

                {
                    "week": 4,
                    "goal": "Build First Mini Project"
                },

                {
                    "week": 6,
                    "goal": "Complete Backend APIs"
                },

                {
                    "week": 8,
                    "goal": "Placement Ready"
                }

            ]

        }

    def get_topics(self, skill):

        data = {

            "HTML": [
                "Elements & Tags",
                "Forms",
                "Semantic HTML",
                "Tables & Media"
            ],

            "CSS": [
                "Selectors",
                "Flexbox",
                "Grid",
                "Responsive Design"
            ],

            "JavaScript": [
                "Variables & Types",
                "Functions & Scope",
                "DOM Manipulation",
                "Async/Await"
            ],

            "React": [
                "Components & Props",
                "State & Hooks",
                "Routing",
                "API Integration"
            ],

            "TypeScript": [
                "Types & Interfaces",
                "Generics",
                "Enums",
                "Decorators"
            ],

            "Java": [
                "Variables",
                "Loops",
                "Arrays",
                "Functions"
            ],

            "Spring Boot": [
                "REST APIs",
                "Controllers",
                "Dependency Injection",
                "JPA"
            ],

            "SQL": [
                "SELECT",
                "JOINS",
                "GROUP BY",
                "Indexes"
            ],

            "REST APIs": [
                "HTTP Methods",
                "Status Codes",
                "JSON",
                "Authentication"
            ],

            "Git": [
                "Commit",
                "Branch",
                "Merge",
                "GitHub"
            ],

            "Docker": [
                "Images",
                "Containers",
                "Dockerfile",
                "Compose"
            ],

            "AWS": [
                "EC2",
                "S3",
                "IAM",
                "Deployment"
            ]

        }

        return data.get(skill, ["Introduction"])


planner_agent = PlannerAgent()