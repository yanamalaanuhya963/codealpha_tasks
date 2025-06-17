# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

# Dictionary to store user portfolio
portfolio = {}

# Input loop
print("Enter stock names and quantities (type 'done' to finish):")
while True:
    stock = input("Stock Symbol: ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_investment = 0
print("\nYour Investment Portfolio:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")
    total_investment += value

print(f"\nTotal Investment Value: ${total_investment}")

# Optionally save to file
save = input("Do you want to save this to a file? (yes/no): ").strip().lower()
if save == 'yes':
    file_type = input("Save as .txt or .csv? ").strip().lower()
    filename = input("Enter filename (without extension): ").strip()
    
    if file_type == 'txt':
        with open(filename + ".txt", "w") as f:
            f.write("Investment Portfolio\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
            f.write(f"\nTotal Investment Value: ${total_investment}")
        print(f"Saved to {filename}.txt")
        
    elif file_type == 'csv':
        import csv
        with open(filename + ".csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price per Share", "Total Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
            writer.writerow([])
            writer.writerow(["", "", "Total Investment", total_investment])
        print(f"Saved to {filename}.csv")
        
    else:
        print("Unsupported file type. Data not saved.")
