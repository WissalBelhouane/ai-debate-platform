# 🤖 AI Debate Platform

A multi-agent AI system where 4 specialized agents debate any topic using **100% free local AI** (no API costs, no internet required).

## 🚀 Quick Start

### 1. Install Requirements
```bash
# Install Ollama (local AI)
# Download from: https://ollama.com

# Pull the AI model
ollama pull llama3.2

# Clone this repository
git clone https://github.com/WissalBelhouane/ai-debate-platform.git
cd ai-debate-platform

# Install Python dependencies
pip install -r requirements.txt

2. Run a Debate
# Interactive mode
python run_debate.py

# Direct topic mode
python run_debate.py "Should artificial intelligence be regulated?"

🎯 Example Debate
🤖 DEBATE: Should homework be banned?
✅ Alex (PRO): Homework causes unnecessary stress...
📊 Taylor (FACT): Studies show 70% of students report homework stress...
❌ Sam (CON): Homework teaches discipline and reinforces learning...
⚖️ Jordan (MOD): Let's find a balanced approach...

🤖 The 4 AI Agents
<img width="956" height="283" alt="image" src="https://github.com/user-attachments/assets/9f26079d-0d8c-4628-91d6-4be6c98529cc" />

✨ Features
💰 100% Free: Uses local Ollama AI, no API costs

🎯 Any Topic: Politics, technology, education, ethics, fun topics

🏗️ Real Architecture: 4 specialized agents with different roles

📁 Auto-save: Transcripts saved automatically

🔧 Extensible: Easy to add new agents or features

🎮 Try These Topics
# Education
python run_debate.py "Should college be free?"

# Technology
python run_debate.py "Is social media harmful?"

# Environment
python run_debate.py "Should plastic be banned?"

# Fun & Creative
python run_debate.py "Are cats better than dogs?"
python run_debate.py "Should pineapple be on pizza?"

🛠️ Technical Details
AI Model: llama3.2 (4GB, excellent for debates)

Framework: LangChain for agent orchestration

Local Inference: Ollama for CPU/GPU inference

Requirements: Python 3.11+, 4GB RAM, 4GB storage

🔧 Customization
# Use different AI model
pro = ProAgent("Alex", model="llama3.2")

# Custom agent names
moderator = Moderator("Dr. Smith", model="llama3.2")

# Adjust debate rounds
orchestrator.run_debate(rounds=4, topic="Your Topic")

📈 Roadmap
Multi-agent architecture

Local AI integration

User input system

Web interface (Streamlit)

Enhanced fact-checking

Debate analytics

graph TB
    User[User Input Topic] --> Orchestrator[Debate Orchestrator]
    
    Orchestrator --> Pro[Pro Agent 🤖]
    Orchestrator --> Con[Con Agent 🤖]
    Orchestrator --> Moderator[Moderator Agent ⚖️]
    Orchestrator --> FactChecker[Fact-Checker Agent 📊]
    
    Pro --> Debate[Real-time Debate]
    Con --> Debate
    Moderator --> Debate
    FactChecker --> Debate
    
    Debate --> Output[Transcript + Analysis]
    
    style Pro fill:#e1f5e1
    style Con fill:#fdeaea
    style Moderator fill:#e3f2fd
    style FactChecker fill:#fff3e0

🤝 Contributing
1.Fork the repository

2.Create a feature branch

3.Commit your changes

4.Push to the branch

5.Open a Pull Request


