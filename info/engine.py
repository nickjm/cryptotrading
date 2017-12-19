import gdax


class InfoEngine:

    def last_filled_order_price(self, product):
        raise NotImplementedError

    def highest_buy_price(self, product):
        raise NotImplementedError

    def moving_average(self, product, start, end, candle_size):
        raise NotImplementedError

    @staticmethod
    def make_gdax(config):
        from cryptotrading.info.gdax_infoengine import GdaxInfoEngine
        return GdaxInfoEngine(config)
