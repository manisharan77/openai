import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
