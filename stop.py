from openai import OpenAI
client = OpenAI(api_key="", base_url="https://api.deepseek.com/beta")

response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[
        {"role": "user", "content": "Axel has 9900270 silver pesos and 1735148 gold pesos. He visits his friend Anna who has 9 times as many silver pesos as he has and 9356776 more gold pesos. What's the total number of pesos they have together?"},
    ],
)
response_new = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[
        {"role": "user", "content": response.choices[0].message.reasoning_content},
    ],
)

print("reasoning tokens: ", response_new.choices[0].message.reasoning_content)
print("=====================================================")
print("result: ", response_new.choices[0].message.content) # null

