def check_price_alert(crypto_price, alert_price):
    if crypto_price <= alert_price:
        return True
    return False
