# fact_checker.py - Fact-checker agent
from agent_base import DebateAgent

class FactChecker(DebateAgent):
    """Fact-checker agent that verifies claims"""
    
    def __init__(self, name="Taylor", model="llama3.2"):
        super().__init__(name, "fact_checker", model)
    
    def verify_claim(self, claim, context=""):
        """Verify a claim made during debate"""
        prompt = f"""You are a fact-checker analyzing a debate claim.
        Claim to verify: "{claim}"
        
        Analyze this claim for accuracy. Respond in 2 sentences.
        Start with: "Fact check:"
        
        Use a neutral, informative tone."""
        
        if context:
            prompt += f"\n\nContext: {context}"
        
        response = self.llm.invoke(prompt)
        return f"{self.name} (FACT-CHECKER): {response}"