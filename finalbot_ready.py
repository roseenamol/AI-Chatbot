from ollama import chat

# System prompt
messages = [
    {
        "role": "system",
        "content": "You are a helpful, friendly AI assistant. Give clear and concise answers."
    }
]

print("=== AI Chatbot ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    try:
        response = chat(
            model="qwen2.5:1.5b",
            messages=messages
        )

        bot_reply = response["message"]["content"]

        print("Bot:", bot_reply)

        messages.append(
            {
                "role": "assistant",
                "content": bot_reply
            }
        )

    except Exception as e:
        print("Error:", e)