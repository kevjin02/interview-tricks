"""
Strategy pattern, use for big if/elif chains
Very good for input processing, examples include:

Key Value Store
in: ["ADD dog sophie", "ADD cat leon", "GET dog", "GET cat", "DELETE dog", "UPDATE cat leonardo"]

Stock Market
in: ["SET AAPL 50", "SET GOOG 50", "BUY AAPL 100", "SELL GOOG 10", "SET GOOG 30"]

Natural Language Processing
in: [
    {intent: "order_food", entities: {product: "hamburger", quantity: 1}},
    {intent: "order_drink", entities: {size: "large"}},
    {intent: "show_hours"},
    {intent: "process_allergies", entities: {allergies: ["peanuts", "shellfish"]}}
]

"""


"""
-------------------------------DON'T DO THIS-------------------------------
"""
def get_portfolio_value_without_strategy(data: list, money: int) -> int:
    stock_portfolio = {}
    stock_prices = {}
    portfolio_value = money

    for command in data:
        action = command.split()[0]
        if action == "SET":
            stock = command.split()[1]
            price = command.split()[2]
            stock_prices[stock] = price
        elif action == "BUY":
            stock = command.split() [1]
            quantity = command.split()[2]
            stock_portfolio[stock] = stock_portfolio.get(stock, 0) + int(quantity)
            portfolio_value -= int(stock_prices[stock]) * int(quantity)
        elif action == "SELL":
            stock = command.split()[1]
            quantity = command.split()[2]
            stock_portfolio[stock] = stock_portfolio.get(stock, 0) - int(quantity)
            portfolio_value += int(stock_prices[stock]) * int(quantity)

    for stock in stock_portfolio:
        portfolio_value += int(stock_prices[stock]) * stock_portfolio[stock]

    return portfolio_value


"""
-------------------------------DO THIS INSTEAD-------------------------------
"""
from abc import ABC, abstractmethod


class TradeStrategy(ABC):

    @abstractmethod
    def execute(self, command: str, stock_portfolio: dict, stock_prices: dict, portfolio_value: int) -> int:
        pass


class SetStrategy(TradeStrategy):

    def execute(self, command: str, stock_portfolio: dict, stock_prices: dict, portfolio_value: int) -> int:
        _, stock, price = command.split()
        stock_prices[stock] = int(price)
        return portfolio_value


class BuyStrategy(TradeStrategy):

    def execute(self, command: str, stock_portfolio: dict, stock_prices: dict, portfolio_value: int) -> int:
        _, stock, quantity = command.split()
        stock_portfolio[stock] = stock_portfolio.get(stock, 0) + int(quantity)
        portfolio_value -= int(stock_prices[stock]) * int(quantity)
        return portfolio_value


class SellStrategy(TradeStrategy):
        
    def execute(self, command: str, stock_portfolio: dict, stock_prices: dict, portfolio_value: int) -> int:
        _, stock, quantity = command.split()
        stock_portfolio[stock] = stock_portfolio.get(stock, 0) - int(quantity)
        portfolio_value += int(stock_prices[stock]) * int(quantity)
        return portfolio_value


TRADE_STRATEGIES = {
    "SET": SetStrategy(),
    "BUY": BuyStrategy(),
    "SELL": SellStrategy()
}


def get_portfolio_value_with_strategy(data: list, money: int) -> int:
    stock_portfolio = {}
    stock_prices = {}
    portfolio_value = money

    for command in data:
        action = command.split()[0]

        # One liner to execute strategy
        portfolio_value = TRADE_STRATEGIES[action].execute(command, stock_portfolio, stock_prices, portfolio_value)

    for stock in stock_portfolio:
        portfolio_value += int(stock_prices[stock]) * stock_portfolio[stock]

    return portfolio_value


# print(get_portfolio_value(["SET AAPL 50", "SET GOOG 50", "BUY GOOG 10", "SET GOOG 30","SELL GOOG 10", "SET GOOG 10"], 1000))