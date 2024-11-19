# Pairs Trading Strategy

## Overview
This project implements a **Pairs Trading Strategy** using historical stock data. The strategy:  
1. **Checks cointegration** between two stocks.  
2. **Generates trading signals** based on the spread between the two stocks.  
3. **Backtests the strategy**, calculates performance metrics, and visualizes the results.

---

## Files
- `pairs_trading_strategy.py`: Main script to run the strategy.
- `README.md`: Documentation file.

---

## Dependencies
- `pandas`
- `numpy`
- `yfinance`
- `statsmodels`
- `matplotlib`

Install these dependencies using the following command:

```bash
pip install pandas numpy yfinance statsmodels matplotlib
```

---

## Usage
Run the main script to execute the strategy:

```bash
python pairs_trading_strategy.py
```

---

## Code Explanation
1. **Fetch Historical Data**: Retrieves historical data for two correlated stocks using Yahoo Finance.
2. **Check Cointegration**: Tests for cointegration between the two stocks using statistical methods.
3. **Generate Trading Signals**: Creates buy/sell signals based on the spread between the two stocks.
4. **Backtest Strategy**: Simulates buying and selling based on the signals and calculates the portfolio's performance.
5. **Calculate Performance Metrics**: Computes metrics such as:
   - Annual return
   - Annual volatility
   - Sharpe Ratio
   - Maximum drawdown
   - Sortino Ratio
6. **Plot Strategy**: Visualizes the portfolio's value over time.

---

## Example
Below is an example of running the strategy for **British American Tobacco (BTI)** and **Philip Morris International (PM)** from January 1, 2020, to January 1, 2023:

```python
# Input Parameters
ticker1 = 'BTI'
ticker2 = 'PM'
start_date = '2020-01-01'
end_date = '2023-01-01'

# Fetch and Process Data
data = get_data(ticker1, ticker2, start_date, end_date)

# Check Cointegration
coint_result = check_cointegration(data)
if coint_result[1] < 0.05:  # Check if p-value < 0.05 (significant cointegration)
    # Generate Signals and Backtest
    data = generate_signals(data)
    final_value, profit_percent = backtest(data)

    # Calculate Performance Metrics
    annual_return, annual_volatility, sharpe_ratio, drawdown, sortino_ratio = calculate_metrics(data, final_value, 100000)

    # Display Results
    print(f"Final Portfolio Value: ${final_value:.2f}")
    print(f"Total Return: {profit_percent * 100:.2f}%")
    print(f"Annual Return: {annual_return * 100:.2f}%")
    print(f"Annual Volatility: {annual_volatility * 100:.2f}%")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Maximum Drawdown: {drawdown * 100:.2f}%")
    print(f"Sortino Ratio: {sortino_ratio:.2f}")

    # Plot the Strategy
    plot_strategy(data)
else:
    print("The selected stocks are not cointegrated, please choose different pairs.")
```

---

## Results
After running the script, you'll receive outputs like the following:  
- **Final Portfolio Value**: `$134248.67`  
- **Total Return**: `34.25%`  
- **Annual Return**: `10.32%`  
- **Annual Volatility**: `19.50%`  
- **Sharpe Ratio**: `0.53`  
- **Maximum Drawdown**: `-36.48%`  
- **Sortino Ratio**: `173.85`

The output plot will show:
1. The portfolio value over time.
2. Buy/Sell markers and trading signals.

---

## Output Example  
*plot of the strategy results*

---