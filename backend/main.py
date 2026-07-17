from fastapi import FastAPI
from pydantic import BaseModel
import os
from google import genai
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

class GhostToggleRequest(BaseModel):
    enable: bool
    learner_id: str = "vedant"


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


@app.post("/api/ghost-mode/toggle")
def toggle_ghost_mode(payload: GhostToggleRequest):
    session = learner_memory.get_session(payload.learner_id)
    if session is None:
        return {"error": "Session not found"}

    if payload.enable:
        session["ghost_mode"] = True
        session["backed_up_task"] = session["current_topic"]
        
        prompt = f"You are the Ghost Agent. The user is overwhelmed while trying to learn. Their current difficult milestone is: '{session['current_topic']}'. Generate a 2-minute alternative micro-task requiring zero coding or setup. Output ONLY a highly encouraging 2-sentence instruction. Never use guilt-inducing language."
        
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        
        session["current_topic"] = response.text
    else:
        session["ghost_mode"] = False
        session["current_topic"] = session["backed_up_task"]
        session["backed_up_task"] = ""

    return session