"""
Those are the functions used in Millionaire simulation.
You can write your own functions here and import tham to main program.
All of the functions have their own description below.
"""

from random import randint

def add_data():
    """This function collects data from user about numbers tipped by him.
    It is forcing user to type numbers between 1 to 49.

    Returns:
        set: Numbers tipped by the user (it should be 6 of them)
    """
    data = []
    for counter in range(6):
        collected_data=int(input(f"Podaj {counter+1} liczbę do losowania: "))
        if collected_data not in range (1,50) or collected_data in data:
            while collected_data not in range (1,50) or collected_data in data:
                collected_data=int(input(f"Podaj {counter+1} liczbę do losowania: "))
        data.append(collected_data)
    return set(data)


def lottery_draw():
    """This function simulates one lottery draw of numbers.
       It picks 6 numbers from 1 to 49 randomly.

    Returns:
        set: Numbers randomly selected for lottery simulation.
    """
    lottery_numbers = set()
    while len(lottery_numbers)<6:
        lottery_numbers.add(randint(1,49))
    return lottery_numbers


def win_classification( tipped_numbers, lottery_numbers):
    """This function returns type of win in lottery draw. It counts correctly tipped numbers.
       If it is bigger than the treshold it returns number of them.

    Args:
        tipped_numbers (set): 6 numbers from 1 to 49 selected by the user
        lottery_numbers (set): 6 numbers from 1 to 49 randomly selected by the computer

    Returns:
        int: Amount of correctly tipped numbers above the treshold or 0 as no win information
    """
    win_type = len(tipped_numbers.intersection(lottery_numbers))
    if win_type>2:
        return win_type
    return 0


def cost_func(number_of_draws):
    """Generates cost of all lottery draws, we assume that one draw costs 3 zł.

    Args:
        number_of_draws (int): Amount of draws needed to win

    Returns:
        int: Cost of all draws
    """
    cost=number_of_draws*3
    return cost


def income_func(win_type_3 = 0, win_type_4 = 0 ,win_type_5 = 0, win_type_6 = 1):
    """Function returns amount of money that we won during all lotteries
       (including the one that we won)

    Args:
        win_type_3 (int): Amount of correctly tipped 3 numbers. Defaults to 0.
        win_type_4 (int): Amount of correctly tipped 4 numbers. Defaults to 0.
        win_type_5 (int): Amount of correctly tipped 5 numbers. Defaults to 0.
        win_type_6 (int): Amount of correctly tipped all numbers. Defaults to 1.

    Returns:
        int: Sum of all rewards during all draws
    """
    income = win_type_3*24 + win_type_4*500 + win_type_5*5000 + win_type_6*2000000
    return income



def classification_counter_func(win_type_3, win_type_4,win_type_5, win_type_add):
    """_summary_

    Args:
        win_type_3 (int): Amount of correctly tipped 3 numbers till now.
        win_type_4 (int): Amount of correctly tipped 4 numbers till now.
        win_type_5 (int): Amount of correctly tipped 5 numbers till now.
        win_type_add (int): Type of win that we ant to classify to existing ones.

    Returns:
        list: list of every win sorted by type in ascending order
    """
    classification_counter =[win_type_3, win_type_4,win_type_5,1]
    if win_type_add == 0:
        return classification_counter
    if win_type_add == 3:
        classification_counter[0] = classification_counter[0]+1
        return classification_counter
    if win_type_add == 4:
        classification_counter[1] = classification_counter[1]+1
        return classification_counter
    classification_counter[2] = classification_counter[2]+1
    return classification_counter
