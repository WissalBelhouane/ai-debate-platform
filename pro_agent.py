# pro_agent.py - Agent that argues FOR topics using REAL LOCAL AI
from agent_base import DebateAgent

class ProAgent(DebateAgent):
    """Agent that argues IN FAVOR using local AI"""
    
    def __init__(self, name="Alex", model="llama3.2"):
        super().__init__(name, "pro", model)
    
    def speak(self, topic, context=""):
        """Generate pro argument using REAL local AI"""
        self.remember(topic)
        
        prompt = f"""You are a debate expert arguing STRONGLY IN FAVOR of this topic.
        Topic: {topic}
        
        Give one strong, persuasive argument in 2-3 sentences.
        Be convincing and use logical reasoning.
        
        Your response should start with: 'I strongly believe that...'"""
        
        if context:
            prompt += f"\n\nContext from previous discussion: {context}"
        
        response = self.llm.invoke(prompt)
        return f"{self.name} (PRO): {response}"