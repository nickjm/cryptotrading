from cryptotrading.info.engine import InfoEngine
from cryptotrading.order.engine import OrderEngine
from cryptotrading.order.position import OrderType, Position
from cryptotrading.strategy.strategy import Strategy
from cryptotrading.gdax.config import config
# from cryptotrading.gdax.config_sandbox import config
import sys
import argparse


if __name__ == '__main__':
    # TODO Implement Argparse
    parser = argparse.ArgumentParser(description='Run a cryptocurrency trading algorithm on specified exchange.')
    parser.add_argument('--strategy', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    product = sys.argv[1]
    amount = sys.argv[2]
    order_type = OrderType.LIMIT
    post_only = True
    position = Position(product, amount, order_type, post_only)
    gdax_order_engine = OrderEngine.make_gdax_mock(config)
    gdax_info_engine = InfoEngine.make_gdax(config)
    strat = Strategy.make_moving_average_crossover(gdax_info_engine, gdax_order_engine, position)
