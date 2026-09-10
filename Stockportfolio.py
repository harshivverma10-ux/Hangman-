# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 200,
    "MSFT": 400
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print("Stock Price:", stock_prices[stock])
        print("Investment:", investment)
        print()
    else:
        print("Stock not available.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        print()

print("===================================")
print("Total Investment:", total_investment)
print("===================================")