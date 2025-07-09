from bot import BasicBot

def main():
    bot = BasicBot()
    print("Welcome to the Binance Testnet Trading Bot CLI\n")

    symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
    side = input("Enter order side (BUY/SELL): ").upper()
    order_type = input("Enter order type (MARKET/LIMIT): ").upper()
    quantity = input("Enter quantity (e.g., 0.001): ")

    # Validate quantity
    try:
        quantity = float(quantity)
    except ValueError:
        print("Invalid quantity. Must be a number.")
        return

    if order_type == "MARKET":
        print("\nPlacing market order...")
        response = bot.place_market_order(symbol, side, quantity)

    elif order_type == "LIMIT":
        price = input("Enter limit price (e.g., 30000): ")
        try:
            price = float(price)
        except ValueError:
            print("Invalid price. Must be a number.")
            return

        print("\nPlacing limit order...")
        response = bot.place_limit_order(symbol, side, quantity, price)

    else:
        print("Invalid order type. Must be MARKET or LIMIT.")
        return

    # Display response
    if response:
        print("\nOrder Response:")
        for key, value in response.items():
            print(f"{key}: {value}")
    else:
        print("Order failed. Check logs for details.")

if __name__ == "__main__":
    main()
