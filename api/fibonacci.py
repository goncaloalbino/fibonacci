from typing import Dict, List, Tuple, Iterator, Union

import paginate

BLACKLIST = set()


def fibonacci() -> Iterator[int]:
    """
    Generates an iterator with the fibonacci sequence values
    :return: Iterator with fibonacci value
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_sequence(number: int) -> Dict[int, int]:
    """
    Creates a fibonacci sequence with number, value information, for a requested number.
    :param number: Fibonacci number requested
    :return: `number: value` dict with the fibonacci sequence generated
    """
    fib = fibonacci()
    sequence = {number: next(fib) for number in range(1, number + 1)}
    return sequence


def fibonacci_value(number: int) -> Tuple[Dict[str, Union[str, int]], int]:
    """
    Get the value of a requested number from the fibonacci sequence
    :param number: Fibonacci number
    :return: Fibonacci value and status code. Status message if number is blacklisted
    """
    if number in BLACKLIST:
        return {"value": f"Number {number} is blacklisted"}, 404
    return {"value": fibonacci_sequence(number)[number]}, 200


def fibonacci_values(page: int, items_per_page: int) -> Tuple[Dict[str, List[Tuple]], int]:
    """
    Gets all the fibonacci numbers and corresponding values from the fibonacci sequence
    for the page requested. If any of the numbers are on the BLACKLIST those are removed
    from the resulting list.
    :param page: Page requested
    :param items_per_page: Items per page requested
    :return: List of tuples with fibonacci number, value
    """
    total_items = page * items_per_page
    sequence = fibonacci_sequence(total_items)
    values = [(number, value) for number, value in sequence.items() if number not in BLACKLIST]
    return {"values": paginate.Page(values, page=page, items_per_page=items_per_page).items}, 200


def blacklist_add(number: int) -> Tuple[Dict[str, str], int]:
    """
    Adds a number to the blacklist
    :param number: Number to be added to the blacklist
    :return: Dict with tatus message and status code
    """
    BLACKLIST.add(number)
    return {"value": f"Value {number} added to blacklist"}, 200


def blacklist_remove(number) -> Tuple[Dict[str, str], int]:
    """
    Removes a number from the blacklist
    :param number: Number to be removed from the blacklist
    :return: Dict with status message and status code
    """
    try:
        BLACKLIST.remove(number)
        return {"value": f"Value {number} removed from blacklist"}, 200
    except KeyError:
        return {"value": f"Value {number} is not blacklisted"}, 404
