import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# 1. Load CSV
df = pd.read_csv('solar_irradiance.csv')
df.rename(columns={'date': 'ds', 'irradiance': 'y'}, inplace=True)

# 2. Initialize Prophet model
model = Prophet(yearly_seasonality=True, daily_seasonality=False)

# 3. Train the model
model.fit(df)

# 4. Make future dataframe (12 months)
future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)

# 5. Plot forecast
fig = model.plot(forecast)
plt.show()

# 6. Save forecast data to CSV
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv('solar_forecast.csv', index=False)
print("Forecast saved to solar_forecast.csv")
