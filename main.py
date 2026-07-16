from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

app = FastAPI(title="Hack Better Than Me 2026 - Personal Learning Agent API")

# Enable CORS for Flutter web/desktop/mobile local testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Keys will be "user_id" (or we can default to a global "singleton" key for hackathon simplicity)
ROADMAP_DB: Dict[str, Dict[str, Any]] = {}


class GeneratePlanRequest(BaseModel):
    user_id: str = Field(..., example="user_123")
    learning_goal: str = Field(..., example="Learn FastAPI and Flutter integration")

class Task(BaseModel):
    task_id: str
    title: str
    description: str
    status: str = Field("Pending", description="Pending, In_Progress, Completed")

class RoadmapResponse(BaseModel):
    user_id: str
    learning_goal: str
    milestones: List[Task]
    reflection_log: List[str] = []
    coach_nudge: Optional[str] = None

class SimulateEventRequest(BaseModel):
    user_id: str
    event_trigger: str = Field(..., example="User finished Chapter 1 but failed the quiz")

class SimulateEventResponse(BaseModel):
    roadmap: RoadmapResponse
    evaluator_feedback: str
    reflection_insight: str
    coach_nudge: str

def run_intent_agent(goal: str) -> str:
    """Agent 1: Extracts clean intent and target metrics from user input."""
    return f"Refined Intent: Master the core concepts of '{goal}' with structured milestones."

def run_planner_agent(refined_intent: str) -> List[Dict[str, Any]]:
    """Agent 2: Breaks down the refined intent into sequential roadmap tasks."""
    # In a real setup, this calls your LLM API to output structured JSON
    return [
        {"task_id": "task_1", "title": "Setup & Fundamentals", "description": "Initialize workspace and run Hello World.", "status": "Pending"},
        {"task_id": "task_2", "title": "Core Deep Dive", "description": "Implement data routing, state management, and API calls.", "status": "Pending"},
        {"task_id": "task_3", "title": "Golden Path MVP Integration", "description": "Build, test, and wire up end-to-end user flows.", "status": "Pending"}
    ]

def run_evaluator_agent(event: str, current_roadmap: Dict[str, Any]) -> Dict[str, Any]:
    """Agent 3: Analyzes event triggers (e.g., test score, stuck timer) and evaluates progress."""
    return {
        "evaluation": f"Evaluated event '{event}'. User is showing engagement but needs structural adjustments to the learning speed.",
        "task_to_update": "task_1",
        "new_status": "Completed"
    }

def run_reflection_agent(evaluation_summary: str, current_roadmap: Dict[str, Any]) -> str:
    """Agent 4: Identifies friction points and appends lessons learned to the history."""
    return f"Reflection: The user adapted quickly to the setup phase. Recommended action: Accelerate transition to the Core Deep Dive."

def run_coach_agent(reflection: str) -> str:
    """Agent 5: Synthesizes a high-agency, supportive nudge based on reflection."""
    return f"Hey! You crushed that setup. 🚀 Let's keep this momentum rolling into the next module!"


@app.post("/api/generate-plan", response_model=RoadmapResponse)
async def generate_plan(payload: GeneratePlanRequest):
    try:
        # 1. Chain Intent -> Planner
        refined_intent = run_intent_agent(payload.learning_goal)
        milestones = run_planner_agent(refined_intent)
        
        # 2. Build the state
        roadmap_data = {
            "user_id": payload.user_id,
            "learning_goal": payload.learning_goal,
            "milestones": milestones,
            "reflection_log": [],
            "coach_nudge": "Welcome to your personalized agent path! Let's get started."
        }
        
        # 3. Store in-memory
        ROADMAP_DB[payload.user_id] = roadmap_data
        
        return roadmap_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/simulate-event", response_model=SimulateEventResponse)
async def simulate_event(payload: SimulateEventRequest):
    user_id = payload.user_id
    if user_id not in ROADMAP_DB:
        raise HTTPException(status_code=404, detail="Roadmap not found. Please run /generate-plan first.")
    
    current_roadmap = ROADMAP_DB[user_id]
    
    try:
        # 1. Run Evaluator Agent
        eval_result = run_evaluator_agent(payload.event_trigger, current_roadmap)
        
        # Apply the evaluator's state mutations to the roadmap
        for task in current_roadmap["milestones"]:
            if task["task_id"] == eval_result["task_to_update"]:
                task["status"] = eval_result["new_status"]
        
        # 2. Pass evaluation to Reflection Agent
        reflection_insight = run_reflection_agent(eval_result["evaluation"], current_roadmap)
        current_roadmap["reflection_log"].append(reflection_insight)
        
        # 3. Pass reflection to Coach Agent
        coach_nudge_msg = run_coach_agent(reflection_insight)
        current_roadmap["coach_nudge"] = coach_nudge_msg
        
        # Update our in-memory database
        ROADMAP_DB[user_id] = current_roadmap
        
        return {
            "roadmap": current_roadmap,
            "evaluator_feedback": eval_result["evaluation"],
            "reflection_insight": reflection_insight,
            "coach_nudge": coach_nudge_msg
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    # Run server locally on port 8000
    uvicorn.run("main:app", host="2401:4900:1c43:766a:e0f1:bd07:1a80:f61", port=8000, reload=True)