from model_connections import open_ai_response, mistral_response, gemini_response

def open_ai_bot(prompt):
    # Call the OpenAI API with the prompt
    system_prompt = "You are a helpful assistant"
    response = open_ai_response(system_prompt, prompt)
    return response

def mistral_bot(prompt):
    # Call the Mistral API with the prompt
    system_prompt = "You are a helpful assistant"
    response = mistral_response(system_prompt, prompt)
    return response

def gemini_bot(prompt):
    # Call the Gemini API with the prompt
    system_prompt = "You are a helpful assistant"
    response = gemini_response(system_prompt, prompt)
    return response
