from openai import OpenAI

api_key = "<your_api_key>"
client = OpenAI(
    api_key = api_key
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis and skilled in all type of general tasks like alexa and google cloud"},
        {
            "role": "user",
            "content": "write a simplified explanation about recursion in computer programming"
        }
    ]
)

print(completion.choices[0].message.content)