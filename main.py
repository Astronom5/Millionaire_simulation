"""This is our main program that allows us to perform simulation of one of gambling games.
First it is necessary to input 6 numbers from 1 to 49,
then it shows how long it will take to win in game,
and how old the player will be. It shows also the income (or the lose to be precise).

"""
from functions import add_data,lottery_draw,win_classification,cost_func, income_func


My_data=add_data()
COUNTER_VARIABLE = 0 # initializes number of draws to main prize
Lottery_data = set()
WIN_TYPE_3 = 0
WIN_TYPE_4 = 0
WIN_TYPE_5 = 0
WIN_TYPE_6 = 1
User_age = float(input("Podaj swój wiek: "))


while My_data != Lottery_data:
    Lottery_data = lottery_draw()
    COUNTER_VARIABLE +=1
    win_capture = win_classification(My_data,Lottery_data)
    if win_capture == 3:
        WIN_TYPE_3 +=1
    elif win_capture == 4:
        WIN_TYPE_4 +=1
    elif win_capture == 5:
        WIN_TYPE_5 +=1


MY_COST = cost_func(COUNTER_VARIABLE)
MY_INCOME = income_func(WIN_TYPE_3, WIN_TYPE_4, WIN_TYPE_5)
my_profit = MY_INCOME - MY_COST
print(f"Twoje liczby: {My_data} \nWylosowane liczby: {Lottery_data} \n\
Ilość prób: {COUNTER_VARIABLE}\n\
Typy wygranych:\n3: {WIN_TYPE_3}\n4: {WIN_TYPE_4}\n5: {WIN_TYPE_5}")
print (f"Twój wiek kiedy wygrasz: {User_age + COUNTER_VARIABLE//52} lat \
i {COUNTER_VARIABLE % 52} tygodni")
print (f"W tym czasie zarobiłeś {my_profit} zł")
