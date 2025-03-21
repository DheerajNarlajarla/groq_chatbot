import json
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from groq import Groq

client = Groq(
    # This is the default and can be omitted
    #api_key=os.environ.get("GROQ_API_KEY"),
    api_key = "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"
)
query = 0
prompt = input("query:\n")

chat_completion = client.chat.completions.create(
  messages=[
    {
      "role": "system",
      "content": "you are a helpful assistant, that can guide and resolve problems in business and tech world."
    },
    {
      "role": "user",
      "content": prompt,
    }
  ],
      # Replace the decommissioned model with an active model.
      # You can find a list of active models in the Groq documentation:
      # https://console.groq.com/docs/models
  model="llama-3.3-70b-versatile",  # Example: Using Llama 3.3
)
print(chat_completion.choices[0].message.content)

prompts = []
responses = []
n = 5 # Define n, for example, to get 5 prompts

while prompt != "end":
  # Instead of assigning to a specific index, append the prompt to the list
  prompts.append(prompt)

  # Get n prompts from user
  for i in range(n):
    prompt = input("query:\n") # Get new prompt from user and assign to prompt variable
    if prompt == "end": # Allow user to end loop by typing "end"
      break
    prompts.append(prompt)
    response = client.chat.completions.create( # Move completion call inside the loop
      messages=[
        {
          "role": "system",
          "content": "you are a helpful assistant, that can guide and resolve problems in business and tech world."
        },
        {
          "role": "user",
          "content": prompt,
        }
      ],
      model="qwen-2.5-coder-32b",
    ).choices[0].message.content

    responses.append(response)
    print(response)



print(responses)
print(prompts)

# Save prompts and responses to a JSON file
data = {"prompts": prompts, "responses": responses}
with open("prompts_responses.json", "w") as f:
    json.dump(data, f) 
# Load prompts and responses from the JSON file
with open("prompts_responses.json", "r") as f:
    data = json.load(f)
    prompts = data["prompts"]
    responses = data["responses"]
print(prompts[-1])
print(responses)