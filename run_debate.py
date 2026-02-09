#!/usr/bin/env python3
"""
AI Debate System - User provides topic at runtime
Usage: python run_debate.py "Your topic here"
"""

import sys
import time

# ---------- GET USER'S TOPIC ----------
if len(sys.argv) < 2:
    print("🤖 AI DEBATE PLATFORM")
    print("=" * 60)
    print("Please provide a debate topic!")
    print()
    print("USAGE:")
    print("  Option 1: python run_debate.py \"Your topic here\"")
    print("  Example:  python run_debate.py \"Should homework be banned?\"")
    print()
    print("  Option 2: python run_debate.py")
    print("  (Will prompt for topic interactively)")
    print()
    
    # Interactive input
    topic = input("Enter debate topic: ").strip()
    if not topic:
        print("❌ No topic provided. Exiting.")
        sys.exit(1)
else:
    # Topic from command line
    topic = " ".join(sys.argv[1:])

print(f"\n🎯 DEBATE TOPIC: {topic}")
print("=" * 60)

# ---------- CONTINUE WITH YOUR EXISTING CODE ----------
# Import your agents
from pro_agent import ProAgent
from con_agent import ConAgent
from moderator import Moderator
from fact_checker import FactChecker
from orchestrator_fixed import DebateOrchestrator

# Get number of rounds
try:
    rounds_input = input("\nNumber of debate rounds (1-5, default 2): ").strip()
    rounds = int(rounds_input) if rounds_input else 2
    rounds = max(1, min(5, rounds))
except:
    rounds = 2
    print("Using default: 2 rounds")

# Initialize
print("\n🤖 Initializing AI agents...")
pro = ProAgent("Alex")
con = ConAgent("Sam")
moderator = Moderator("Jordan")
fact_checker = FactChecker("Taylor")

orchestrator = DebateOrchestrator()
orchestrator.add_agent(pro)
orchestrator.add_agent(con)
orchestrator.add_agent(moderator)
orchestrator.add_agent(fact_checker)

# Set USER'S TOPIC (not hardcoded!)
orchestrator.set_topic(topic)

# Run debate
print(f"\n🎤 Starting debate about: {topic}")
print("=" * 60)

history = orchestrator.run_debate(rounds=rounds)

# Save transcript
filename = f"debate_{topic.replace(' ', '_').replace('?', '')[:30]}.txt"
with open(filename, 'w', encoding='utf-8') as f:
    f.write(f"Topic: {topic}\n")
    f.write(f"Rounds: {rounds}\n")
    f.write("=" * 60 + "\n\n")
    for line in history:
        f.write(line + "\n\n")

print(f"\n💾 Transcript saved to: {filename}")
print("✅ Debate complete!")