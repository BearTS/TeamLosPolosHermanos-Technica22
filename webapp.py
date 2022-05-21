import streamlit as st
import yfinance as yf
from datetime import date
from dateutil.relativedelta import relativedelta as rd

import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt
from matplotlib import rc
from plotly import graph_objs as go
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Bidirectional, Dropout, Activation, Dense, LSTM
from tensorflow.python.keras.layers import CuDNNLSTM
from tensorflow.keras.models import Sequential
import json
import requests

start = (date.today() - rd(years=1)).strftime("%Y-%m-%d")
end =  date.today().strftime("%Y-%m-%d")

st.title("Crypto Currency Predictor")

crypto = ("BTC-USD", "ETH-USD", "BNB-USD", "DOGE-USD")
crypto_selected = st.selectbox("Select the currency for prediction", crypto)

@st.cache
def load_data(ticker):
    data = yf.download(ticker, start, end)
    data.reset_index(inplace=True)
    return data

data = load_data(crypto_selected)

st.subheader("Dataset")
st.write(data.head())

#Visualisation
st.subheader("Visualisation")
def plot_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Open"], name="stock_open"))
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], name="stock_close"))
    fig.layout.update(title_text="Opening and Closing vs Time", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_data()