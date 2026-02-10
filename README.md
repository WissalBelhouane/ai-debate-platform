# 🤖 AI Debate Platform

![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/ai-debate-platform?style=flat-square)
![GitHub license](https://img.shields.io/github/license/YOUR_USERNAME/ai-debate-platform?style=flat-square)
![Python version](https://img.shields.io/badge/python-3.11%2B-blue?style=flat-square)
![Platform](https://img.shields.io/badge/platform-local--AI-success?style=flat-square)

A fully local, multi-agent AI debate system where different AI personas argue, moderate, and fact-check any topic you give them — **100% free, offline, and open-source**.

---

## 🚀 Quick Start

### 1️⃣ Install Ollama
Download and install Ollama from:  
👉 https://ollama.com

Then pull the model:
```bash
ollama pull llama3.2
```

---

### 2️⃣ Run the System
```bash
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
```

---

## 🎯 What It Does

You give a topic → **4 AI agents debate it**

- 🤖 **Pro Agent** – Argues FOR the topic  
- ❌ **Con Agent** – Argues AGAINST the topic  
- ⚖️ **Moderator** – Controls debate flow  
- 📊 **Fact-Checker** – Verifies claims  
<img width="956" height="283" alt="Screenshot 2026-02-09 170752" src="https://github.com/user-attachments/assets/007d03a4-c7f7-478c-8e23-63307253f7ab" />

✅ Uses **local AI only**  
✅ **No API keys required**  
✅ **Works offline**  
✅ **$0 cost forever**

---

## 📊 Example Output

```text
🎤 DEBATE: Should homework be banned?

🤖 Alex (PRO): Homework causes student stress and reduces family time...
📊 Taylor (FACT): Studies show 70% of students report homework stress...
❌ Sam (CON): Homework teaches discipline and reinforces learning...
⚖️ Jordan (MOD): Let's consider both educational value and student well-being...
```

---

## 🎮 Try These Topics

```bash
python run_debate.py "Should college be free?"
python run_debate.py "Is AI dangerous?"
python run_debate.py "Should social media have age limits?"
python run_debate.py "Are cats better than dogs?"
python run_debate.py "Should plastic be banned?"
```

---

## 🏗️ Architecture

```text
User Topic → Orchestrator → 4 Agents → Debate → Transcript

<img width="1473" height="813" alt="Screenshot 2026-02-09 171213" src="https://github.com/user-attachments/assets/3ffc72b7-9774-44b1-9098-b5aeeaf8ddc7" />

```

## 🛠️ Tech Stack

- **Python 3.11+**
- **LangChain**
- **Ollama**
- **LLaMA 3.2**
- **Streamlit**

---

## 🌐 Web Interface

```bash
streamlit run app.py


Open: http://localhost:8501
```
---

## 🤝 Contributing

1. Fork the repository  
2. Create a feature branch  
3. Commit your changes  
4. Push to your branch  
5. Open a Pull Request  

---

## 📄 License

MIT License

---

## ⭐ Support

If this project helped you, please give it a ⭐ on GitHub!
