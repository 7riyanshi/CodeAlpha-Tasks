# Manually defined stock prices (as required by the task)
stock_price_list = {
    "TCS": 3500,
    "INFY": 1500,
    "WIPRO": 420,
    "RELIANCE": 2800
}

# Dictionary to store user portfolio
user_portfolio = {}

print("Stock Portfolio Tracker")
print("-----------------------")
print("Available Stocks:")

for stock, price in stock_price_list.items():
    print(f"{stock} : Price per share = {price}")

print("\nPlease enter your investment details.")

# Take number of stocks from user
try:
    total_stocks = int(input("Enter number of different stocks you own: "))
    if total_stocks <= 0:
        print("Number of stocks must be greater than zero.")
        exit()
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit()

# Collect stock and quantity details
for i in range(total_stocks):
    stock_name = input("\nEnter stock symbol: ").upper().strip()

    if stock_name not in stock_price_list:
        print("This stock is not available in the predefined list.")
        continue

    try:
        shares = int(input("Enter number of shares: "))
        if shares <= 0:
            print("Shares must be greater than zero.")
            continue
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        continue

    if stock_name in user_portfolio:
        user_portfolio[stock_name] += shares
    else:
        user_portfolio[stock_name] = shares

# Display portfolio summary
print("\nInvestment Summary")
print("------------------")

grand_total = 0

for stock, shares in user_portfolio.items():
    price = stock_price_list[stock]
    investment_amount = price * shares
    grand_total += investment_amount

    print(
        f"Stock: {stock} | Shares: {shares} | "
        f"Price: {price} | Total Value: {investment_amount}"
    )

print("\nTotal Portfolio Value:", grand_total)
