# agent_base.py - Base class for all agents
from langchain_community.llms import Ollama

class DebateAgent:
    """Base class for all debate agents using LOCAL AI"""
    
    def __init__(self, name, role, model="llama3.2"):
        self.name = name
        self.role = role  # "pro", "con", "moderator", "fact_checker"
        self.model = model
        self.llm = Ollama(model=model)
        self.memory = []  # Store conversation history
    
    def speak(self, topic, context=""):
        """Generate response - to be implemented by child classes"""
        raise NotImplementedError("Child classes must implement speak()")
    
    def remember(self, statement):
        """Store statement in memory"""
        self.memory.append(statement[:100])  # Store first 100 chars
    
    def get_memory(self):
        """Get recent memory"""
        return self.memory[-3:] if self.memory else []