import openai

# Init OpenAI API key
openai.api_key = "your-openai-api-key-here"

def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # or "gpt-3.5-turbo" if we want to use
            messages=[
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[OpenAI Tool] Error: {e}")
        return None