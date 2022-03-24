from functions  import lottery_draw
def test_max_value():
    max_value = max(lottery_draw())
    assert max_value < 50

def test_min_value():
    min_value = min(lottery_draw())
    assert min_value > 0

def test_size_of_draw():
    size = len(lottery_draw())
    assert size == 6