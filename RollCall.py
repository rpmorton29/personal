import pandas as pd


def readcsv():
    roll = pd.read_csv(r"rollCall.csv",index_col=0)
    return roll


def addcall(roll):
    call = raw_input("Enter The Call: ")
    people = raw_input("Enter those on the call(Seperate by ,): ")
    people =people.replace(" ", "")
    people =people.split(",")
    for name in people:
        if name not in roll.index:
            print(name +" is not on the roll sheet")
            people.remove(name)

    roll.loc[people,call]='1'
    jane =['2']

    roll.to_csv(r"rollCall.csv")

def deletecall(roll):
    print(roll.head())
    call = raw_input("Enter The Call: ")
    if call not in roll:
        print("Call not in roll")
    else:
        roll = roll.drop(str(call),axis=1)

roll = readcsv()
answer = raw_input("Would you like to add a call?Y/N")
if answer.lower() == 'y':
    addcall(roll)
answer2 = raw_input("Would you like to add a call?Y/N")
if answer2.lower() == 'y':
    deletecall(roll)