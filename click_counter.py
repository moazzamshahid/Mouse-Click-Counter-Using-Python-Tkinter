import mouse
import keyboard
import pandas as pd
import datetime
import time

def on_click(pressed):
    if pressed:

        data= {"date": datetime.datetime.today().strftime("%Y-%m-%d"),
                "Time": datetime.datetime.now().strftime("%H:%M:%S"), 
                "click_Status":"Mouse Clicked"
                }
        df=pd.DataFrame(data,index=[0])
        df.to_csv('log.csv', mode='a', index=False, header=False)
    

    while mouse.is_pressed():
       continue



def check_format(inputDate):
    year, month, day = inputDate.split('-')

    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False

    if(isValidDate):
        print("Input date is valid ..")
        return False
    else:
        print("Input date is not valid..")
        return True
# Collect events until released

if(datetime.datetime.now().weekday()==5):
    df=pd.read_csv("log.csv")
    df["date"]=pd.to_datetime(df["date"])
    df["age"]=  datetime.datetime.today()-df["date"]
    #print(df["age"])
    df=df.loc[df["age"]<=datetime.timedelta(days=7)]
    df.to_csv('log.csv', index=False, header=True)

while True:
    if(mouse.is_pressed()):
        on_click(True)
    time.sleep(0.01)

        
       

           

