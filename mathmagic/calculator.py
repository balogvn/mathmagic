def add(a, b):
    """
    Add two numbers together!
    
    It's like counting on your fingers!
    
    Args:
        a (number): First number
        b (number): Second number
    
    Returns:
        number: The sum of a and b
    
    Examples:
        >>> add(5, 3)
        8
        >>> add(10, 25)
        35
    """
    return a + b


def subtract(a, b):
    """
    Subtract one number from another!
    
    Like taking away cookies!
    
    Args:
        a (number): Number to subtract from
        b (number): Number to subtract
    
    Returns:
        number: The difference
    
    Examples:
        >>> subtract(10, 3)
        7
        >>> subtract(50, 20)
        30
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers!
    
    Like repeated addition!
    
    Args:
        a (number): First number
        b (number): Second number
    
    Returns:
        number: The product
    
    Examples:
        >>> multiply(5, 3)
        15
        >>> multiply(7, 8)
        56
    """
    return a * b


def divide(a, b):
    """
    Divide one number by another!
    
    Like sharing cookies equally!
    
    Args:
        a (number): Number to divide
        b (number): Number to divide by
    
    Returns:
        float: The result
    
    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(15, 3)
        5.0
    """
    if b == 0:
        raise ValueError("Oops! Can't divide by zero! That's like trying to share cookies with nobody!")
    return a / b


def average(numbers):
    """
    Find the average of a list of numbers!
    
    Like finding the middle score!
    
    Args:
        numbers (list): A list of numbers
    
    Returns:
        float: The average
    
    Examples:
        >>> average([10, 20, 30])
        20.0
        >>> average([5, 10, 15, 20])
        12.5
    """
    if len(numbers) == 0:
        raise ValueError("Oops! Can't average an empty list!")
    return sum(numbers) / len(numbers)


def power(a, b):
    """
    Raise a number to a power!
    
    Like multiplying a number by itself!
    
    Args:
        a (number): Base number
        b (number): Power/exponent
    
    Returns:
        number: a raised to the power of b
    
    Examples:
        >>> power(2, 3)
        8
        >>> power(5, 2)
        25
    """
    return a ** b 

    