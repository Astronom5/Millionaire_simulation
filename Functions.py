def add_data():
    data = []
    for counter in range(6):
        collected_data=int(input(f"Podaj {counter+1} liczbę do losowania: "))
        if collected_data not in range (1,50) or collected_data in data:
            while collected_data not in range (1,50) or collected_data in data:
                collected_data=int(input(f"Podaj {counter+1} liczbę do losowania: "))
        data.append(collected_data)
    return set(data)
