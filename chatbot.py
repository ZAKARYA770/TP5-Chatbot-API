import requests
import json

# Configuration OpenRouter
API_KEY = "sk-or-v1-d8728c71..." # Copier l-key dialk hna
MODEL = "google/gemini-2.0-flash-001"

def chat():
    print("--- Simple Chatbot (TP 5) ---")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']: break

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            data=json.dumps({
                "model": MODEL,
                "messages": [{"role": "user", "content": user_input}]
            })
        )
        
        result = response.json()
        print("Bot:", result['choices'][0]['message']['content'])

if __name__ == "__main__":
    chat()
