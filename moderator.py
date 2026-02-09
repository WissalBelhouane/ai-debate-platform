# moderator.py - Moderator agent to control debate
from agent_base import DebateAgent

class Moderator(DebateAgent):
    """Moderator agent that controls debate flow"""
    
    def __init__(self, name="Jordan", model="llama3.2"):
        super().__init__(name, "moderator", model)
    
    def introduce_topic(self, topic):
        """Introduce debate topic"""
        prompt = f"""You are a debate moderator. Introduce this debate topic professionally.
        Topic: {topic}
        
        Give a brief, neutral introduction in 2 sentences."""
        
        response = self.llm.invoke(prompt)
        return f"{self.name} (MODERATOR): {response}"
    
    def transition(self, round_num, next_speaker):
        """Transition between speakers"""
        prompt = f"""As debate moderator, transition to the next speaker.
        Round: {round_num}
        Next speaker: {next_speaker}
        
        Keep it brief (1 sentence)."""
        
        response = self.llm.invoke(prompt)
        return f"{self.name} (MODERATOR): {response}"
    
    def conclude(self, topic):
        """Conclude the debate"""
        prompt = f"""As debate moderator, conclude this debate.
        Topic: {topic}
        
        Give a brief, neutral conclusion in 2 sentences."""
        
        response = self.llm.invoke(prompt)
        return f"{self.name} (MODERATOR): {response}"