FIVE_MINUTES_IN_SEC = 300
TEN_SEC = 10
GRANULARITY_SEC = 59


class Strategy:

    def execute(self):
        raise NotImplementedError

    def run(self):
        # TODO make multi-threaded or implement some way of finishing gracefully
        raise NotImplementedError

    @staticmethod
    def make_moving_average_crossover(info_provider, order_engine, position, interval=TEN_SEC, candle_size=GRANULARITY_SEC):
        from cryptotrading.strategy.moving_average_crossover import MovingAverageCrossover
        return MovingAverageCrossover(info_provider, order_engine, position, interval, candle_size)
