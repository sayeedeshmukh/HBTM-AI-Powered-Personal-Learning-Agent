from models.learner import LearnerInput
from models.roadmap import PlannerInput
from models.resource import ResourceInput

from agents.intent_agent import intent_agent
from agents.planner_agent import planner_agent
from agents.resource_agent import resource_agent

from memory.learner_memory import learner_memory


class OrchestratorAgent:

    def execute(self, data):

        # ------------------------------------
        # Step 1 : Intent Agent
        # ------------------------------------

        learner = LearnerInput(
            goal=data.goal,
            skill_level=data.skill_level,
            daily_hours=data.daily_hours,
            deadline=data.deadline,
            learning_style=data.learning_style
        )

        intent_result = intent_agent.analyze(learner)

        # ------------------------------------
        # Step 2 : Planner Agent
        # ------------------------------------

        planner_input = PlannerInput(
            goal=intent_result["goal"],
            goal_category=intent_result["goal_category"],
            domain=intent_result["domain"],
            target_role=intent_result["target_role"],
            current_skill_level=intent_result["current_skill_level"],
            difficulty=intent_result["difficulty"],
            deadline_feasible=intent_result["deadline_feasible"],
            recommended_timeline=intent_result["recommended_timeline"],
            required_skills=intent_result["required_skills"],
            missing_prerequisites=intent_result["missing_prerequisites"],
            learning_constraints=intent_result["learning_constraints"],
            priority_topics=intent_result["priority_topics"],
            summary=intent_result["summary"]
        )

        roadmap = planner_agent.generate(planner_input)

        # ------------------------------------
        # Step 3 : Create Learner Session
        # ------------------------------------

        learner_id = "vedant"

        session = learner_memory.get_session(learner_id)

        if session is None:

            learner_memory.create_session(
                learner_id=learner_id,
                roadmap=roadmap
            )

            session = learner_memory.get_session(learner_id)

        # ------------------------------------
        # Step 4 : Resource Agent
        # ------------------------------------

        resources = {}

        if intent_result["required_skills"]:

            first_skill = intent_result["required_skills"][0]

            resource_input = ResourceInput(
                topic=first_skill,
                skill_level=intent_result["current_skill_level"],
                learning_style=data.learning_style
            )

            resources = resource_agent.get_resources(resource_input)

        # ------------------------------------
        # Final Response
        # ------------------------------------

        return {

            "learner_profile": intent_result,

            "roadmap": roadmap,

            "resources": resources,

            "session": session

        }


orchestrator_agent = OrchestratorAgent()