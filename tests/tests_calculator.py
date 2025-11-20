"""Tests our amazing calculator package!

This makes sure our calculator package is working as expected."""

from mathmagic import calculator

def test_add():
    """Test the add function"""
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-1, -1) == -2
    
    print("addition tests passed!")


def test_subtract():
    """Test the subtract function"""
    assert calculator.subtract(1, 2) == -1
    assert calculator.subtract(-1, 1) == -2
    assert calculator.subtract(-1, -1) == 0
    
    print("subtraction tests passed!")
    
def test_multiply():
    """Test the multiply function"""
    assert calculator.multiply(1, 2) == 2
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(-1, -1) == 1
    print("multiplication tests passed!")

def test_divide():
    """Test the divide function"""
    assert calculator.divide(1, 2) == 0.5
    assert calculator.divide(-1, 1) == -1
    assert calculator.divide(-1, -1) == 1
    print("division tests passed!")

def test_average():
    """Test the average function"""
    assert calculator.average([1, 2, 3, 4, 5]) == 3.0
    assert calculator.average([1, 2, 3, 4, 5]) == 3.0 
    print("average tests passed!")

def test_power():
    """Test the power function"""
    assert calculator.power(2, 3) == 8
    assert calculator.power(-1, 1) == -1
    assert calculator.power(-1, -1) == 1
    print("power tests passed!")


def run_all_tests():
    """Run all tests"""
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_average()
    test_power()
    print("all tests passed!")

if __name__ == "__main__":
    run_all_tests()