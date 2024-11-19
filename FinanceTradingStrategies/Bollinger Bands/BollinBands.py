import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical data for a stock or currency pair
def get_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data['Return'] = data['Close'].pct_change()
    return data

# Calculate Bollinger Bands
def add_bollinger_bands(data, lookback_period=20, std_dev=2):
    data['SMA'] = data['Close'].rolling(window=lookback_period, min_periods=1).mean()
    data['Rolling Std'] = data['Close'].rolling(window=lookback_period, min_periods=1).std()
    data['Upper Band'] = data['SMA'] + (data['Rolling Std'] * std_dev)
    data['Lower Band'] = data['SMA'] - (data['Rolling Std'] * std_dev)
    return data

# Clean column names to ensure no empty or multi-level columns
def clean_column_names(data):
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    data.columns = [col if col != '' else 'Unnamed' for col in data.columns]
    return data

# Generate Buy/Sell signals
def generate_signals(data):
    data = clean_column_names(data)
    data['Prev Close'] = data['Close'].shift(1)  # Shift 'Close' for 'Prev Close'
    data['Prev SMA'] = data['SMA'].shift(1)      # Shift 'SMA' for 'Prev SMA'
    data = data.dropna(subset=['Prev Close', 'Prev SMA'])
    data = data.copy()
    data.loc[(data['Close'] > data['SMA']) & (data['Prev Close'] <= data['Prev SMA']), 'Signal'] = 1  # Buy signal
    data.loc[(data['Close'] < data['SMA']) & (data['Prev Close'] >= data['Prev SMA']), 'Signal'] = -1  # Sell signal
    data['Position'] = data['Signal'].replace(to_replace=0, method='ffill').fillna(0)
    return data

# Calculate additional performance metrics
def calculate_metrics(data):
    # Calculate daily returns for the strategy
    data['Strategy Returns'] = data['Close'].pct_change() * data['Position'].shift(1)
    
    # Annualize the returns
    annualized_return = data['Strategy Returns'].mean() * 252
    
    # Calculate annualized volatility
    annualized_volatility = data['Strategy Returns'].std() * np.sqrt(252)
    
    # Calculate Sharpe Ratio
    risk_free_rate = 0.01  # Example risk-free rate
    sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility
    
    # Calculate Maximum Drawdown
    cumulative_returns = (1 + data['Strategy Returns']).cumprod()
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    max_drawdown = drawdown.min()

    return annualized_return, annualized_volatility, sharpe_ratio, max_drawdown

# Backtest Strategy
def backtest(data):
    initial_capital = 100000  # Initial capital in dollars
    shares = 0  # Track number of shares held
    capital = initial_capital  # Current capital

    for i in range(len(data)):
        if data['Position'].iloc[i] == 1 and shares == 0:  # Buy signal
            shares = capital // data['Close'].iloc[i]  # Buy shares
            capital -= shares * data['Close'].iloc[i]  # Deduct cost from capital
        elif data['Position'].iloc[i] == -1 and shares > 0:  # Sell signal
            capital += shares * data['Close'].iloc[i]  # Sell all shares
            shares = 0  # Reset shares
    
    # Final portfolio value
    final_value = capital + (shares * data['Close'].iloc[-1])
    profit_percent = (final_value - initial_capital) / initial_capital

    return final_value, profit_percent

# Plotting results
def plot_strategy(data):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['SMA'], label='SMA', color='orange')
    plt.plot(data['Upper Band'], label='Upper Band', color='green')
    plt.plot(data['Lower Band'], label='Lower Band', color='red')
    plt.plot(data[data['Signal'] == 1].index, 
             data['SMA'][data['Signal'] == 1], 
             '^', markersize=10, color='g', label='Buy Signal')
    plt.plot(data[data['Signal'] == -1].index, 
             data['SMA'][data['Signal'] == -1], 
             'v', markersize=10, color='r', label='Sell Signal')
    plt.title('Bollinger Bands Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

# Plotting additional results
def plot_additional_metrics(data):
    # Equity Curve
    data['Equity Curve'] = (1 + data['Strategy Returns']).cumprod() * 100000
    plt.figure(figsize=(14, 7))
    plt.plot(data['Equity Curve'], label='Equity Curve')
    plt.title('Equity Curve')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value')
    plt.legend()
    plt.show()
    
    # Returns Distribution
    plt.figure(figsize=(14, 7))
    data['Strategy Returns'].hist(bins=50, edgecolor='black')
    plt.title('Returns Distribution')
    plt.xlabel('Daily Returns')
    plt.ylabel('Frequency')
    plt.show()

    # Cumulative Returns
    data['Cumulative Returns'] = (1 + data['Strategy Returns']).cumprod() - 1
    plt.figure(figsize=(14, 7))
    plt.plot(data['Cumulative Returns'], label='Cumulative Returns')
    plt.title('Cumulative Returns')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.legend()
    plt.show()
    
    # Drawdowns
    cumulative_returns = (1 + data['Strategy Returns']).cumprod()
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    plt.figure(figsize=(14, 7))
    plt.plot(drawdown, label='Drawdown')
    plt.title('Drawdowns')
    plt.xlabel('Date')
    plt.ylabel('Drawdown')
    plt.legend()
    plt.show()
    
    # Rolling Sharpe Ratio
    rolling_sharpe = (data['Strategy Returns'].rolling(window=252).mean() / data['Strategy Returns'].rolling(window=252).std()) * np.sqrt(252)
    plt.figure(figsize=(14, 7))
    plt.plot(rolling_sharpe, label='Rolling Sharpe Ratio')
    plt.title('Rolling Sharpe Ratio')
    plt.xlabel('Date')
    plt.ylabel('Sharpe Ratio')
    plt.legend()
    plt.show()

# Run Strategy
ticker = 'AAPL'  # Example: Apple stock
start_date = '2020-01-01'
end_date = '2024-11-09'

data = get_data(ticker, start_date, end_date)
data = add_bollinger_bands(data)
data = generate_signals(data)
final_value, profit_percent = backtest(data)

# Calculate additional metrics
annualized_return, annualized_volatility, sharpe_ratio, max_drawdown = calculate_metrics(data)

# Print results
print(f"Final Portfolio Value: ${final_value:.2f}")
print(f"Total Return: {profit_percent * 100:.2f}%")
print(f"Annualized Return: {annualized_return * 100:.2f}%")
print(f"Annualized Volatility: {annualized_volatility * 100:.2f}%")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"Maximum Drawdown: {max_drawdown * 100:.2f}%")

# Plot strategy and additional metrics
plot_strategy(data)
plot_additional_metrics(data)


