import numpy as np
import pandas as pd
from random import randint

data = pd.read_csv('dataFile.csv',sep=',')
df_col = data.shape[1]      #stores # of columns

def allQuestions():
    menuFunc(0,df_col-1)

def impact():
    menuFunc(0, 5)

def chooseCol():
    initCount = 0
    for each in data.columns.values:
        print ("["+str(initCount)+"] "+each)
        initCount = initCount+1
    ans2 = raw_input("Enter selection #: ")

    menuAQ = {"1":("Randomize"),"2":("Back to menu")}

    while True:
        aq_col = int(ans2)                            #randomize column index from 0 to (# of cols) - 1
        aq_row = randint(0,int(data[[aq_col]].count()-1))       #length of column

        print("["+data.columns.values[int(ans2)]+"]")
        print("Question: "+str(data.iloc[aq_row,aq_col]))
        print("("+str(aq_row)+","+str(aq_col)+")")
        for key in sorted(menuAQ.keys()):
            print key + " : " + menuAQ[key]
        ans = raw_input("Selection: ")
        if ans == "1":
            continue
        elif ans == "2":
            break
        else:
            invalid()




def chooseQ():
    ans1 = raw_input("Enter location: ")
    my_list = ans1.split(",")
    print("Question: " + str(data.iloc[int(my_list[0]),int(my_list[1])]))

def quit():
    raise SystemExit

def invalid():
    print("Invalid")

def menuFunc(a,b):
    menuAQ = {"1":("Randomize"),"2":("Back to menu")}

    while True:
        aq_col = randint(a,b)                            #randomize column index from 0 to (# of cols) - 1
        aq_row = randint(0,int(data[[aq_col]].count()-1))       #length of column

        print("Question: "+str(data.iloc[aq_row,aq_col]))
        print("("+str(aq_row)+","+str(aq_col)+")")
        for key in sorted(menuAQ.keys()):
            print key + " : " + menuAQ[key]
        ans = raw_input("Selection: ")
        if ans == "1":
            continue
        elif ans == "2":
            break
        else:
            invalid()


menu = {"1":("All Questions",allQuestions),
        "2":("IMPACT Only",impact),
        "3":("Choose Column",chooseCol),
        "4":("Choose Question",chooseQ),
        "5":("Quit",quit)
       }

while True:
    print("---------------")
    for key in sorted(menu.keys()):
        print key + " : " + menu[key][0]

    ans = raw_input("Selection: ")
    menu.get(ans,[None,invalid])[1]()
