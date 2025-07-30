 from main import add

 def test_add_positive():
    assert add(3, 5) == 8


 def test_add_negative():
    assert add(-3, -3) == -5
