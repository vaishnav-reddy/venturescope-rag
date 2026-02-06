# VentureScope 
### A Prototype Retrieval-Augmented Generation (RAG) System for Startup Feasibility Analysis

VentureScope is a **prototype RAG-based decision-support system** that analyzes startup ideas
using a curated knowledge base and produces **evidence-grounded feasibility insights**.

This project is designed for **learning and demonstration purposes**, focusing on how
Retrieval-Augmented Generation (RAG) systems reason over retrieved evidence while explicitly
handling uncertainty.

---

##  Project Objective

Traditional Large Language Models (LLMs) often generate confident answers without verifying
their factual grounding.

VentureScope demonstrates how RAG can be used to:
- Ground responses in retrieved evidence
- Avoid hallucinated facts
- Explicitly acknowledge missing or insufficient information
- Act as a **decision-support system**, not an oracle

---

##  What the System Does

- Accepts a startup idea as user input (CLI-based)
- Retrieves relevant startup-related knowledge using semantic search
- Injects retrieved evidence into an LLM prompt
- Generates a structured feasibility report
- Clearly states when evidence is insufficient

---

##  High-Level Architecture

1. **User Input**
   - The user enters a startup idea via the command line.

2. **Document Retrieval**
   - Startup-related knowledge is split into chunks.
   - Chunks are embedded using a sentence-transformer model.
   - FAISS is used to retrieve semantically relevant chunks.

3. **RAG Pipeline**
   - Retrieved evidence is injected into a structured prompt.
   - The LLM reasons only over the provided evidence.

4. **Feasibility Analysis Output**
   - Market Demand
   - Competition Level
   - Key Risks
   - Evidence-Based Verdict
   - Explicit disclaimer on limitations

---

##  Important Note on Accuracy & Scope

This system uses a **limited, curated knowledge base**.

It is intended to demonstrate:
- How retrieval context affects reasoning
- How uncertainty is handled responsibly in RAG systems

It is **NOT** intended to:
- Provide real-world market guarantees
- Replace professional business or market research

The output should be interpreted strictly as **decision support**.

---

##  Tech Stack

- **Language**: Python
- **Framework**: LangChain
- **Vector Database**: FAISS (CPU)
- **Embeddings**: Sentence Transformers
- **LLM Provider**: Groq
- **Interaction**: Command Line Interface (CLI)

---

##  Project Structure

```
venturescope-rag/
│
├── data/
│ └── startup_cases.txt # Curated startup knowledge base
│
├── venturescope.py # Main RAG pipeline
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── .gitignore # Git ignore rules
└── .env # Environment variables (NOT committed)

```

---

##  How to Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/vaishnav-reddy/VentureScope-RAG.git
cd VentureScope-RAG
```
### Step 2: Create a Virtual Environment (Recommended)
```
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate  # macOS/Linux
```
### Step 3: Install Dependencies

```
pip install -r requirements.txt
```
### Step 4: Configure API Key
```
GROQ_API_KEY=your_groq_api_key_here
```
Make sure .env is listed in .gitignore.

### Step 5: Run the Application

python venturescope.py

### Step 6: Enter a Startup Idea
Example:
 Enter your startup idea: AI-based attendance system for colleges in India

The system will generate a feasibility report based on retrieved evidence.

Example Output (Simplified)

Startup Feasibility Report:

1. Market Demand: Not present in evidence
2. Competition Level: High competition in SaaS markets
3. Key Risks:
   - Lack of product-market fit
   - High customer acquisition cost
   - Ignoring user feedback
4. Evidence-Based Verdict: Insufficient evidence to fully assess feasibility.

---
Note: This feasibility analysis is generated using a limited, curated knowledge base and
is intended to demonstrate how Retrieval-Augmented Generation (RAG) systems reason over
available evidence.



