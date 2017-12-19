from cryptotrading.info.engine import InfoEngine
from cryptotrading.gdax.realtime_client import RealtimeClient
import gdax


class GdaxInfoEngine(InfoEngine):

    def __init__(self, config):
        self.public_client = gdax.PublicClient()
        # self.auth_client = gdax.AuthenticatedClient(config.key, config.b64secret, config.passphrase, api_url=config.url)
        # self.realtime_client = RealtimeClient()
        # self.realtime_client.start()

    def last_filled_order_price(self, product):
        """Last filled order price for product
        """
        pass

    def highest_buy_price(self, product):
        """Highest buy limit order price curently on the order book for product
        """
        pass

    def moving_average(self, product, start, end, candle_size):
        """Calculate moving average from start time to end time

        args:
            product (Str): product aka instrument
            start (Str): iso formatted string of begin time
            end (Str): iso formatted string of end time
            candle_size (Int): granularity size of candle in secs
        """
        rates = self.public_client.get_product_historic_rates(product_id=product, start=start, end=end, granularity=candle_size)
        if (not(isinstance(rates, list)
            return -1
        moving_avg = sum([x[4] for x in rates]) / len(rates)
        return moving_avg
