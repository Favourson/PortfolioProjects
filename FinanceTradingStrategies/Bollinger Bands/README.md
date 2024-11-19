# Bollinger Bands Strategy

## Overview
This project implements a **Bollinger Bands Strategy** using historical stock data. The strategy:
- **Buys shares** when the price crosses above the middle band (Simple Moving Average, SMA).  
- **Sells shares** when the price crosses below the middle band.  

The code utilizes **Yahoo Finance** to fetch historical data, calculates Bollinger Bands, generates buy/sell signals, backtests the strategy, calculates performance metrics, and visualizes the results.

---

## Files
- `bollinger_bands_strategy.py`: Main script to run the strategy.
- `README.md`: Documentation file.

---

## Dependencies
- `pandas`
- `numpy`
- `yfinance`
- `matplotlib`

Install these dependencies using the following command:

```bash
pip install pandas numpy yfinance matplotlib
```

---

## Usage
Run the main script to execute the strategy:

```bash
python bollinger_bands_strategy.py
```

---

## Code Explanation
1. **Fetch Historical Data**: Retrieves historical stock data using Yahoo Finance.
2. **Calculate Bollinger Bands**: Computes the Simple Moving Average (SMA), upper band, and lower band.
3. **Clean Column Names**: Ensures the dataset is properly formatted for processing.
4. **Generate Buy/Sell Signals**: Creates trading signals based on Bollinger Bands crossovers.
5. **Backtest Strategy**: Simulates buying and selling based on signals and calculates the final portfolio value.
6. **Calculate Additional Performance Metrics**: Computes metrics such as:
   - Annualized return
   - Annualized volatility
   - Sharpe Ratio
   - Maximum drawdown
7. **Plot Strategy**: Visualizes the stock price, Bollinger Bands, and buy/sell signals.
8. **Plot Additional Metrics**: Displays metrics such as:
   - Equity curve
   - Returns distribution
   - Cumulative returns
   - Drawdowns
   - Rolling Sharpe Ratio

---

## Example
Below is an example of running the strategy for **Apple Inc. (AAPL)** from January 1, 2020, to November 9, 2024:

```python
# Input Parameters
ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2024-11-09'

# Fetch and Process Data
data = get_data(ticker, start_date, end_date)

# Add Bollinger Bands and Generate Signals
data = add_bollinger_bands(data)
data = generate_signals(data)

# Backtest and Analyze Results
final_value, profit_percent = backtest(data)
annualized_return, annualized_volatility, sharpe_ratio, max_drawdown = calculate_metrics(data)

# Display Results
print(f"Final Portfolio Value: ${final_value:.2f}")
print(f"Total Return: {profit_percent * 100:.2f}%")
print(f"Annualized Return: {annualized_return * 100:.2f}%")
print(f"Annualized Volatility: {annualized_volatility * 100:.2f}%")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"Maximum Drawdown: {max_drawdown * 100:.2f}%")

# Plot the Strategy and Metrics
plot_strategy(data)
plot_additional_metrics(data)
```

---

## Results
After running the script, you'll receive outputs like the following:  
- **Final Portfolio Value**: `$306850.53`  
- **Total Return**: `206.85%`  
- **Annualized Return**: `3.53%`  
- **Annualized Volatility**: `8.50%`  
- **Sharpe Ratio**: `0.30`  
- **Maximum Drawdown**: `-14.20%`

The output includes the following visualizations:
1. Bollinger Bands Strategy plot (close price, SMA, Bollinger Bands, buy/sell markers).
2. Additional metrics:
   - Equity curve
   - Cumulative returns
   - Drawdowns
   - Rolling Sharpe Ratio
   - Returns distribution

---

## Output Example  
*output plots showing the Bollinger Bands strategy results and performance metrics*

---
