import os
from openai import OpenAI
from mistralai import Mistral
from google import genai

def open_ai_response(system_prompt,user_prompt):
    client = OpenAI(api_key= os.environ.get("api_key_open_ai_2"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
    ],
        max_tokens=200,
        temperature=0.7,
        stream=False
    )

    return response.choices[0].message.content

def mistral_response(system_prompt,user_prompt):
    model = "mistral-large-latest"

    client = Mistral(api_key=os.environ["mistral_api_key"])

    chat_response = client.chat.complete(
        model = model,
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user","content": user_prompt},
        ]
    )

    return chat_response.choices[0].message.content

def gemini_response(system_prompt,user_prompt):
    
    client = genai.Client(api_key="GOOGLE_API_KEY")
    prompt = f"""system prompt : {system_prompt} 
    user prompt : {user_prompt}"""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt]
    )
    return response.text
    