import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(api_key=os.getenv("GROQ_API_KEY"))


blog_text = input("Enter the blog : ")


prompt = "Summarize the following blog in simple, clear language:\n\n" + blog_text


response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user",
                "content": prompt}]
)


summary = response.choices[0].message.content
print("\n=== SUMMARY ===\n")
print(summary)
