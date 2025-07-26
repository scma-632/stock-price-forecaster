import streamlit as st
from forecast import forecast_stock
from utils import plot_forecast

st.title("📈 NSE Stock Price Forecast App")
st.write("Forecasts the **next 5 trading days** closing price using **Exponential Smoothing**.")

ticker = st.text_input("Enter NSE Ticker (e.g., TCS.NS, INFY.NS, RELIANCE.NS):", value="INFY.NS")

if st.button("Forecast"):
    try:
        df, forecast_df = forecast_stock(ticker)
        st.write("### Forecasted Closing Prices:")
        st.dataframe(forecast_df)
        st.pyplot(plot_forecast(df, forecast_df))
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
