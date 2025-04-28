from tools.openai_tool import ask_openai

class BirthmarkOpenAIAgent:
    def run(self, image_description):
        print("[Agent] Sending image description to OpenAI...")
        prompt = f"Based on this description of a birthmark, assess the risk (Low, Medium, High): {image_description}"
        answer = ask_openai(prompt)
        return answer