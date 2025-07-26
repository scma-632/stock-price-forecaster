import matplotlib.pyplot as plt

def plot_forecast(df, forecast_df):
    fig, ax = plt.subplots(figsize=(10, 5))
    df['Close'].plot(ax=ax, label="Historical", color='blue')
    forecast_df['Forecast'].plot(ax=ax, label="Forecast", color='red', linestyle='--')
    ax.set_title("Stock Price Forecast")
    ax.set_ylabel("Price (INR)")
    ax.set_xlabel("Date")
    ax.legend()
    return fig
