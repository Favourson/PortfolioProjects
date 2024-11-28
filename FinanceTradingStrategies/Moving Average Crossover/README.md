# Moving Average Crossover Strategy

## Overview
This project implements a **Moving Average Crossover Strategy** using historical stock data. The strategy:
- **Buys shares** when the short-term moving average crosses above the long-term moving average.
- **Sells shares** when the short-term moving average crosses below the long-term moving average.  

The code utilizes **Yahoo Finance** to fetch historical data, calculates moving averages, generates buy/sell signals, backtests the strategy, and plots the results.

---

## Files
- `moving_average_crossover.py`: Main script to run the strategy.
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
python moving_average_crossover.py
```

---

## Code Explanation
1. **Fetch Historical Data**: Retrieves historical stock data using Yahoo Finance.
2. **Calculate Moving Averages**: Computes the short-term and long-term moving averages.
3. **Generate Buy/Sell Signals**: Generates trading signals based on moving average crossovers.
4. **Backtest Strategy**: Simulates buying and selling based on signals and calculates the final portfolio value.
5. **Plot Strategy**: Visualizes the stock price, moving averages, and buy/sell signals.

---

## Example
Below is an example of running the strategy for **Apple Inc. (AAPL)** from January 1, 2020, to November 9, 2024:

```python
# Input Parameters
ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2024-11-09'
short_window = 50
long_window = 200

# Fetch and Process Data
data = get_data(ticker, start_date, end_date)
data = add_moving_averages(data, short_window, long_window)
data = generate_signals(data, short_window)

# Backtest and Analyze Results
final_value, profit_percent = backtest(data)

# Display Results
print(f"Final Portfolio Value: ${final_value:.2f}")
print(f"Total Return: {profit_percent * 100:.2f}%")

# Plot the Strategy
plot_strategy(data)
```

---

## Results
After running the script, you'll receive outputs similar to the following:  
- **Final Portfolio Value**: `$160617.77`
- **Total Return**: `60.62%`

The output plot will show:
1. Stock close prices.
2. Short-term and long-term moving averages.
3. Buy and Sell markers.

---

## Output Example  
![MA1](https://github.com/user-attachments/assets/ee89d093-3794-403e-87c7-38a5449a3676)


---
