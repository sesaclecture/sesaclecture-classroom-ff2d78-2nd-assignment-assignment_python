from basic import add, sub, mul, div, exp, square, greet


def test_addition():
    """Test addition function"""
    assert 5 == add(2, 3)
    assert 100 == add(100, 0)


def test_subtraction():
    """Test subtraction function"""
    assert 6 == sub(12, 6)
    assert 100 == sub(100, 0)


def test_multiplication():
    """Test multiplication function"""
    assert 6 == mul(2, 3)
    assert 0 == mul(100, 0)


def test_division():
    """Test division function"""
    assert 6.0 == div(12, 2)
    assert 0 == div(0, 100)


def test_exponential():
    """Test exponential function"""
    assert 10000 == exp(10, 4)
    assert 100 == exp(10, 2)
    assert 4 == exp(-2, 2)
    assert 1 == exp(1000, 0)


def test_square():
    """Test square function"""
    assert 9 == square(3)
    assert 100 == square(10)
    assert 4 == square(-2)


def test_greetings():
    """Test greet function"""
    assert "안녕하신가 낯선자!" == greet()
    assert "안녕하십니까 김철수!" == greet("김철수", 40)
    assert "안녕 낯선자!" == greet(나이=10)
