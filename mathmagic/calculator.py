def add(a, b):
    """Add two numbers together

    it's not magic, it's just a function that adds two numbers together

    Args:
        a: The first number to add
        b: The second number to add

    Returns:
        The sum of the two numbers
    
    Examples:
        >>> add(1, 2)
        3
        """
    return a + b
    
def subtract(a, b):
    """Subtract two numbers together

    it's not magic, it's just a function that subtracts two numbers together

    Args:
        a: The first number to subtract
        b: The second number to subtract

    Returns:
        The difference of the two numbers
    
    Examples:
        >>> subtract(1, 2)
        -1
        """
    return a - b
    
def multiply(a, b):
    """Multiply two numbers together

    it's not magic, it's just a function that multiplies two numbers together

    Args:
        a: The first number to multiply
        b: The second number to multiply

    Returns:
        The product of the two numbers
    
    Examples:
        >>> multiply(1, 2)
        2
        """
    return a * b
    
def divide(a, b):
    """Divide two numbers together

    it's not magic, it's just a function that divides two numbers together

    Args:
        a: The first number to divide
        b: The second number to divide

    Returns:
        float: The quotient of the two numbers/ result of the division
    
    Examples:
        >>> divide(1, 2)
        0.5
        """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def average(numbers):
    """Calculate the average of a list of numbers

    it's not magic, it's just a function that calculates the average of a list of numbers

    Args:
        numbers: A list of numbers to calculate the average of

    Returns:
        float: The average of the numbers
    
    Examples:
        >>> average([1, 2, 3, 4, 5])
        3.0
    """
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    return sum(numbers) / len(numbers)

def power(a, b):
        """Raise a number to the power of another number

        it's not magic, it's just a function that raises a number to the power of another number

        Args:
            a: The number to raise
            b: The power to raise the number to

        Returns:
          number: a raised to the power of b
        
        examples:
            >>> power(2, 3)
            8
            """
    return a ** b
        
        