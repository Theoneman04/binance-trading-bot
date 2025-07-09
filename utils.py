import os
import logging

def setup_logger():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)  # Create 'logs/' if it doesn't exist

    log_file = os.path.join(log_dir, "bot.log")

    logging.basicConfig(
        filename=log_file,
        filemode="a",  # Append to existing file
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

    return logging.getLogger("TradingBot")

# Unit test (runs only when you run this file directly)
# if __name__ == "__main__":
#     logger = setup_logger()
#     logger.info("Logger test: This is an info message.")
#     logger.error("Logger test: This is an error message.")
#     print("Log messages written to logs/bot.log")
