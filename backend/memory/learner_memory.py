from typing import Dict


class LearnerMemory:

    def __init__(self):
        # Stores all learner sessions
        self.sessions: Dict[str, dict] = {}

    # ----------------------------------------
    # Create New Session
    # ----------------------------------------
    def create_session(self, learner_id: str, roadmap):

        print(f"\nCreating session for {learner_id}")

        self.sessions[learner_id] = {

            "learner_id": learner_id,

            "current_index": 0,

            "current_topic": roadmap["roadmap"][0]["title"],

            "completed_topics": [],

            "roadmap": roadmap,

            "quiz_history": [],

            "average_score": 0,

            "weak_topics": []

        }

        print("Session Created Successfully")
        print(self.sessions)

        return self.sessions[learner_id]

    # ----------------------------------------
    # Get Session
    # ----------------------------------------
    def get_session(self, learner_id: str):

        print(f"\nSearching Session for {learner_id}")
        print("Available Sessions:", list(self.sessions.keys()))

        return self.sessions.get(learner_id)

    # ----------------------------------------
    # Update Session After Quiz
    # ----------------------------------------
    def update_after_quiz(
        self,
        learner_id: str,
        topic: str,
        percentage: float,
        weak_topics: list,
        move_next: bool
    ):

        session = self.sessions.get(learner_id)

        if session is None:
            print("Session Not Found")
            return None

        # Save Quiz History
        session["quiz_history"].append({

            "topic": topic,

            "score": percentage

        })

        # Save Weak Topics
        session["weak_topics"] = weak_topics

        # Calculate Average Score
        scores = [
            quiz["score"]
            for quiz in session["quiz_history"]
        ]

        session["average_score"] = round(
            sum(scores) / len(scores),
            2
        )

        # Move to Next Topic
        if move_next:

            session["completed_topics"].append(topic)

            session["current_index"] += 1

            roadmap = session["roadmap"]["roadmap"]

            if session["current_index"] < len(roadmap):

                session["current_topic"] = roadmap[
                    session["current_index"]
                ]["title"]

            else:

                session["current_topic"] = "Course Completed"

        print("\nUpdated Session")
        print(session)

        return session


# Singleton Instance
learner_memory = LearnerMemory()