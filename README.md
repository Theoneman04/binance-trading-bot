# 🧠 Binance Testnet Trading Bot

A simplified crypto trading bot built in Python using the **Binance Spot Testnet**.  
This project was developed as part of the hiring task for the **Junior Python Developer** role.

## ✅ Features
- 🔐 Secure API key handling via `.env` file  
- 📈 Supports **Market** and **Limit** orders (Buy/Sell)  
- 🧪 Uses Binance **Spot Testnet** (no real funds required)  
- 🛠 Command-line interface for user-friendly input/output  
- 🪵 Logs all API requests, responses, and errors to the `logs/` folder  

## 🧰 Tech Stack
- Python 3.10+  
- [`python-binance`](https://github.com/sammchardy/python-binance)  
- `python-dotenv` for environment variable management  
- `logging` for error/info tracking  

## 🚀 Getting Started

### Step 1: Clone the Repository
```bash
git clone https://github.com/Theoneman04/binance-trading-bot.git
cd binance-trading-bot
```

### Step 2: Create & Activate a Virtual Environment
```bash
python -m venv myvenv
myvenv\Scripts\activate    # On Windows
# OR
source myvenv/bin/activate # On macOS/Linux
```

### Step 3: Install Project Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create a `.env` File
Create a new `.env` file in the project root and add your Binance API credentials:
```env
BINANCE_API_KEY=your_key_here
BINANCE_API_SECRET=your_secret_here
```
> You can get API keys from the [Binance Spot Testnet](https://testnet.binance.vision/)

### Step 5: Run the Bot Using the CLI
```bash
python cli.py
```
Follow the on-screen prompts:
```
Enter trading pair (e.g., BTCUSDT): BTCUSDT
Enter order side (BUY/SELL): BUY
Enter order type (MARKET/LIMIT): MARKET
Enter quantity (e.g., 0.001): 0.001
```

## 📁 Project Structure
```
binance-trading-bot/
├── bot.py            # Trading logic (places orders via Binance API)
├── cli.py            # Interactive command-line interface
├── config.py         # Loads API credentials from .env
├── utils.py          # Logger setup and helper functions
├── logs/             # Stores log files (gitignored)
├── .env.example      # Example .env template
├── requirements.txt  # Project dependencies
└── README.md         # Project overview and instructions
```

## 🧪 Logs
Sample log entries:
```
[INFO] Placed MARKET BUY order: BTCUSDT qty=0.001
[ERROR] Failed to place LIMIT SELL order: Invalid price
```
Logs are automatically saved to the `logs/` directory.


## 🛡 Disclaimer
This bot is built for educational/demo purposes and operates only on Binance’s **Testnet**. No real trades or real money are involved.

## 📜 License
MIT
