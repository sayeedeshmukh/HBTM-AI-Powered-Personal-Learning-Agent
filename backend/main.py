from fastapi import FastAPI

from models.learner import LearnerInput
from models.roadmap import PlannerInput

from agents.intent_agent import intent_agent
from agents.planner_agent import planner_agent

from models.resource import ResourceInput
from agents.resource_agent import resource_agent

from models.quiz import QuizInput
from agents.quiz_agent import quiz_agent

from models.evaluation import EvaluationInput
from agents.evaluation_agent import evaluation_agent

from models.coach import CoachInput
from agents.coach_agent import coach_agent

from models.orchestrator import OrchestratorInput
from agents.orchestrator_agent import orchestrator_agent

from models.supervisor import SupervisorInput
from agents.supervisor_agent import supervisor_agent

from models.nudge import NudgeInput
from agents.nudge_agent import nudge_agent

from fastapi.middleware.cors import CORSMiddleware
from memory.learner_memory import learner_memory

app = FastAPI(title="Agentic AI Learning System")

# Add CORS middleware to allow requests from Flutter Web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def home():

    return {

        "message": "Agentic AI Backend Running"

    }


@app.post("/intent")
def intent(data: LearnerInput):

    return intent_agent.analyze(data)


@app.post("/planner")
def planner(data: PlannerInput):

    return planner_agent.generate(data)


@app.post("/resources")
def resources(data: ResourceInput):
    return resource_agent.get_resources(data)


@app.post("/quiz")
def quiz(data: QuizInput):
    return quiz_agent.generate_quiz(data)


@app.post("/evaluate")
def evaluate(data: EvaluationInput):
    return evaluation_agent.evaluate(data)


@app.post("/coach")
def coach(data: CoachInput):
    return coach_agent.generate_feedback(data)


@app.post("/learn")
def learn(data: OrchestratorInput):
    return orchestrator_agent.execute(data)


@app.post("/supervisor")
def supervisor(data: SupervisorInput):
    return supervisor_agent.decide(data)


@app.post("/nudge")
def nudge(data: NudgeInput):
    return nudge_agent.generate_nudge(data)


@app.get("/memory/{learner_id}")
def get_memory(learner_id: str):

    session = learner_memory.get_session(learner_id)

    if session is None:
        return {
            "message": "Session not found."
        }

    return session