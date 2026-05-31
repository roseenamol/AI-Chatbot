from ollama import chat

messages = []

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

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