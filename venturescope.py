from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
import os

load_dotenv()

# 1. Load startup knowledge base
loader = TextLoader("data/startup_cases.txt")
documents = loader.load()

# 2. Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(documents)

# 3. Create embeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4. Create FAISS vector store
vectorstore = FAISS.from_documents(chunks, embedding_model)

# 5. Initialize Groq LLM
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.2
)

# 6. User startup idea
startup_idea = input("\n Enter your startup idea: ").strip()

if not startup_idea:
    print("Startup idea cannot be empty.")
    exit()


# 7. Retrieve relevant evidence
retrieved_docs = vectorstore.similarity_search(startup_idea, k=3)

context = "\n".join([doc.page_content for doc in retrieved_docs])

# 8. Build RAG prompt
prompt = f"""
You are a startup feasibility advisor.

STRICT RULES:
- Use ONLY the evidence provided below.
- Do NOT add general knowledge, assumptions, or trends.
- If information is missing, explicitly say "Not present in evidence".
- Do NOT infer beyond the evidence.

Startup Idea:
{startup_idea}

Evidence:
{context}

Output format:
1. Market Demand (only from evidence)
2. Competition Level (only from evidence)
3. Key Risks (only from evidence)
4. Evidence-Based Verdict

If evidence is insufficient, say so clearly.
"""


# 9. Generate response
response = llm.invoke(prompt)

print("\n Startup Feasibility Report:\n")
print(response.content)

print("\n---")
print(
    "Note: This feasibility analysis is generated using a limited, curated knowledge base "
    "and is intended to demonstrate how Retrieval-Augmented Generation (RAG) systems reason "
    "over available evidence. The output should be interpreted as decision support, not as a "
    "definitive market or business assessment."
)
