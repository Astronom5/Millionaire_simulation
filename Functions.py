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


def counter (counter_value = 0):
    counter_value = counter_value + 1
    return counter_value


def lottery_draw():
    lottery_numbers = set()
    while len(lottery_numbers)<6:
        lottery_numbers.add(randint(1,49))
    return lottery_numbers