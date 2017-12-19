import gdax

class OrderEngine:

    def open(self, position):
        raise NotImplementedError

    def close(self, position):
        raise NotImplementedError

    @staticmethod
    def make_gdax(config):
        from cryptotrading.order.gdax_orderengine import GdaxOrderEngine
        return GdaxOrderEngine(config)

    @staticmethod
    def make_gdax_mock(config):
        from cryptotrading.order.gdax_orderengine import GdaxOrderEngineMock
        return GdaxOrderEngineMock(config)
