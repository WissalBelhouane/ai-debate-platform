# orchestrator_fixed.py - Works with ANY topic automatically
import time

class DebateOrchestrator:
    """Orchestrator that automatically adapts to any topic"""
    
    def __init__(self):
        self.agents = {}
        self.topic = ""
        self.history = []
        self.round = 0
        self.last_argument = ""  # Track the last argument made
    
    def add_agent(self, agent):
        """Add an agent to the system"""
        self.agents[agent.role] = agent
        print(f"✅ Added agent: {agent.name} ({agent.role})")
    
    def set_topic(self, topic):
        """Set the debate topic - system will automatically use this"""
        self.topic = topic
        print(f"🎯 Debate topic set: {topic}")
        self.history.append(f"TOPIC: {topic}")
    
    def run_debate(self, rounds=2):
        """Run debate - automatically uses the set topic"""
        print(f"\n🎤 STARTING DEBATE: {self.topic}")
        print("=" * 60)
        
        # 1. Moderator introduces ACTUAL topic
        if "moderator" in self.agents:
            intro = self.agents["moderator"].introduce_topic(self.topic)
            print(f"\n{intro}")
            self.history.append(intro)
            time.sleep(1)
        
        for round_num in range(1, rounds + 1):
            self.round = round_num
            print(f"\n🔄 ROUND {round_num}")
            print("-" * 40)
            
            # 2. PRO argues about ACTUAL topic
            if "pro" in self.agents:
                print(f"\n🤖 {self.agents['pro'].name} (PRO) is speaking...")
                pro_response = self.agents["pro"].speak(self.topic)
                print(f"   {pro_response}")
                self.history.append(pro_response)
                self.last_argument = pro_response  # Store for fact-checking
                time.sleep(1)
            
            # 3. Fact-checker checks ACTUAL argument (not hardcoded!)
            if "fact_checker" in self.agents:
                print(f"\n📊 {self.agents['fact_checker'].name} (FACT) is checking...")
                
                # Get just the argument text (remove "Alex (PRO): ")
                if ": " in self.last_argument:
                    argument_text = self.last_argument.split(": ", 1)[1]
                else:
                    argument_text = self.last_argument
                
                # Fact-check the ACTUAL argument about the ACTUAL topic
                fact_response = self.agents["fact_checker"].verify_claim(
                    argument_text[:150],  # First 150 chars of real argument
                    f"Debate about {self.topic}"
                )
                print(f"   {fact_response}")
                self.history.append(fact_response)
                time.sleep(1)
            
            # 4. CON argues about ACTUAL topic  
            if "con" in self.agents:
                print(f"\n🤖 {self.agents['con'].name} (CON) is speaking...")
                con_response = self.agents["con"].speak(self.topic)
                print(f"   {con_response}")
                self.history.append(con_response)
                time.sleep(1)
            
            # 5. Moderator controls debate about ACTUAL topic
            if "moderator" in self.agents:
                print(f"\n⚖️ {self.agents['moderator'].name} (MOD) is moderating...")
                if round_num < rounds:
                    transition = self.agents["moderator"].transition(
                        round_num, 
                        f"Round {round_num + 1} about {self.topic}"
                    )
                else:
                    transition = self.agents["moderator"].conclude(self.topic)
                
                print(f"   {transition}")
                self.history.append(transition)
                time.sleep(1)
        
        print("\n" + "=" * 60)
        print(f"🏁 DEBATE COMPLETE: All arguments were about '{self.topic}'")
        print(f"📊 Total exchanges: {len(self.history)}")
        
        return self.history