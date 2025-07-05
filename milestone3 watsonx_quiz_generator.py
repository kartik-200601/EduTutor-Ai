import os
from dotenv import load_dotenv
from pathlib import Path

# ✅ CORRECT: Two underscores before and after: _file_
env_path =Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Get WatsonX API key from .env
api_key = os.getenv("WATSONX_API_KEY")

if not api_key:
    raise ValueError("WatsonX API key is missing.")

# Simulate quiz generation
def get_quiz(prompt):
    return f"""
1. What is the main pigment involved in photosynthesis?
    a) Hemoglobin
    b) Chlorophyll
    c) Myoglobin
    d) Keratin
Answer: b

2. What gas is absorbed during photosynthesis?
    a) Oxygen
    b) Nitrogen
    c) Carbon Dioxide
    d) Hydrogen
Answer: c

3. Photosynthesis occurs in which cell organelle?
    a) Mitochondria
    b) Nucleus
    c) Ribosome
    d) Chloroplast
Answer: d

4. What is the by-product of photosynthesis?
    a) CO2
    b) O2
    c) Glucose
    d) Lactic acid
Answer: b

5. What is the source of energy for photosynthesis?
    a) Moonlight
    b) Fire
    c) Sunlight
    d) Electric bulb
Answer: c
"""

# Run it
prompt = "Generate 5 multiple-choice quiz questions on the topic: Photosynthesis"
quiz = get_quiz(prompt)

print("Generated Quiz:\n")
print(quiz)