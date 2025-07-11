# 📊 Real-time Stock Analytics with AI Assistant — IDIS BOT

> Built with Streamlit, YFinance, Plotly, FAISS, and OpenAI GPT-4o  
> 🧠 AI Chatbot with RAG (Retrieval-Augmented Generation) for smart investment Q&A.

---

## 📌 Overview

IDIS BOT is an AI-powered investment assistant and dashboard built with Streamlit.  
It helps users visualize technical indicators and answer investment-related questions using real-time market data.

🔎 Supports multi-asset analysis:
- Stocks
- Mutual Funds
- Bonds
- Gold
- Crypto

---

## 🔗 Data Sources

- 📈 [Yahoo Finance](https://finance.yahoo.com/) via [`yfinance`](https://github.com/ranaroussi/yfinance)
- 📚 Custom investment knowledge base (used in RAG)

---

## 🧠 RAG-Powered Chat Assistant

**Retrieval-Augmented Generation (RAG)** combines embeddings, vector search, and LLMs.

IDIS BOT:
- Embeds knowledge base using `OpenAI embeddings`
- Stores in `FAISS` vector index
- Uses `GPT-4o` for context-rich responses
- Retrieves real-time stock metrics (RSI, Bollinger, PER, PBV, etc)
- Restricts answers strictly to investment topics

⚠️ Disclaimer shown in every response:  
_“Informasi edukatif, bukan ajakan jual/beli.”_

---

## 📈 Features

- 📊 Bollinger Bands & RSI visualization  
- 🧮 Fundamental metrics: PE Ratio, PBV, Dividend Yield  
- 💬 RAG-based AI Chatbot  
- 🔐 Login gate via `session_state['isverif']`

---

## 📁 Project Structure

```
📦 Invesment_Advisor/
├── Home_Page.py
├── pages/
│   ├── IDIS_bot.py          # Chatbot with RAG
│   └── Stock_Realtime.py    # Visual chart w/ indicators
├── .streamlit/
│   └── secrets.toml         # Secure API key storage
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

**Languages**: Python 3.10+  
**Tools & Libraries**:
- `Streamlit`, `yfinance`, `plotly`
- `OpenAI`, `faiss`, `pandas`, `numpy`

**RAG Stack**:  
- `OpenAI Embeddings` + `FAISS` + `GPT-4o`

---

## ⚙️ Setup Instructions

```bash
# Clone repo
$ git clone https://github.com/Julio-analyst/Invesment_Advisor.git
$ cd Invesment_Advisor

# Create virtual environment
$ python -m venv .venv
$ source .venv/bin/activate     # Or .venv\Scripts\activate on Windows

# Install dependencies
$ pip install -r requirements.txt

# Add your OpenAI API key in .streamlit/secrets.toml
[OPENAI_API_KEY]
key = "your-key-here"

# Run the app
$ streamlit run Home_Page.py
```

---

## 🧪 How to Use

- Run `Home_Page.py`  
- Navigate to:
  - `IDIS_bot` for chatbot Q&A  
  - `Stock_Realtime` to see technical charts  

> Try asking: “Apakah BBRI undervalued saat ini berdasarkan PBV?”  
> Or visualize: “AAPL” to see RSI chart with Bollinger Bands

---

## 🧠 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)  
- Embeddings & vector similarity search  
- Streamlit dashboard design  
- Stock analysis & financial indicators  
- API integration (OpenAI, Yahoo Finance)  
- Clean code structure & modularization

---

## 📚 References & Documentation

- 🔗 Asetal BOT by kyukazamiqq: https://github.com/kyukazamiqq/Asetal_BOT
- 📘 [OpenAI API Documentation](https://platform.openai.com/docs)
- 📘 [FAISS by Facebook Research](https://github.com/facebookresearch/faiss)
- 📘 [Streamlit Documentation](https://docs.streamlit.io/)
- 📘 [YFinance Documentation](https://pypi.org/project/yfinance/)
- 📘 [Plotly for Python](https://plotly.com/python/)

---

## 📝 License

MIT License  
© 2025 Julio-analyst

---

## 📬 Contact

- 🌐 [LinkedIn](https://www.linkedin.com/in/farrel-julio-427143288)  
- 🗂️ [Portfolio (Notion)](https://linktr.ee/Julio-analyst)  
- ✉️ farelrel12345@gmail.com

---

[![Streamlit](https://img.shields.io/badge/Built_with-Streamlit-orange?logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
