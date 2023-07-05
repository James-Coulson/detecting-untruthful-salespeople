import os
import openai

from constant import META_PROMPT, PDS_1, TEST_TRANSCRIPT_1, TEST_TRANSCRIPT_2, PDS_2, TEST_TRANSCRIPT_3, TEST_TRANSCRIPT_4

openai.api_key = os.getenv("OPENAI_API_KEY")

print("Using API Key = " + os.getenv("OPENAI_API_KEY"))

print("")
print(" ---- Test Case 1 ---- ")
print("PDS")
print(PDS_1)
print("")
print("TRANSCRIPT")
print(TEST_TRANSCRIPT_1)
print("")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": META_PROMPT},
        {"role": "system", "content": PDS_1},
        {"role": "user", "content": TEST_TRANSCRIPT_1}
    ]
)
print("RESPONSE")
print(response["choices"][0]["message"]["content"])

print("")
print(" ---- Test Case 2 ---- ")
print("PDS")
print(PDS_1)
print("")
print("TRANSCRIPT")
print(TEST_TRANSCRIPT_2)
print("")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": META_PROMPT},
        {"role": "system", "content": PDS_1},
        {"role": "user", "content": TEST_TRANSCRIPT_2}
    ]
)
print("RESPONSE")
print(response["choices"][0]["message"]["content"])

print("")
print(" ---- Test Case 3 ---- ")
print("PDS")
print(PDS_2)
print("")
print("TRANSCRIPT")
print(TEST_TRANSCRIPT_3)
print("")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": META_PROMPT},
        {"role": "system", "content": PDS_2},
        {"role": "user", "content": TEST_TRANSCRIPT_3}
    ]
)
print("RESPONSE")
print(response["choices"][0]["message"]["content"])

print("")
print(" ---- Test Case 4 ---- ")
print("PDS")
print(PDS_2)
print("")
print("TRANSCRIPT")
print(TEST_TRANSCRIPT_4)
print("")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": META_PROMPT},
        {"role": "system", "content": PDS_2},
        {"role": "user", "content": TEST_TRANSCRIPT_4}
    ]
)
print("RESPONSE")
print(response["choices"][0]["message"]["content"])