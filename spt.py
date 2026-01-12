STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130
}

print("📈 Welcome to Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(STOCK_PRICES.keys()))
print("-" * 40)

portfolio = {}
total_investment = 0

while True:
    stock_name = input("Enter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in STOCK_PRICES:
        print("❌ Stock not found. Please choose from the available list.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        portfolio[stock_name] = quantity
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

print("\n🧾 Investment Summary")
print("-" * 40)

for stock, qty in portfolio.items():
    value = STOCK_PRICES[stock] * qty
    total_investment += value
    print(f"{stock} | Quantity: {qty} | Value: ${value}")

print("-" * 40)
print(f"💰 Total Investment Value: ${total_investment}")
save_choice = input("\nDo you want to save the result? (yes/no): ").lower()

if save_choice == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-" * 30 + "\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock} - Quantity: {qty}, Price: ${STOCK_PRICES[stock]}\n")
        file.write(f"\nTotal Investment: ${total_investment}")

    print("✅ Data saved successfully in 'portfolio_summary.txt'")

print("\n🚀 Program completed successfully!")