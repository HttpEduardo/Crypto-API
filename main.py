from crypto_api import get_crypto_price
from alert_system import check_price_alert
from user_interface import get_user_crypto_choice, get_user_alert_price
import time

def main():
    crypto_id = get_user_crypto_choice()
    alert_price = get_user_alert_price()

    while True:
        current_price = get_crypto_price(crypto_id)
        print(f"Current {crypto_id} price: USD {current_price}")

        if check_price_alert(current_price, alert_price):
            print(f"Alert! {crypto_id} has reached the target price of USD {alert_price}.")
            break

        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
