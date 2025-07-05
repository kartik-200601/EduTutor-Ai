import os
from dotenv import load_dotenv

# This loads .env file from the current directory
load_dotenv()

print("HF_TOKEN:", os.getenv("HF_TOKEN"))
print("WATSONX_API_KEY:", os.getenv("WATSONX_API_KEY"))
print("GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))
print("PINECONE_API_KEY:", os.getenv("PINECONE_API_KEY"))