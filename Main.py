from Functions import add_data,lottery_draw,win_classification,classification_counter_func 
from random import randint

my_data=add_data()
print(my_data)
counter_variable = 0 # initializes number of draws to main prize
win_type=[0,0,0,1] ### makes a list of win type from 3 to 6, so initial values will be 0001 for this simulation
lottery_data = lottery_draw()
counter_variable = 1
win_capture = win_classification(my_data,lottery_data)
win_type= classification_counter_func(win_type,win_capture)

while my_data != lottery_data:
    lottery_data = lottery_draw()
    counter_variable +=1
    win_capture = win_classification(my_data,lottery_data)
    win_type= classification_counter_func(win_type,win_capture)

print(f"Twoje liczby: {my_data} \nWylosowane liczby:{lottery_data} \nIlość prób: {counter_variable} \nTypy wygranych: {win_type}")