"""Module for testing functions from millionaire simulation"""
import functions
TEST_SET = {1,2,3,4,5,6}

def test_max_value():
    max_value = max(functions.lottery_draw())
    assert max_value < 50

def test_min_value():
    min_value = min(functions.lottery_draw())
    assert min_value > 0

def test_size_of_draw():
    size = len(functions.lottery_draw())
    assert size == 6

#Tests for check output from win_classification()

def test_win_classification_0():
    classification_type = functions.win_classification(TEST_SET,{7,8,9,10,11,12})
    assert classification_type == 0

def test_win_classification_1():
    classification_type = functions.win_classification(TEST_SET,{6,7,8,9,10,11})
    assert classification_type == 0

def test_win_classification_2():
    classification_type = functions.win_classification(TEST_SET,{5,6,7,8,9,10})
    assert classification_type == 0

def test_win_classification_3():
    classification_type = functions.win_classification(TEST_SET,{4,5,6,7,8,9})
    assert classification_type == 3

def test_win_classification_4():
    classification_type = functions.win_classification(TEST_SET,{3,4,5,6,7,8})
    assert classification_type == 4

def test_win_classification_5():
    classification_type = functions.win_classification(TEST_SET,{2,3,4,5,6,7})
    assert classification_type == 5

def test_cost():
    tested_cost= functions.cost_func(5)
    assert tested_cost == 15

def test_income():
    tested_income= functions.income_func(1,1,1,1)
    assert tested_income == 2005524

#Tests for check output from classification_counter_func()

def test_classification_0():
    test_value = functions.classification_counter_func(0,0,0,0)
    assert test_value == [0,0,0,1]

def test_classification_3():
    test_value = functions.classification_counter_func(0,0,0,3)
    assert test_value == [1,0,0,1]

def test_classification_4():
    test_value = functions.classification_counter_func(0,0,0,4)
    assert test_value == [0,1,0,1]

def test_classification_5():
    test_value = functions.classification_counter_func(0,0,0,5)
    assert test_value == [0,0,1,1]

def test_classification_type():
    test_type_value = type(functions.classification_counter_func(0,0,0,0))
    assert test_type_value == list
