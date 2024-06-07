# session_manager.py

from typing import List, Dict

class SessionManager:
    def __init__(self):
        self.sessions: Dict[str, List[dict]] = {}

    def store_questions(self, session_id: str, questions: List[dict]):
        self.sessions[session_id] = questions

    def get_questions(self, session_id: str) -> List[dict]:
        return self.sessions.get(session_id, [])
session_manager = SessionManager()
