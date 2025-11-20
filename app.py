
import streamlit as st

import numpy as np
import pandas as pd

# Load SARIMA model
sarima_model = joblib.load('sarima_model.pkl')

st.title("Apple Stock Price Multi-Day Forecast")

days = st.slider("Select number of days to predict:", min_value=1, max_value=30, value=7)

if st.button("Predict"):
    # Forecast next 'days' points
    forecast = sarima_model.forecast(steps=days)

    # Create a DataFrame for nice output
    # The last date in the original df can be retrieved from `series` (which is df['Close'])
    last_date_in_data = df['Date'].iloc[-1]
    future_dates = pd.date_range(start=last_date_in_data + pd.Timedelta(days=1), periods=days)
    df_forecast = pd.DataFrame({'Date': future_dates, 'Predicted_Close': forecast})

    st.write(f"Predicted Closing Prices for Next {days} Days:")
    st.line_chart(df_forecast.set_index('Date')['Predicted_Close'])
    st.table(df_forecast)
