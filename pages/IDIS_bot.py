import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import openai
import numpy as np
import faiss

# Set API key (OpenAI >= v1.0)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Inisialisasi FAISS & embedding
def initialize_rag():
    index = faiss.IndexFlatL2(1536)
    knowledge_base = [
        "Investasi saham adalah kegiatan menanam modal di perusahaan publik dengan membeli saham mereka di bursa efek.",
        "Diversifikasi portofolio adalah strategi menyebar investasi ke berbagai instrumen untuk mengurangi risiko.",
        "Analisis fundamental mencakup rasio seperti PER, PBV, ROE untuk mengevaluasi kondisi keuangan perusahaan.",
        "Analisis teknikal mencakup indikator RSI, MACD, MA, dan pola candlestick untuk memprediksi arah harga.",
        "Investasi emas adalah penempatan dana dalam bentuk logam mulia untuk lindung nilai terhadap inflasi.",
        "Reksadana adalah instrumen investasi kolektif yang dikelola manajer investasi.",
        "Obligasi adalah surat utang jangka menengah atau panjang yang diterbitkan oleh pemerintah atau perusahaan."
    ]
    try:
        response = openai.embeddings.create(
            model="text-embedding-3-small",
            input=knowledge_base
        )
        embeddings = [d.embedding for d in response.data]
        index.add(np.array(embeddings))
    except Exception as e:
        st.warning(f"Gagal memuat embedding dari OpenAI: {e}")
    return index, [], knowledge_base

# Ambil info saham dan hitung RSI
def get_stock_info(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        hist = stock.history(period="14d")

        delta = hist['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        latest_rsi = rsi.iloc[-1] if not rsi.isnull().all() else None

        current_price = info.get('currentPrice', 0)
        previous_close = info.get('previousClose', 0)
        price_change = current_price - previous_close
        price_change_percent = (price_change / previous_close) * 100 if previous_close else 0

        return {
            'name': info.get('longName', 'N/A'),
            'current_price': current_price,
            'change': price_change,
            'change_percent': price_change_percent,
            'volume': info.get('volume', 0),
            'market_cap': info.get('marketCap', 0),
            'pe_ratio': info.get('trailingPE', 0),
            'dividend_yield': info.get('dividendYield', 0),
            'rsi': latest_rsi
        }
    except Exception as e:
        st.error(f"Error fetching stock info: {str(e)}")
        return None

# Cari knowledge base
def search_knowledge(query, index, knowledge_base, top_k=3):
    try:
        response = openai.embeddings.create(
            model="text-embedding-3-small",
            input=[query]
        )
        query_embedding = np.array([response.data[0].embedding])
        D, I = index.search(query_embedding, top_k)
        return [knowledge_base[i] for i in I[0]]
    except Exception as e:
        st.warning(f"Gagal melakukan pencarian embedding: {e}")
        return []

# UI & Logic Chat
def chat_with_ai():
    st.title("🤖 IDIS BOT")
    st.markdown("Asisten Investasi Pintar Anda 💰")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    index, vectors, kb_texts = initialize_rag()

    # Sidebar Saham
    with st.sidebar:
        st.subheader("📈 Analisis Saham")
        stock_symbol = st.text_input("Masukkan simbol saham (contoh: GOTO.JK)", "GOTO.JK")
        if stock_symbol:
            stock_info = get_stock_info(stock_symbol)
            if stock_info:
                st.write(f"**{stock_info['name']}**")
                st.write(f"Harga: ${stock_info['current_price']:.2f}")
                st.write(f"Perubahan: {stock_info['change_percent']:.2f}%")
                st.write(f"P/E Ratio: {stock_info['pe_ratio']:.2f}")
                st.write(f"Dividen: {stock_info['dividend_yield']:.2f}%")
                st.write(f"RSI: {stock_info['rsi']:.2f}" if stock_info['rsi'] else "RSI: Tidak tersedia")

                hist = yf.Ticker(stock_symbol).history(period="1y")
                fig = go.Figure(data=[go.Candlestick(
                    x=hist.index,
                    open=hist['Open'],
                    high=hist['High'],
                    low=hist['Low'],
                    close=hist['Close']
                )])
                fig.update_layout(title=f"{stock_symbol} - Grafik 1 Tahun")
                st.plotly_chart(fig)

    # Chat Display
    with st.chat_message("assistant"):
        st.markdown("Halo! Saya IDIS Bot, siap bantu kamu seputar investasi! 🧠")

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Apa pertanyaan kamu hari ini?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            retrieved = search_knowledge(prompt, index, kb_texts)
            context = "\n".join(retrieved)

            system_prompt = (
                "Anda adalah asisten AI profesional di bidang investasi. Hanya jawab pertanyaan yang relevan dengan topik investasi: saham, emas, obligasi, reksadana, dan semua instrumen keuangan. "
                "Jawaban harus edukatif, berbasis data, dan disertai sumber terpercaya dari internet bila memungkinkan.\n"
                f"\nKonteks tambahan:\n{context}\n"
                "\n⚠️ Ini bukan ajakan jual/beli, melainkan informasi edukatif."
            )

            try:
                stream = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                    ],
                    stream=True,
                    temperature=0.7,
                )

                for chunk in stream:
                    content = chunk.choices[0].delta.content or ""
                    full_response += content
                    message_placeholder.markdown(full_response + "▌")

                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"Gagal mengambil respons dari OpenAI: {e}")
                st.session_state.messages.append({"role": "assistant", "content": "Maaf, terjadi gangguan saat mengambil jawaban. Silakan coba beberapa saat lagi."})

# Verifikasi login
if "isverif" not in st.session_state or not st.session_state["isverif"]:
    st.header("🚫 AKSES DITOLAK")
    st.subheader("Silakan login / buat akun terlebih dahulu.")
else:
    chat_with_ai()