# Simple Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 140,
    "MSFT": 330
}

portfolio = {}

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks: ", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    else:
        print("Invalid stock symbol. Try again.")

# Calculate total investment
total_investment = 0
print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print(f"\nTotal Investment: ${total_investment}")

# Optional: Save to a file
save = input("Do you want to save your portfolio to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Your Portfolio:\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock}: {quantity} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment: ${total_investment}")
    print("Portfolio saved to portfolio_summary.txt")
