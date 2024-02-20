"""
Dependency Injection: pass in all dependencies to a function as arguments
"""

# DON'T DO THIS
def how_long_is_hello_world() -> int:
    hello_world = "Hello, World!"
    def count_letters() -> int:
        return len(hello_world)
    return count_letters()


# DO THIS INSTEAD
def count_letters(word: str) -> int:
    return len(word)

def how_long_is_hello_world() -> int:
    hello_world = "Hello, World!"
    return count_letters(hello_world)

"""
Sometimes, it's wayy easier to have nested functions (i.e. depth-first search).
Implement it that way first, then see if you can refactor it to be more maintainable.
"""