import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import timedelta

# Load data
df = pd.read_csv('energy_demand.csv', parse_dates=['Date'])
df['Days'] = (df['Date'] - df['Date'].min()).dt.days.values.reshape(-1, 1)

# Fit model
model = LinearRegression()
model.fit(df['Days'], df['Demand'])

# Predict next 30 days
future_days = pd.DataFrame({'Days': range(df['Days'].max()+1, df['Days'].max()+31)})
future_demand = model.predict(future_days)

# Plot
plt.plot(df['Date'], df['Demand'], label='Historical')
future_dates = df['Date'].max() + pd.to_timedelta(future_days['Days'] - df['Days'].max(), unit='d')
plt.plot(future_dates, future_demand, label='Forecast')
plt.legend()
plt.title('Energy Demand Forecast')
plt.savefig('forecast_plot.png')
