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
def in_memory_store_no_strategy(data: list) -> dict:
    store = {}
    for command in data:
        action, *args = command.split()
        if action == "ADD":
            key, value = args
            store[key] = value
        elif action == "GET":
            key = args[0]
            print(store[key])
        elif action == "DELETE":
            key = args[0]
            del store[key]
        elif action == "UPDATE":
            key, value = args
            store[key] = value
    return store
"""
-------------------------------DO THIS INSTEAD-------------------------------
"""
from abc import ABC, abstractmethod


class CommandStrategy(ABC):
    @abstractmethod
    def execute(self, store: dict, *args):
        pass


class AddCommand(CommandStrategy):
    def execute(self, store: dict, *args):
        key, value = args
        store[key] = value


class GetCommand(CommandStrategy):
    def execute(self, store: dict, *args):
        key = args[0]
        print(store[key])


class DeleteCommand(CommandStrategy):
    def execute(self, store: dict, *args):
        key = args[0]
        del store[key]


class UpdateCommand(CommandStrategy):
    def execute(self, store: dict, *args):
        key, value = args
        store[key] = value


class CommandContext:
    def __init__(self):
        self.store = {}
        self.commands = {
            "ADD": AddCommand(),
            "GET": GetCommand(),
            "DELETE": DeleteCommand(),
            "UPDATE": UpdateCommand()
        }

    def execute_command(self, command: str, *args):
        self.commands[command].execute(self.store, *args)

    def get_store(self):
        return self.store


def in_memory_store_with_strategy(data: list) -> dict:
    context = CommandContext() # If you're low on time, don't need to do Context layer.
    for command in data:
        action, *args = command.split()
        context.execute_command(action, *args)
    return context.get_store()


print(in_memory_store_with_strategy(["ADD dog sophie", "ADD cat leon", "GET dog", "GET cat", "DELETE dog", "UPDATE cat leonardo"]))