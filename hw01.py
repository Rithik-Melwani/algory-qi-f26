import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

appl = yf.Ticker("AAPL")
spy = yf.Ticker("SPY")

appl_data = appl.history(start="2025-09-01", end="2026-09-01")
appl_close = appl_data['Close'].round(2)
appl_return = (appl_close.iloc[-1] - appl_close.iloc[0])/appl_close.iloc[0]
daily_appl_return = appl_close.pct_change()
daily_appl_std = daily_appl_return.std()
appl_ann_vol = daily_appl_std * np.sqrt(252)
print(appl_close)
print("Ticker: AAPL")
print(f"Number of days: {len(appl_close)}")
print("First Date: 2025-09-02")
print("Last Date: 2026-09-01")
print(f"Last Close: {(appl_close.iloc[-1]).round(2)}")
print(f"Return Over Year: {appl_return*100:.2f}%")
print (f"Annualized Volatility: {appl_ann_vol:.4f}")
print(f"Annualized Volatility as a Percentage: {appl_ann_vol * 100:.2f}%")
print("")

spy_data = spy.history(start="2025-09-01", end="2026-09-01")
spy_close = spy_data['Close'].round(2)
spy_return = (spy_close.iloc[-1] - spy_close.iloc[0])/spy_close.iloc[0]
daily_spy_return = spy_close.pct_change()
daily_spy_std = daily_spy_return.std()
spy_ann_vol = daily_spy_std * np.sqrt(252)
print(spy_close)
print("Ticker: SPY")
print(f"Number of days: {len(spy_close)}")
print("First Date: 2025-09-02") 
print("Last Date: 2026-09-01")
print(f"Last Close: {(spy_close.iloc[-1]).round(2)}")
print(f"Return Over Year: {spy_return*100:.2f}%")
print (f"Annualized Volatility: {spy_ann_vol:.4f}")
print(f"Annualized Volatility as a Percentage: {spy_ann_vol * 100:.2f}%")

appl_rebased = (appl_close/appl_close.iloc[0]) * 100
spy_rebased = (spy_close/spy_close.iloc[0]) * 100

plt.figure(figsize=(12, 6))
plt.plot(appl_rebased.index, appl_rebased, label="AAPL")
plt.plot(spy_rebased.index, spy_rebased, label="SPY")

plt.title("AAPL vs SPY: Rebased Performance (Start = 100)")
plt.xlabel("Date")
plt.ylabel("Rebased Price (Start = 100)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()