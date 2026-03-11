import os 
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GEMINIX_API_KEY"))
model=genai.GenerativeModel("gemini-2.5-flash-lite")

def generate_answer(context,query):
    prompt=f"""
    
    You are an AI News Intelligence Analyst. Analyze the given news article and provide:
    1. Short summary (3 lines)
    2. Key entities (people, organizations, countries)
    3. Main topics
    4. Sentiment (Positive, Negative, Neutral)
    5. Why this news is important
    6. Possible impact
    
Use the news context to answer the question.
Return the result in a structured format.

    Context: {context}

    Question: {query}
    """
    response = model.generate_content(prompt)
    return response.text