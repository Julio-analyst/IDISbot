# 📊 Real-time Stock Analytics with AI Assistant (IDIS BOT)

> Developed using Streamlit, YFinance, Plotly, FAISS, and OpenAI

## 📌 Overview

A Streamlit-based investment dashboard that provides:

* Real-time stock price visualization with **Bollinger Bands** and **RSI**.
* AI Chatbot **IDIS BOT** with **RAG (Retrieval-Augmented Generation)** capability to answer investment questions.
* Support for multiple asset classes: **stocks, mutual funds, gold, bonds**, and more.

---

## 🧠 IDIS BOT - AI Chat Assistant (RAG)

**RAG (Retrieval-Augmented Generation)** is a method where chatbot responses are enhanced with information retrieved from a custom knowledge base.

🔍 This bot:

* Retrieves relevant facts from an investment knowledge base using OpenAI embeddings + FAISS vector search.
* Uses **GPT-4o** to generate answers.
* Can fetch **real-time stock data** (price, RSI, PER, PBV, etc) from Yahoo Finance.
* Strictly answers **only investment-related topics**, such as:

  * Technical & fundamental analysis
  * Asset classes (stocks, bonds, mutual funds, crypto, etc)
  * Market insights and educational content

⚠️ Always includes disclaimer: *"Informasi edukatif, bukan ajakan jual/beli"*.

---

## 📈 Features

* 📊 Bollinger Bands & RSI visualization
* 🧮 Fundamental metrics: PE Ratio, Dividend Yield
* 💬 Chatbot with smart investment reasoning
* 🔐 Login verification (`st.session_state['isverif']`)

---

## 🛠️ Tech Stack

* `Python 3.10+`
* [`Streamlit`](https://streamlit.io/)
* [`yfinance`](https://github.com/ranaroussi/yfinance)
* [`plotly`](https://plotly.com/python/)
* [`openai`](https://pypi.org/project/openai/)
* [`faiss`](https://github.com/facebookresearch/faiss)
* \[`numpy`, `pandas`]

---

## 📁 Project Structure

```
📦 Invesment_Advisor/
├── Home_Page.py
├── pages/
│   ├── IDIS_bot.py          # AI chatbot with OpenAI + RAG
│   └── Stock_Realtime.py    # Stock charting with RSI & Bollinger
├── .streamlit/
│   └── secrets.toml         # OpenAI API Key securely stored
└── requirements.txt
```

---

## ⚙️ Setup Instructions

```bash
# Clone the repo
$ git clone https://github.com/<your-repo>
$ cd Invesment_Advisor

# Create virtual environment
$ python -m venv .venv
$ source .venv/bin/activate   # or .venv\Scripts\activate on Windows

# Install dependencies
$ pip install -r requirements.txt

# Set your OpenAI API key in .streamlit/secrets.toml
[OPENAI_API_KEY]
key = "your-key-here"

# Run the app
$ streamlit run Home_Page.py
```

---

## 🧪 Sample Usage

* Run `IDIS_bot.py` for AI Q\&A (e.g., "Apakah BBRI saat ini undervalued?")
* Run `Stock_Realtime.py` to visualize Bollinger Bands & RSI for selected ticker.

---

## 🔐 Notes

* Ensure stable internet connection.
* Be mindful of [Yahoo Finance rate limits](https://github.com/ranaroussi/yfinance/issues/800): too many requests may cause temporary bans (error 429).
* You can enhance by adding caching or local storage for stock history.

---

## 📣 Contributions

Pull requests welcome! 🚀

---

## 📝 License

MIT

---

> Built with ❤️ by Julio-analyst | 2025
