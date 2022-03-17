from random import randint

def add_data():
    data = []
    for counter in range(6):
        collected_data=int(input(f"Podaj {counter+1} liczbę do losowania: "))
        if collected_data not in range (1,50) or collected_data in data:
            while collected_data not in range (1,50) or collected_data in data:
                collected_data=int(input(f"Podaj {counter+1} liczbę do losowania: "))
        data.append(collected_data)
    return set(data)


def lottery_draw():
    lottery_numbers = set()
    while len(lottery_numbers)<6:
        lottery_numbers.add(randint(1,49))
    return lottery_numbers


def win_classification( typed_numbers, lottery_numbers):
    win_type = len(typed_numbers.intersection(lottery_numbers))
    if win_type>2:
        return win_type
    else:
        return 0


def age_counter(number_of_draws):
    added_age = number_of_draws/52
    return added_age


def cost(number_of_draws):
    cost=number_of_draws*3
    return cost


def income_func(win_type_3 = 0, win_type_4 = 0 ,win_type_5 = 0, win_type_6 = 1):
    income = win_type_3*24 + win_type_4*500 + win_type_5*5000 + win_type_6*2000000
    return income



def classification_counter_func(win_type_3, win_type_4,win_type_5, win_type_add):
    classification_counter =[win_type_3, win_type_4,win_type_5,1]
    if win_type_add == 0:
        return classification_counter
    elif win_type_add == 3:
        classification_counter[0] = classification_counter[0]+1
        return classification_counter
    elif win_type_add == 4:
        classification_counter[1] = classification_counter[1]+1
        return classification_counter
    elif win_type_add == 5:
        classification_counter[2] = classification_counter[2]+1
        return classification_counter