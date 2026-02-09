# con_agent.py - Agent that argues AGAINST topics using REAL LOCAL AI
from agent_base import DebateAgent

class ConAgent(DebateAgent):
    """Agent that argues AGAINST using local AI"""
    
    def __init__(self, name="Sam", model="llama3.2"):
        super().__init__(name, "con", model)
    
    def speak(self, topic, context=""):
        """Generate con argument using REAL local AI"""
        self.remember(topic)
        
        prompt = f"""You are a debate expert arguing STRONGLY AGAINST this topic.
        Topic: {topic}
        
        Give one strong, persuasive counter-argument in 2-3 sentences.
        Be convincing and use logical reasoning.
        
        Your response should start with: 'I strongly oppose this because...'"""
        
        if context:
            prompt += f"\n\nContext from previous discussion: {context}"
        
        response = self.llm.invoke(prompt)
        return f"{self.name} (CON): {response}"