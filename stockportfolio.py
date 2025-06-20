# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2750,
    "MSFT": 330
}

# Dictionary to store user's stock holdings
portfolio = {}

# Get user input
while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print(f"Sorry, we don't have price data for {stock}.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_value = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Optionally save to file
save = input("Do you want to save this report to a CSV file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.csv", "w") as file:
        file.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            file.write(f"{stock},{qty},{price},{value}\n")
        file.write(f",,,Total: ${total_value}\n")
    print("Portfolio saved to 'portfolio_summary.csv'")
