from cryptotrading.strategy.strategy import Strategy
from enum import Enum
import time


class Signal(Enum):
    BUY = 1
    SELL = 2
    WAIT = 3


class MovingAverageCrossover(Strategy):

    def __init__(self, info_provider, order_engine, position, interval, candle_size):
        # Generic Strategy Providers - These two interfaces are the bread and
        #  butter of every strategy, providing the two basic suite of functions:
        #  informational functions, and order placement functions
        self.info_provider = info_provider
        self.order_engine = order_engine
        # Moving-Average specific parameters (that could also be shared by other strategies)
        self.position = position
        self.interval = interval
        self.candle_size = candle_size
        # Moving Average specific state
        self.is_started = False
        self.has_open_position = False
        self.last_signal = Signal.WAIT

    def execute(self):
        """Executes one iteration of the Moving Average Crossover Strategy
        """
        print("Executing moving average crossover strategy")
        current_time = datetime.datetime.utcnow()
        time_delta_short = datetime.timedelta(seconds=short_interval)
        time_delta_long = datetime.timedelta(seconds=long_interval)
        begin_short = (current_time - time_delta_short).isoformat()
        begin_long = (current_time - time_delta_long).isoformat()
        end = current_time.isoformat()
        short_term_moving_average = self.info_provider.moving_average(self.position.product, begin_short, end, self.candle_size)
        long_term_moving_average = self.info_provider.moving_average(self.position.product, begin_long, end, self.candle_size)
        if short_term_moving_average > long_term_moving_average:
            # Buy signal
            if self.last_signal == Signal.SELL and self.has_open_position == False:
                self.position.price = self.info_provider.highest_buy_price
                success = self.order_engine.open(position)
                if success:
                    self.has_open_position = True
            self.last_signal = Signal.BUY
        elif short_term_moving_average < long_term_moving_average:
            # Sell signal
            if self.has_open_position:
                self.order_engine.close(position)
            self.last_signal = Signal.SELL

    def run(self):
        """Every self.interval seconds, execute one iteration of the strategy
        """
        # TODO Implement graceful shutdown, probably with multi-threading
        while True:
            self.execute()
            time.sleep(self.interval)

    def __str__(self):
        print("TODO")
