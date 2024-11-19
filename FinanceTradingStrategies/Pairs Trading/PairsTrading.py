import pandas as pd
import numpy as np
import yfinance as yf
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Step 1: Fetch historical stock data for two correlated stocks
def get_data(ticker1, ticker2, start_date, end_date):
    # Download historical stock data
    data1 = yf.download(ticker1, start=start_date, end=end_date)['Close']
    data2 = yf.download(ticker2, start=start_date, end=end_date)['Close']
    
    # Print to debug if data is being fetched
    print(f"Data1 ({ticker1}):")
    print(data1.head())
    print(f"Data2 ({ticker2}):")
    print(data2.head())
    
    # Ensure both dataframes have consistent datetime formats
    data1.index = pd.to_datetime(data1.index)
    data2.index = pd.to_datetime(data2.index)
    
    # Check date range for both data series
    print(f"{ticker1} date range: {data1.index.min()} to {data1.index.max()}")
    print(f"{ticker2} date range: {data2.index.min()} to {data2.index.max()}")
    
    # Manually merge dataframes on date index
    merged_data = pd.merge(data1, data2, left_index=True, right_index=True, how='inner', suffixes=(f'_{ticker1}', f'_{ticker2}'))
    
    # Print merged data to check if it's correct
    print("Merged Data:")
    print(merged_data.head())
    
    # Check if merged data is empty
    if merged_data.empty:
        print("Warning: Merged dataset is empty.")
    
    return merged_data

# The rest of the strategy code remains unchanged...

# Step 2: Check for cointegration
def check_cointegration(data):
    coint_result = sm.tsa.stattools.coint(data.iloc[:, 0], data.iloc[:, 1])
    return coint_result

# Step 3: Generate trading signals based on the spread
def generate_signals(data, window=5):
    data['Spread'] = data.iloc[:, 0] - data.iloc[:, 1]
    data['Spread_MA'] = data['Spread'].rolling(window=window).mean()
    data['Spread_Std'] = data['Spread'].rolling(window=window).std()
    data['Z_Score'] = (data['Spread'] - data['Spread_MA']) / data['Spread_Std']
    
    data['Signal'] = np.where(data['Z_Score'] > 1, -1, np.nan)  # Short if Z > 1
    data['Signal'] = np.where(data['Z_Score'] < -1, 1, data['Signal'])  # Long if Z < -1
    data['Signal'] = np.where(np.abs(data['Z_Score']) < 0.5, 0, data['Signal'])  # Exit position if |Z| < 0.5
    data['Position'] = data['Signal'].ffill().fillna(0)
    return data

# Step 4: Backtest the strategy
def backtest(data, initial_capital=100000):
    data['Return'] = (data.iloc[:, 0].pct_change() - data.iloc[:, 1].pct_change()) * data['Position'].shift()
    data['Portfolio_Value'] = initial_capital * (1 + data['Return']).cumprod()
    final_value = data['Portfolio_Value'].iloc[-1]
    return final_value, (final_value - initial_capital) / initial_capital

# Step 5: Calculate performance metrics
def calculate_metrics(data, final_value, initial_capital):
    data['Daily_Return'] = data['Return']
    annual_return = (final_value / initial_capital) ** (252 / len(data)) - 1
    annual_volatility = data['Daily_Return'].std() * np.sqrt(252)
    sharpe_ratio = annual_return / annual_volatility
    drawdown = data['Portfolio_Value'].div(data['Portfolio_Value'].cummax()).sub(1).min()
    sortino_ratio = annual_return / data['Daily_Return'][data['Daily_Return'] < 0].std() * np.sqrt(252)
    return annual_return, annual_volatility, sharpe_ratio, drawdown, sortino_ratio

# Step 6: Plot the strategy
def plot_strategy(data):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Portfolio_Value'], label='Portfolio Value')
    plt.title('Pairs Trading Strategy')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value')
    plt.legend()
    plt.show() 

# Run the project
##ticker1 = 'AAPL'  # Example: Apple
##ticker2 = 'MSFT'  # Example: Microsoft
##start_date = '2020-01-01'
##end_date = '2023-01-01'
##
### Fetch stock data and check for cointegration
##data = get_data(ticker1, ticker2, start_date, end_date)
##
### Check for cointegration
##coint_result = check_cointegration(data)
##print(f"Cointegration Test p-value: {coint_result[1]}")
##
##if coint_result[1] < 0.05:  # Cointegration exists
##    data = generate_signals(data)
##    final_value, profit_percent = backtest(data)
##    annual_return, annual_volatility, sharpe_ratio, drawdown, sortino_ratio = calculate_metrics(data, final_value, 100000)
##    
##    print(f"Final Portfolio Value: ${final_value:.2f}")
##    print(f"Total Return: {profit_percent * 100:.2f}%")
##    print(f"Annual Return: {annual_return * 100:.2f}%")
##    print(f"Annual Volatility: {annual_volatility * 100:.2f}%")
##    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
##    print(f"Maximum Drawdown: {drawdown * 100:.2f}%")
##    print(f"Sortino Ratio: {sortino_ratio:.2f}")
##    
##    plot_strategy(data)
##else:
##    print("The selected stocks are not cointegrated, please choose different pairs.")


# Run the project with new pairs
ticker1 = 'BTI'  # Example: British American Tobacco
ticker2 = 'PM'  # Example: Philip Morris International
start_date = '2020-01-01'
end_date = '2023-01-01'

# Fetch stock data and check for cointegration
data = get_data(ticker1, ticker2, start_date, end_date)

# Check for cointegration
coint_result = check_cointegration(data)
print(f"Cointegration Test p-value: {coint_result[1]}")

if coint_result[1] < 0.05:  # Cointegration exists
    data = generate_signals(data)
    final_value, profit_percent = backtest(data)
    annual_return, annual_volatility, sharpe_ratio, drawdown, sortino_ratio = calculate_metrics(data, final_value, 100000)
    
    print(f"Final Portfolio Value: ${final_value:.2f}")
    print(f"Total Return: {profit_percent * 100:.2f}%")
    print(f"Annual Return: {annual_return * 100:.2f}%")
    print(f"Annual Volatility: {annual_volatility * 100:.2f}%")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Maximum Drawdown: {drawdown * 100:.2f}%")
    print(f"Sortino Ratio: {sortino_ratio:.2f}")
    
    plot_strategy(data)
else:
    print("The selected stocks are not cointegrated, please choose different pairs.")
