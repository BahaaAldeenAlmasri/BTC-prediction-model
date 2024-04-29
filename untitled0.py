import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Load your Bitcoin data (assuming it's stored in a DataFrame with a 'Date' index and a 'Close' column)
# Replace 'your_data.csv' with the actual path to your data file
bitcoin_data = pd.read_csv('C:/Users/BAHAA ALDEEN/Downloads/Binance_BTCUSDT_d.csv', parse_dates=['Date'], index_col='Date')

# Plot the time series to visualize any trends, seasonality, or other patterns
plt.figure(figsize=(10, 6))
plt.plot(bitcoin_data.index, bitcoin_data['Close'], color='blue')
plt.title('Bitcoin Daily Close Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.show()

# Check for stationarity (optional)
# You can use the Augmented Dickey-Fuller test or plot ACF/PACF
# For simplicity, let's assume the data is stationary

# Plot ACF and PACF to determine the order of ARIMA(p,d,q)
plot_acf(bitcoin_data['Close'], lags=20)
plot_pacf(bitcoin_data['Close'], lags=20)
plt.show()

# Specify the order of ARIMA(p,d,q) based on the ACF and PACF plots
p = 2  # AR order (based on PACF)
d = 1  # differencing order (based on stationarity)
q = 2  # MA order (based on ACF)

# Split the data into train and test sets
train_size = int(len(bitcoin_data) * 0.8)
train_data, test_data = bitcoin_data.iloc[:train_size], bitcoin_data.iloc[train_size:]

# Fit the ARIMA model
model = ARIMA(train_data['Close'], order=(p, d, q))
fitted_model = model.fit()

# Forecast
forecast = fitted_model.forecast(steps=len(test_data))

# Plot actual vs. forecasted values
plt.figure(figsize=(10, 6))
plt.plot(train_data.index, train_data['Close'], label='Train')
plt.plot(test_data.index, test_data['Close'], label='Test')
plt.plot(test_data.index, forecast, label='Forecast', color='red')
plt.title('Bitcoin Daily Close Price Forecast')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
