from openai import OpenAI

client = OpenAI(api_key='')

conversation = []

print("Assistant: Hello, I am GPT-4o-mini! How can I help you today? (type 'exit' to finish the conversation)")

while True:
  user_query = input("User: ").lower()
  if user_query == 'exit':
    break

  conversation.append({"role": "user", "content": user_query})
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=conversation
  )
  assistant_answer = response.choices[0].message.content
  conversation.append({"role": "assistant", "content": assistant_answer})
  print("Assistant: " + assistant_answer)
