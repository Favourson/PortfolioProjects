import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical data for a stock
def get_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data['Return'] = data['Close'].pct_change()
    return data

# Calculate Moving Averages
def add_moving_averages(data, short_window=50, long_window=200):
    data['SMA50'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['SMA200'] = data['Close'].rolling(window=long_window, min_periods=1).mean()
    return data

# Generate Buy/Sell signals
def generate_signals(data, short_window=50):
    data['Signal'] = 0
    data.iloc[short_window:, data.columns.get_loc('Signal')] = np.where(
        data['SMA50'].iloc[short_window:] > data['SMA200'].iloc[short_window:], 1, 0
    )
    data['Position'] = data['Signal'].diff()
    return data

# Backtest Strategy
def backtest(data):
    initial_capital = 100000  # Initial capital in dollars
    shares = 0  # Track number of shares held
    capital = initial_capital  # Current capital
    
    for i in range(len(data)):
        if data['Position'].iloc[i] == 1:  # Buy signal
            shares = capital // data['Close'].iloc[i]  # Buy shares
            capital -= shares * data['Close'].iloc[i]  # Deduct cost from capital
        elif data['Position'].iloc[i] == -1:  # Sell signal
            capital += shares * data['Close'].iloc[i]  # Sell all shares
            shares = 0  # Reset shares
            
    # Final portfolio value
    final_value = capital + (shares * data['Close'].iloc[-1])
    final_value = float(final_value.iloc[0])  # Use iloc[0] here

    # Ensure profit_percent is a scalar before formatting
    profit_percent = (final_value - initial_capital) / initial_capital
    profit_percent = float(profit_percent)  # Convert to float

    return final_value, profit_percent

# Plotting results
def plot_strategy(data):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data['SMA50'], label='50-day SMA')
    plt.plot(data['SMA200'], label='200-day SMA')
    
    plt.plot(data[data['Position'] == 1].index, 
             data['SMA50'][data['Position'] == 1], 
             '^', markersize=10, color='g', lw=0, label='Buy Signal')
    plt.plot(data[data['Position'] == -1].index, 
             data['SMA50'][data['Position'] == -1], 
             'v', markersize=10, color='r', lw=0, label='Sell Signal')
    
    plt.title('Moving Average Crossover Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

# Run Strategy
ticker = 'AAPL'  # Example: Apple stock
start_date = '2020-01-01'
end_date = '2024-11-09'
short_window = 50
long_window = 200

data = get_data(ticker, start_date, end_date)
data = add_moving_averages(data, short_window, long_window)
data = generate_signals(data, short_window)
final_value, profit_percent = backtest(data)

# Ensure final_value and profit_percent are scalars before formatting
final_value = float(final_value)
profit_percent = float(profit_percent)

print(f"Final Portfolio Value: ${final_value:.2f}")
print(f"Total Return: {profit_percent * 100:.2f}%")

plot_strategy(data)
