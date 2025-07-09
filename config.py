import os
from dotenv import load_dotenv

def load_api_credentials():
    # Load environment variables from .env file
    load_dotenv()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    # Raise error if either is missing
    if not api_key or not api_secret:
        raise ValueError("API credentials not found. Please set BINANCE_API_KEY and BINANCE_API_SECRET in your .env file.")

    return api_key, api_secret

# Optional: Test block
# if __name__ == "__main__":
#     try:
#         key, secret = load_api_credentials()
#         print("API credentials loaded successfully.")
#     except ValueError as e:
#         print(str(e))
