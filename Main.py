from cgi import print_arguments
from Functions import add_data,lottery_draw,win_classification,cost, income_func


my_data=add_data()
counter_variable = 0 # initializes number of draws to main prize
lottery_data = set()
win_type_3 = 0
win_type_4 = 0
win_type_5 = 0 
win_type_6 = 1
User_age = float(input("Podaj swój wiek: "))


while my_data != lottery_data:
    lottery_data = lottery_draw()
    counter_variable +=1
    win_capture = win_classification(my_data,lottery_data)
    if win_capture == 3:
        win_type_3 +=1
    elif win_capture == 4:
        win_type_4 +=1      
    elif win_capture == 5:
        win_type_5 +=1  


my_cost = cost(counter_variable)
my_income = income_func(win_type_3, win_type_4, win_type_5)
my_profit = my_income - my_cost
print(f"Twoje liczby: {my_data} \nWylosowane liczby: {lottery_data} \nIlość prób: {counter_variable} \nTypy wygranych:\n3: {win_type_3}\n4: {win_type_4}\n5: {win_type_5}")
print (f"Twój wiek kiedy wygrasz: {User_age + counter_variable/52}")
print (f"W tym czasie zarobiłeś {my_profit}")