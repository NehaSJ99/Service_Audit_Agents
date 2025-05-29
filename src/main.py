from crew import build_crew
from dotenv import load_dotenv
import os
 
load_dotenv()

# Optional: safety check
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(" OPENAI_API_KEY not found in .env")

if __name__ == "__main__":
    crew = build_crew()
    result = crew.kickoff()
    print(result)
