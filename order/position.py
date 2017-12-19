from enum import Enum

class OrderType(Enum):
    MARKET = "market"
    LIMIT = "limit"

class Position:
"""Defines a market position by amount, product and type of order
"""

    def __init__(self, product, amount, order_type, post_only, price=0):
        """Initializer creates a new Position instance

        args:
            product (Str): product name
            amount (Float): amount of product
            price (Float): price of product
            order_type (Enum): type of order to place e.g. Market or Limit
            post_only (Bool): is limit order post-only
        """

        self.amount = amount
        self.product = product
        self.order_type = order_type
        self.post_only = post_only

    def __str__(self):
        print("Amount:", self.amount, " Product:", self.product, " OrderType:", self.order_type, " PostOnly:", self.post_only)
