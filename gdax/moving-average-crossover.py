# A basic Moving Average Crossover strategy
import gdax
import time
import datetime


GRANULARITY_SEC = 59
FIVE_MINUTES = 300
TEN_MINUTES = 600
THIRTY_MINUTES = 1800

class MACBot:

    def __init__(self, public_client, product, auth_client):
        self.invested = False
        self.public_client = public_client
        self.product = product
        self.auth_client = auth_client

    def tick(self):
        print(" =========== tick =========== ")
        decision_time = 0
        current_time = datetime.datetime.utcnow()
        time_delta_short = datetime.timedelta(seconds=TEN_MINUTES)
        time_delta_long = datetime.timedelta(seconds=THIRTY_MINUTES)
        begin_short = current_time - time_delta_short
        begin_long = current_time - time_delta_long
        short_term = self.public_client.get_product_historic_rates(product_id=self.product, start=begin_short.isoformat(), end=current_time.isoformat(), granularity=GRANULARITY_SEC)
        long_term = self.public_client.get_product_historic_rates(product_id=self.product, start=begin_long.isoformat(), end=current_time.isoformat(), granularity=GRANULARITY_SEC)
        if (not(isinstance(short_term, list) and isinstance(long_term, list))):
            return
        short_moving_avg = sum([x[4] for x in short_term]) / len(short_term)
        long_moving_avg = sum([x[4] for x in long_term]) / len(long_term)
        last_price = short_term[-1][4]

        # TODO incorporate open orders into decision making
        # TODO maybe utilize real time feed to cut latency down - need to
        #      increase odds that limit order is executed
        #      - additionally take later steps to readjust limit order if not
        #        exectuted

        if (True) and not self.invested:
            # Buy 0.01 LTC @ 100 USD
            self.auth_client.buy(price=str(last_price), #USD
                           size='1.00', #BTC
                           product_id=self.product)
            decision_time = datetime.datetime.utcnow()
            self.invested = True
            print("Result: Buying {0}".format(self.product))
        elif (short_moving_avg < long_moving_avg) and self.invested:
            self.auth_client.sell(price=str(last_price),
                             size='1.00',
                             product_id=self.product)
            decision_time = datetime.datetime.utcnow()
            self.invested = False
            print("Result: Selling {0}".format(self.product))
        else:
            print("Result: No action taken")

        print("\nStats")
        print("Start Time:")
        print(current_time)
        print("Decision Time:")
        print(decision_time)
        print("Short Term Moving Average:")
        print(short_moving_avg)
        print("Long Term Moving Average:")
        print(long_moving_avg)
        print("\n\n ============================ ")

        return


if __name__ == '__main__':
    public_client = gdax.PublicClient()
    # TODO load credentials from private config file or cl args
    key = 'your_key_here'
    b64secret = 'your_secret_here'
    passphrase = 'your_passphrase_here'
    auth_client = gdax.AuthenticatedClient(key, b64secret, passphrase,
                                  api_url="https://api.gdax.com") # https://api-public.sandbox.gdax.com
    bot = MACBot(public_client, 'BTC-USD', auth_client) # Update your instrument here
    while True:
        bot.tick()
        time.sleep(FIVE_MINUTES)
    # TODO pass in granularity and periods via args / explore different values
