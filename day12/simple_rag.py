import os
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer
import chromadb

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


text = open("notes.txt", "r", encoding="utf-8").read()


chunks = text.split(".")  


model = SentenceTransformer("all-MiniLM-L6-v2")
chroma = chromadb.Client().create_collection(name="rag")

for i, chunk in enumerate(chunks):
    chroma.add(
        ids=[str(i)],
        documents=[chunk],
        embeddings=[model.encode(chunk)]
    )


query = input("Ask a question: ")


results = chroma.query(
    query_embeddings=[model.encode(query)],
    n_results=1
)

best_chunk = results["documents"][0][0]


prompt = f"Answer using only this context:\n{best_chunk}\n\nQuestion: {query}"

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}]
)

print("\nANSWER:", response.choices[0].message.content)
