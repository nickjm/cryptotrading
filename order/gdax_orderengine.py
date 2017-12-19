from cryptotrading.order.engine import OrderEngine
import gdax


class GdaxOrderEngine(OrderEngine):

    def __init__(self, auth_client):
        self.auth_client = gdax.AuthenticatedClient(config.key, config.b64secret, config.passphrase, api_url=config.url)

    def open(self, position):
        print("Opening position:\n", position)
        response = self.auth_client.buy(price=str(position.price),
                                        size=str(position.amount),
                                        product_id=position.product)
        print("GDAX Buy Order Response:\n", response)
        return True

    def close(self, position):
        print("Closing position:\n", position)
        response = self.auth_client.sell(price=str(position.price),
                                         size=str(position.amount),
                                         post_only=str(position.post_only),
                                         product_id=position.product)
        print("GDAX Sell Order Response:\n", response)
        return True


class GdaxOrderEngineMock(OrderEngine):

    def __init__(self, auth_client):
        self.auth_client = None

    def open(self, position):
        print("MOCK: Opening position:\n", position)
        return True

    def close(self, position):
        print("MOCK: Closing position:\n", position)
        return True
