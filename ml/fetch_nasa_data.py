import requests
import pandas as pd

# 1. Set your location
lat = 1.58   # Malaysia example
lon = 103.76

# 2. Set date range (last 5 years)
start = 20180101
end = 20231231

# 3. API URL
url = f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_SW_DWN&start={start}&end={end}&latitude={lat}&longitude={lon}&community=re&format=json"

# 4. Fetch data
response = requests.get(url)
data = response.json()

# 5. Convert to pandas dataframe
irradiance = data['properties']['parameter']['ALLSKY_SFC_SW_DWN']
df = pd.DataFrame(list(irradiance.items()), columns=['date', 'irradiance'])
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df['irradiance'] = pd.to_numeric(df['irradiance'])

# 6. Save to CSV
df.to_csv('solar_irradiance.csv', index=False)
print("Data saved to solar_irradiance.csv")
