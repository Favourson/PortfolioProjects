import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data
ticker = 'AAPL'  # You can change this to any symbol
start_date = '2020-01-01'
end_date = '2023-01-01'

data = yf.download(ticker, start=start_date, end=end_date)

# Define functions to calculate zones and generate signals
def calculate_zones(data, structure_len, multiplier):
    """
    Calculate zones based on structure length and multiplier.
    """
    zones = []
    
    # Iterate through data to find high/low zones
    for i in range(structure_len, len(data)):
        window_data = data.iloc[i-structure_len:i]
        high = window_data['High'].max()
        low = window_data['Low'].min()
        
        # Add calculated zones to the list
        zones.append((low, high, i))
    
    return zones

def generate_signals(data, zones, multiplier):
    """
    Generate buy/sell signals based on calculated zones.
    """
    signals = []
    for low, high, idx in zones:
        # Ensure high and low are scalar values
        high = float(high)
        low = float(low)

        # Check if price crosses zones with the multiplier
        close_price = float(data['Close'].iloc[idx])
        if close_price > high * multiplier:
            signals.append(('Buy', data.index[idx], close_price))
        elif close_price < low * multiplier:
            signals.append(('Sell', data.index[idx], close_price))

    return signals

# Function to calculate profitability and statistics
def calculate_performance(data, signals, initial_capital=100000):
    """
    Calculate the performance of the trading strategy.
    """
    positions = []
    capital = initial_capital

    for signal in signals:
        if signal[0] == 'Buy':
            positions.append(('Buy', signal[1], signal[2]))
        elif signal[0] == 'Sell' and positions:
            buy_signal = positions.pop(0)
            buy_price = buy_signal[2]
            sell_price = signal[2]
            profit = sell_price - buy_price
            capital += profit
    
    final_value = capital
    total_return = (final_value - initial_capital) / initial_capital * 100

    # Calculate additional performance metrics
    data['Daily_Return'] = data['Close'].pct_change()
    annual_return = (final_value / initial_capital) ** (252 / len(data)) - 1
    annual_volatility = data['Daily_Return'].std() * np.sqrt(252)
    sharpe_ratio = annual_return / annual_volatility

    return final_value, total_return, annual_return, annual_volatility, sharpe_ratio

# Set parameters for backtesting
structure_len = 5  # Example: length of the structure
multiplier = 1.1    # Example: multiplier for zone boundaries

# Calculate zones based on the historical data
zones = calculate_zones(data, structure_len, multiplier)

# Generate signals based on calculated zones
signals = generate_signals(data, zones, multiplier)

# Calculate performance
final_value, total_return, annual_return, annual_volatility, sharpe_ratio = calculate_performance(data, signals)

# Print performance results
print(f"Final Portfolio Value: ${final_value:.2f}")
print(f"Total Return: {total_return:.2f}%")
print(f"Annual Return: {annual_return * 100:.2f}%")
print(f"Annual Volatility: {annual_volatility * 100:.2f}%")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

# Print signals
for signal in signals:
    print(f"Signal: {signal[0]} on {signal[1]} at price {signal[2]}")

# Plot the signals on a price chart
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], label='Close Price', color='blue')

# Plot buy and sell signals
for signal in signals:
    if signal[0] == 'Buy':
        plt.scatter(signal[1], signal[2], marker='^', color='green')
    elif signal[0] == 'Sell':
        plt.scatter(signal[1], signal[2], marker='v', color='red')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title(f'{ticker} Buy and Sell Signals Based on Zones')
plt.legend(['Close Price', 'Buy Signal', 'Sell Signal'])
plt.show()
