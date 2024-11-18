
# Project 3: Bollinger Bands Strategy  

## Overview  
This project implements a Bollinger Bands trading strategy using historical stock data. The strategy involves:  
- **Buying** shares when the price crosses above the middle band (SMA).  
- **Selling** shares when the price crosses below the middle band.  

The implementation fetches data from Yahoo Finance, calculates Bollinger Bands, generates trading signals, backtests the strategy, computes performance metrics, and visualizes the results.

---

## Files  
- `bollinger_bands_strategy.py`: Main script for running the strategy.  
- `README.md`: Documentation file.  

---

## Dependencies  
The following Python libraries are required:  
- `pandas`  
- `numpy`  
- `yfinance`  
- `matplotlib`  

Install dependencies with:  
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

## Code Features  

1. **Fetch Historical Data**  
   - Retrieves historical stock data from Yahoo Finance.  

2. **Calculate Bollinger Bands**  
   - Computes the Simple Moving Average (SMA) and upper/lower Bollinger Bands.  

3. **Clean Column Names**  
   - Standardizes column names for seamless processing.  

4. **Generate Buy/Sell Signals**  
   - Creates trading signals based on Bollinger Band strategy rules.  

5. **Backtest Strategy**  
   - Simulates trades and calculates the final portfolio value and profitability.  

6. **Calculate Performance Metrics**  
   - Provides metrics such as:  
     - **Annualized Return**  
     - **Annualized Volatility**  
     - **Sharpe Ratio**  
     - **Maximum Drawdown**  

7. **Plot Results**  
   - Visualizes:  
     - Stock prices with Bollinger Bands.  
     - Buy/Sell signals.  
     - Equity curve, cumulative returns, rolling Sharpe Ratio, and drawdowns.  

---

## Example  
Here’s an example using Apple Inc. (AAPL) data from January 1, 2020, to November 9, 2024:  

```python  
from bollinger_bands_strategy import *  

ticker = 'AAPL'  
start_date = '2020-01-01'  
end_date = '2024-11-09'  

# Fetch and process data  
data = get_data(ticker, start_date, end_date)  
data = add_bollinger_bands(data)  
data = generate_signals(data)  

# Backtest the strategy  
final_value, profit_percent = backtest(data)  

# Calculate performance metrics  
annualized_return, annualized_volatility, sharpe_ratio, max_drawdown = calculate_metrics(data)  

# Print results  
print(f"Final Portfolio Value: ${final_value:.2f}")  
print(f"Total Return: {profit_percent * 100:.2f}%")  
print(f"Annualized Return: {annualized_return * 100:.2f}%")  
print(f"Annualized Volatility: {annualized_volatility * 100:.2f}%")  
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")  
print(f"Maximum Drawdown: {max_drawdown * 100:.2f}%")  

# Visualize results  
plot_strategy(data)  
plot_additional_metrics(data)  
```  

---

## Results  
Example output:  

- **Final Portfolio
