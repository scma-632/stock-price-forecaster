import streamlit as st
from forecast import forecast_stock
from utils import plot_forecast

st.title("📈 NSE Stock Price Forecast App (Auto ARIMA)")
st.write("Forecasts the **next 5 trading days** closing price using Auto ARIMA model (pmdarima).")

ticker = st.text_input("Enter NSE Stock Symbol (e.g., INFY.NS, TCS.NS, RELIANCE.NS):", value="INFY.NS")

if st.button("Forecast"):
    try:
        df, forecast_df = forecast_stock(ticker)
        st.write("### Forecasted Closing Prices:")
        st.dataframe(forecast_df)
        st.pyplot(plot_forecast(df, forecast_df))
    except Exception as e:
        st.error(f"Error: {e}")
