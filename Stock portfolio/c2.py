stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 300,
}
total_investment = 0
print("Available stocks:", list(stock_prices.keys()))
while True:
    stock = input("\nEnter stock name : ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        price = stock_prices[stock]
        investment = price * quantity
        print(f"Investment in {stock}: {investment}")
        total_investment += investment
    else:
        print("Stock not found!")
print("\nTotal Investment Value:", total_investment)
save = input("Do you want to save result to file? (yes/no): ").lower()
if save == "yes":
    file = open("portfolio.txt", "w")
    file.write(f"Total Investment: {total_investment}")
    file.close()
    print("Saved to portfolio.txt")