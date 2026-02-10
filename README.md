# 🤖 AI Debate Platform

A fully local, multi-agent AI debate system where different AI personas argue, moderate, and fact-check any topic you give them — **100% free, offline, and open-source**.

---

## 🚀 Quick Start

### 1️⃣ Install Ollama
Download and install Ollama from:  
👉 https://ollama.com

Then pull the model:
```bash
ollama pull llama3.2

### 2️⃣ Run the System
# Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-debate-platform.git
cd ai-debate-platform

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux / Mac

# Install dependencies
pip install -r requirements.txt

# Start a debate
python run_debate.py "Should homework be banned?"
🎯 What It Does
You give a topic → 4 AI agents debate it

🤖 Pro Agent – Argues FOR the topic

❌ Con Agent – Argues AGAINST the topic

⚖️ Moderator – Controls debate flow

📊 Fact-Checker – Verifies claims

✅ Uses local AI only
✅ No API keys required
✅ Works offline
✅ $0 cost forever

📊 Example Output
🎤 DEBATE: Should homework be banned?

🤖 Alex (PRO): Homework causes student stress and reduces family time...
📊 Taylor (FACT): Studies show 70% of students report homework stress...
❌ Sam (CON): Homework teaches discipline and reinforces learning...
⚖️ Jordan (MOD): Let's consider both educational value and student well-being...
🎮 Try These Topics
# Education
python run_debate.py "Should college be free?"

# Technology
python run_debate.py "Is AI dangerous?"

# Society
python run_debate.py "Should social media have age limits?"

# Fun
python run_debate.py "Are cats better than dogs?"

# Environment
python run_debate.py "Should plastic be banned?"
🏗️ Architecture
User Topic → Orchestrator → 4 Agents → Debate → Transcript
    │           │           │    │        │         │
    └───────────┼───────────┼────┼────────┼─────────┘
                ↓           ↓    ↓        ↓
           Controls   Pro   Con  Mod   Fact-check
                      │     │    │         │
                      └─────┼────┼─────────┘
                            ↓    ↓
                      Real-time Debate
📁 Project Structure
ai-debate-platform/
├── agents/
│   ├── agent_base.py
│   ├── pro_agent.py
│   ├── con_agent.py
│   ├── moderator.py
│   └── fact_checker.py
├── core/
│   └── orchestrator_fixed.py
├── run_debate.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
🛠️ Tech Stack
Python 3.11+

LangChain (agent framework)

Ollama (local LLM runtime)

LLaMA 3.2

Streamlit (web interface)

🌐 Web Interface
Run the web app:

streamlit run app.py
Open in your browser:
👉 http://localhost:8501

Features
🎨 Animated gradient UI

📱 Fully responsive

⌨️ Typing effects

💾 Download debate transcripts

⚙️ Custom agent names, rounds & models

🎯 One-click topic buttons

📈 Debate statistics

🔧 Customization
Change AI Model
Edit agent_base.py:

def __init__(self, name, role, model="llama3.2"):
Available Models
Model	Size	Notes
llama3.2	~4GB	Best balance (recommended)
llama2	~3.8GB	Lightweight
mistral	~4.1GB	Very fast
gemma2	~9GB	Highest quality
📈 Performance
⏱️ Debate duration: 30 sec – 2 min per round

💾 RAM usage: ~4GB

💽 Storage: < 4.5GB

💰 Cost: $0

⚡ Response time: 2–5 sec per agent

🤝 Contributing
Fork the repository

Create a feature branch

git checkout -b feature/AmazingFeature
Commit your changes

git commit -m "Add AmazingFeature"
Push to your branch

git push origin feature/AmazingFeature
Open a Pull Request 🚀

📄 License
MIT License — see LICENSE file for details.

🙏 Acknowledgments
Ollama – Local AI runtime

LangChain – Agent orchestration

Meta – LLaMA models

Streamlit – Web UI

Open-source community ❤️

