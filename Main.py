from Functions import add_data,lottery_draw,win_classification,classification_counter_func 

my_data=add_data()
print(my_data)
counter_variable = 0 # initializes number of draws to main prize
#win_type=[0,0,0,1] ### makes a list of win type from 3 to 6, so initial values will be 0001 for this simulation
lottery_data = lottery_draw()
win_type_3 = 0
win_type_4 = 0
win_type_5 = 0 
win_type_6 = 1

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
    

print(f"Twoje liczby: {my_data} \nWylosowane liczby: {lottery_data} \nIlość prób: {counter_variable} \nTypy wygranych:\n3: {win_type_3}\n4: {win_type_4}\n5: {win_type_5}")