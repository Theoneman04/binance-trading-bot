from binance.client import Client
from binance.exceptions import BinanceAPIException
from config import load_api_credentials
from utils import setup_logger

class BasicBot:
    def __init__(self):
        api_key, api_secret = load_api_credentials()
        self.logger = setup_logger()

        # Connect to Binance SPOT Testnet
        self.client = Client(api_key, api_secret)
        self.client.API_URL = "https://testnet.binance.vision/api"

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=quantity
            )
            self.logger.info(f"Market Order Placed: {order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Error placing market order: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side.upper(),
                type="LIMIT",
                timeInForce="GTC",  # Good-Till-Cancelled
                quantity=quantity,
                price=price
            )
            self.logger.info(f" Limit Order Placed: {order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f" Error placing limit order: {e}")
            return None

# Optional: Run standalone to test
# if __name__ == "__main__":
#     bot = BasicBot()

#     # Market order test (BUY 0.001 BTC)
#     response = bot.place_market_order("BTCUSDT", "BUY", 0.001)
#     print("Market Order Response:", response)

#     # Uncomment this if you want to test a limit order too
#     # response = bot.place_limit_order("BTCUSDT", "SELL", 0.001, 65000)
#     # print("Limit Order Response:", response)
