stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter Stock Name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue

    quantity = int(input(f"Enter quantity of {stock_name}: "))

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

print("\n===== Portfolio Summary =====")
print("{:<10}{:<10}{:<10}{:<10}".format("Stock", "Price", "Qty", "Value"))

for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print("{:<10}${:<9}{:<10}${:<10}".format(stock, stock_prices[stock], qty, value))

print("\nTotal Investment Value = $", total_investment)

# Save report to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-------------------------\n")

    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        file.write(f"{stock} - Quantity: {qty}, Value: ${value}\n")

    file.write(f"\nTotal Investment: ${total_investment}")

print("\nPortfolio saved successfully in 'portfolio_summary.txt'")