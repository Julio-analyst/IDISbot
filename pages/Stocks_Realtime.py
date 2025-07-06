import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import datetime as dt
import plotly.graph_objects as go

# Verifikasi Login
if "isverif" not in st.session_state or not st.session_state["isverif"]:
    st.header("ANDA TIDAK MEMPUNYAI AKSES")
    st.subheader("Harap buat akun terlebih dahulu 😊")
else:
    st.title("Real-time Stock Analytics")

    stock_symbol = st.text_input("Enter Stock Symbol", "AAPL")
    time_frame = st.slider("Select Time Frame (in months)", 1, 100, 5)
    stock_start_date = dt.datetime.now() - dt.timedelta(days=time_frame * 30)

    def get_stock_data(symbol, start_date, max_retries=3):
        import time
        for attempt in range(max_retries):
            try:
                ticker = yf.Ticker(symbol)
                data = ticker.history(start=start_date, end=dt.datetime.now())
                if not data.empty:
                    return data
                else:
                    st.warning(f"Percobaan {attempt + 1}: Data kosong untuk {symbol}")
            except Exception as e:
                st.warning(f"Percobaan {attempt + 1} gagal: {e}")
            time.sleep(2)
        st.error("Gagal mengambil data saham setelah beberapa kali percobaan.")
        return pd.DataFrame()

    def calculate_rsi(data, window=14):
        delta = data['Close'].diff()
        gain = np.where(delta > 0, delta, 0)
        loss = np.where(delta < 0, -delta, 0)
        avg_gain = pd.Series(gain, index=data.index).rolling(window=window).mean()
        avg_loss = pd.Series(loss, index=data.index).rolling(window=window).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calculate_bollinger_bands(stock_data):
        rolling_mean = stock_data['Close'].rolling(window=20).mean()
        rolling_std = stock_data['Close'].rolling(window=20).std()
        upper_band = rolling_mean + (rolling_std * 2)
        lower_band = rolling_mean - (rolling_std * 2)
        return upper_band, rolling_mean, lower_band

    def calculate_stock_metrics(stock_data):
        stock_data['RSI'] = calculate_rsi(stock_data)
        stock_data['BB_Upper'], stock_data['BB_Middle'], stock_data['BB_Lower'] = calculate_bollinger_bands(stock_data)
        return stock_data

    stock_data = get_stock_data(stock_symbol, stock_start_date)

    if not stock_data.empty:
        stock_data = calculate_stock_metrics(stock_data)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Stock Price'))
        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['BB_Upper'], mode='lines', name='Upper Bollinger Band'))
        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['BB_Middle'], mode='lines', name='Middle Bollinger Band'))
        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['BB_Lower'], mode='lines', name='Lower Bollinger Band'))
        fig.update_layout(title='Stock Price with Bollinger Bands', xaxis_title='Date', yaxis_title='Price')

        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=stock_data.index, y=stock_data['RSI'], mode='lines', name='RSI'))
        fig2.update_layout(title='Relative Strength Index (RSI)', xaxis_title='Date', yaxis_title='RSI')

        st.plotly_chart(fig)
        st.plotly_chart(fig2)