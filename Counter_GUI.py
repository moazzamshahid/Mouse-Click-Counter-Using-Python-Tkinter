from tkinter import *
import pandas as pd
import datetime
import time


window = Tk()
window.title("Mouse Click Counter")
window.geometry('210x100')
window.configure(background = "grey")
a = Label(window ,text = "Today's Total Click", width=18)
a.grid(row = 0,column = 0,pady=2, padx=2)
b = Label(window ,text = "Last One Hour Click", width=18)
b.grid(row = 1,column = 0, pady=2, padx=2)

a1 = Entry(window, width=11)
a1.grid(row = 0,column = 1, pady=2)
b1 = Entry(window,width=11)
b1.grid(row = 1,column = 1, pady=2)


def clicked():
    df=pd.read_csv("log.csv")
    df["date"]=pd.to_datetime(df["date"])
    df["date_check"] =datetime.datetime.today()- df["date"]
    today=df.loc[df["date_check"]<=pd.Timedelta(1,'d')].count()
    a1.delete(0,END)
    a1.insert(0,today["date"])
   
    df["Time"]=pd.to_datetime(df["Time"])
    df["time_check"]= datetime.datetime.now()-df["Time"]
    today=df.loc[(df["date"]==datetime.datetime.today().strftime("%Y-%m-%d")) &(df["time_check"]<=pd.Timedelta(1,'h'))].count()
    b1.delete(0,END)
    b1.insert(0,today["date"])
    window.after(2000, clicked)

def clear():
    data= {"date":"",
                "Time":"", 
                "click_Status":""
            }
    df=pd.DataFrame(data,index=[0])
    df.to_csv('log.csv', index=False, header=True)   

button= Button(window, text="Clear all Data",width=10, pady=3,borderwidth=1,border=2, command= lambda: clear())
button.grid(row=4,column=0,pady=2)


    
    

clicked()
window.mainloop()