# 🧠 RAGNova: Advanced Retrieval-Augmented Generation with Document Intelligence

RAGNova is a modular and adaptive Retrieval-Augmented Generation (RAG) system designed for reasoning over **layout-rich, multimodal, and noisy documents**. This project is part of an M.Tech thesis in Artificial Intelligence and leverages **deep document understanding**, **hybrid semantic retrieval**, and **confidence-calibrated generation** to build a smarter, explainable, and trustworthy QA system.

---
## System Architecture

![image](https://github.com/user-attachments/assets/d80950c7-3742-4eea-9e91-41e53853774a)


## 🚀 Features

- 🧾 **Layout-Aware Document Parsing** using LayoutLM and TableLab
- 🔍 **Hybrid Retrieval Engine** (Dense + Structural Search with Sentence-BERT and FAISS)
- 🧠 **RAG Generator** based on T5 or GPT-2/Neo for contextual answer generation
- ✅ **Confidence Estimation** via hybrid conformal prediction and anomaly detection
- 📄 Works with scanned documents, PDFs, financial reports, and structured forms
- 🧪 Evaluation-ready with custom datasets (DocVQA, CORD, Legal PDFs)

---

## 📁 Project Structure

```
rag-nova/
│
├── 📂data/
│   ├── raw/               # Sample PDFs, JSONs, OCR output
│   └── processed/         # Chunked docs, embeddings, QA pairs
│
├── 📂models/
│   ├── layoutlm/          # Layout-aware encoder configs
│   ├── retriever/         # FAISS/SBERT retriever models
│   └── generator/         # T5 or GPT-based generator models
│
├── 📂notebooks/
│   ├── document_parser.ipynb
│   ├── retriever_eval.ipynb
│   └── generator_eval.ipynb
│
├── 📂src/
│   ├── config.py
│   ├── document_parser.py
│   ├── retriever.py
│   ├── generator.py
│   ├── confidence.py
│   └── rag_pipeline.py
│
├── 📂deployment/
│   ├── streamlit_app.py
│   ├── Dockerfile
│   └── api_server.py
│
├── 📄README.md
├── 📄requirements.txt
├── 📄report/
│   ├── chapter1-introduction.md
│   └── thesis_template.docx
└── LICENSE
```

## Installation
```

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/rajeshmore1/rag-nova.git
cd rag-nova

# Set up virtual environment
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```
## Quick Start
1. Parse a Document
```
python src/document_parser.py --input data/raw/sample_invoice.pdf
```
2. Generate an Answer
```
python src/rag_pipeline.py --query "What is the due date on the invoice?"
```
3. Run the Streamlit UI
```
streamlit run deployment/streamlit_app.py
```

## Evaluation Metrics
🔍 Retrieval: Precision@k, nDCG

🧠 Generation: BLEU, F1, Answer Confidence

🧯 Trust: Confidence Gap, Out-of-Domain Detection

## Acknowledgements
IBM Research for TableLab and Document Understanding inspiration

Microsoft Research for LayoutLM

HuggingFace Transformers & Datasets

FAISS for vector search


