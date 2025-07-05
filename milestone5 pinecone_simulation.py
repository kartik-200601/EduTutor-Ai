# milestone5/pinecone_simulation.py

quiz_vectors = {
    "photosynthesis": [
        "What is the main pigment involved in photosynthesis?",
        "What gas is absorbed during photosynthesis?",
        "Photosynthesis occurs in which organelle?"
    ],
    "machine learning": [
        "What is supervised learning?",
        "Define overfitting in machine learning.",
        "What is a decision tree?"
    ],
    "python programming": [
        "What is a list in Python?",
        "Difference between tuple and list?",
        "Explain Python dictionaries."
    ]
}

def query_pinecone_simulated(topic):
    print(f"\n🔍 Searching for quiz questions on: {topic}")
    results = quiz_vectors.get(topic.lower(), [])
    
    if not results:
        print("❌ No questions found for this topic.")
    else:
        print("✅ Found questions:")
        for q in results:
            print(f"- {q}")

if __name__ == '__main__':
    # Simulate query
    query_topic = "Photosynthesis"  # You can change this
    query_pinecone_simulated(query_topic)