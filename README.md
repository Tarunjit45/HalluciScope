# 🔬 HalluciScope

**HalluciScope** is a lightweight, local-first AI safety tool designed to perform "autopsies" on LLM responses. It extracts factual claims from AI outputs and verifies them against a provided ground-truth context using a local LLM judge.



## 🌟 Features
- **Local-First:** Uses Ollama (Llama 3.2:1b) for private, secure, and free verification.
- **Claim Extraction:** Automatically breaks down paragraphs into individual factual statements.
- **Hallucination Scoring:** Quantifies the truthfulness of a response (0.0 to 1.0).
- **Interactive CLI:** Simple terminal-based interface for quick testing.
- **Root Cause Analysis:** Identifies why a hallucination occurred (e.g., temporal assumptions).

## 🛠️ Installation

### 1. Prerequisites
* Python 3.10+
* [Ollama](https://ollama.com/) (installed and running)

### 2. Setup
Clone the repository and install dependencies:
```bash
git clone [https://github.com/Tarunjit45/HalluciScope.git](https://github.com/Tarunjit45/HalluciScope.git)
cd HalluciScope
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
ollama pull llama3.2:1b
python cli.py



ollama pull llama3.2:1b
