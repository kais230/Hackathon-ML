import openai
import json

openai.api_key = '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'

def preprocess_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    messages = [
        {"role": "system", "content": "You are a kind helpful budget manager assistant."},
    ]

    for category, expenses in data.items():
        messages.append({"role": "user", "content": f"My expenses for {category} are ${expenses}."})

    return messages

messages = preprocess_data('recom.json')

message = "Help me optimize my spendings from this information from the invoice: "

if message:
    messages.append(
        {"role": "user", "content": message},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

reply = chat.choices[0].message.content
print(f"ChatGPT: {reply}")
messages.append({"role": "assistant", "content": reply})

# Store the assistant's reply in a text file
with open('assistant_reply.txt', 'w') as file:
    file.write(reply)
