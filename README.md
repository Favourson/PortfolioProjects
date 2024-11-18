Project 3: Bollinger Bands Strategy

![image](https://github.com/user-attachments/assets/bee5de89-4e85-4c5c-bfb5-9656e827672c)

Overview
This project implements a Bollinger Bands Strategy using historical stock data. The strategy buys shares when the price crosses above the middle band (SMA) and sells shares when the price crosses below the middle band. The code uses Yahoo Finance to fetch historical data, calculates Bollinger Bands, generates buy/sell signals, backtests the strategy, calculates additional performance metrics, and plots the results.

Files
bollinger_bands_strategy.py: Main script to run the strategy.

README.md: Documentation file.

Dependencies
pandas

numpy

yfinance

matplotlib

You can install these dependencies using:

bash
pip install pandas numpy yfinance matplotlib
Usage
Run the main script to execute the strategy:

bash
python bollinger_bands_strategy.py
Code Explanation
Fetch Historical Data: Fetches historical stock data using Yahoo Finance.

Calculate Bollinger Bands: Calculates the Simple Moving Average (SMA) and Bollinger Bands.

Clean Column Names: Ensures column names are suitable for processing.

Generate Buy/Sell Signals: Generates trading signals based on the Bollinger Bands strategy.

Backtest Strategy: Simulates buying and selling based on generated signals and calculates the final portfolio value.

Calculate Additional Performance Metrics: Calculates additional metrics such as annualized return, annualized volatility, Sharpe Ratio, and Maximum Drawdown.

Plot Strategy: Visualizes the close price, SMA, Bollinger Bands, and buy/sell signals.

Plot Additional Metrics: Visualizes additional metrics such as the equity curve, returns distribution, cumulative returns, drawdowns, and rolling Sharpe Ratio.

Example
Here’s an example of running the strategy for Apple Inc. (AAPL) from January 1, 2020, to November 9, 2024:

python
ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2024-11-09'

data = get_data(ticker, start_date, end_date)
data = add_bollinger_bands(data)
data = generate_signals(data)
final_value, profit_percent = backtest(data)

annualized_return, annualized_volatility, sharpe_ratio, max_drawdown = calculate_metrics(data)

print(f"Final Portfolio Value: ${final_value:.2f}")
print(f"Total Return: {profit_percent * 100:.2f}%")
print(f"Annualized Return: {annualized_return * 100:.2f}%")
print(f"Annualized Volatility: {annualized_volatility * 100:.2f}%")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"Maximum Drawdown: {max_drawdown * 100:.2f}%")

plot_strategy(data)
plot_additional_metrics(data)
Results
Final Portfolio Value: $XXX.XX

Total Return: XX.XX%

Annualized Return: XX.XX%

Annualized Volatility: XX.XX%

Sharpe Ratio: XX.XX

Maximum Drawdown: XX.XX%

Include the output plots:
