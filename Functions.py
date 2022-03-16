def add_data():
    data = []
    for counter in range(6):
        collected_data=int(input(f"Podaj {counter+1} liczbę do losowania"))
        data.append(collected_data)
    return set(data)


my_data=add_data()
print('Skończyłem')