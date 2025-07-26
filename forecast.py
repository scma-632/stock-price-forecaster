import yfinance as yf
import pandas as pd
from pmdarima import auto_arima
from datetime import timedelta

def forecast_stock(ticker):
    df = yf.download(ticker, period="6mo", interval="1d")
    if df.empty:
        raise ValueError("No data found. Please check the symbol.")
        
    df = df[['Close']].dropna()

    model = auto_arima(df['Close'], seasonal=False, suppress_warnings=True)
    forecast = model.predict(n_periods=5)

    last_date = df.index[-1]
    forecast_dates = pd.bdate_range(start=last_date + timedelta(days=1), periods=5)

    forecast_df = pd.DataFrame({
        "Date": forecast_dates,
        "Forecast": forecast
    }).set_index("Date")

    return df, forecast_df
