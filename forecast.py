import yfinance as yf
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from datetime import timedelta

def forecast_stock(ticker):
    df = yf.download(ticker, period="6mo", interval="1d")
    if df.empty:
        raise ValueError("No data found for this symbol.")
        
    df = df[['Close']].dropna()

    model = ExponentialSmoothing(df['Close'], trend='add', seasonal=None)
    model_fit = model.fit()
    forecast = model_fit.forecast(5)

    last_date = df.index[-1]
    forecast_dates = pd.bdate_range(start=last_date + timedelta(days=1), periods=5)

    forecast_df = pd.DataFrame({
        "Date": forecast_dates,
        "Forecast": forecast
    }).set_index("Date")

    return df, forecast_df
