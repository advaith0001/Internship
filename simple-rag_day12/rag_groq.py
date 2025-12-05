import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders.text import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from groq import Groq

# 1. Load the text
loader = TextLoader("notes.txt")
docs = loader.load()
print("Loaded document:", docs)

# 2. Split into chunks
splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = splitter.split_documents(docs)
print("Chunks created:", chunks)

# 3. Embeddings
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma.from_documents(chunks, embeddings)

# 4. Initialize Groq LLM (FIXED)
client = Groq(
 

    api_key=os.getenv("GROQ_API_KEY") 

)

# 5. Ask user
question = input("Ask a question: ")

# 6. Retrieve best chunk
retriever = db.as_retriever()
results = retriever.invoke(question)
print("Retrieved results:", results)

best_doc = results[0]
print("Best document:", best_doc)

# 7. Extract content
if hasattr(best_doc, "page_content"):
    content = best_doc.page_content
else:
    content = best_doc.content

print("Chunk content used:", content)

# 8. Create prompt
prompt = (
    "Use ONLY the context below to answer.\n\n"
    "Context:\n" + content +
    "\n\nQuestion: " + question
)

# 9. Call Groq
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}]
)

# 10. Print answer
answer = response.choices[0].message.content
print("\nAnswer:", answer)
