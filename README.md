# 📈 NSE Stock Price Forecast App

A simple Streamlit app to forecast the next **5 trading days** closing prices of **NSE-listed stocks** using **Auto ARIMA** from `pmdarima`.

## 🔧 Features

- Supports any valid NSE ticker (e.g., `TCS.NS`, `INFY.NS`, `RELIANCE.NS`)
- Uses `yfinance` to fetch the last 6 months of historical data
- Forecasts next 5 trading days using `Auto ARIMA`
- Visualizes historical and forecasted prices

## ▶️ How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txx
