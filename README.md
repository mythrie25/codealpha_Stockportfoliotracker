# 📊 Stock Portfolio Tracker (Simple Version)

This is a simple **Stock Portfolio Tracker** written in Python that allows users to enter their stock holdings, calculate the total investment value, and optionally save the results to a CSV file.

> 💡 This version uses **hardcoded stock prices** for demo purposes.

---

## ✅ Features

- User inputs stock symbols and quantities
- Checks availability of stock in the predefined price list
- Calculates individual and total investment value
- Option to save the report as a CSV file

---

## 🖥️ How It Works

1. The user is prompted to enter stock symbols (like `AAPL`, `TSLA`, etc.)
2. If the stock is available, the user enters the quantity they own.
3. The script calculates and displays:
   - Value of each stock (`quantity × price`)
   - Total portfolio value
4. User can choose to save the portfolio as `portfolio_summary.csv`

---

## 💡 Example Run

```plaintext
Enter stock symbol (or type 'done' to finish): AAPL
Enter quantity for AAPL: 4
Enter stock symbol (or type 'done' to finish): MSFT
Enter quantity for MSFT: 1
Enter stock symbol (or type 'done' to finish): done

Your Portfolio:
AAPL: 4 shares × $180 = $720
MSFT: 1 share × $330 = $330

Total Investment Value: $1050
Do you want to save this report to a CSV file? (yes/no): yes
Portfolio saved to 'portfolio_summary.csv'


