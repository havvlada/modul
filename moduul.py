from os.path import split

import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt

def Load(): #завантажує
    try:
        df = pd.read_csv('proga.csv')
        print(df)
        return df
    except Exception as e:
        print(e)

def Add(df,name,number,data,price,status):#додає
    new_item = {"Name":name,"Number":number,"Data":data,"Price":price,"Status":status}
    new_row = pd.DataFrame(new_item)
    df.append(new_row)
    print("add done")
    return df
def Save(df,file_name):
    df.to_csv(file_name)
    print("save done")

def Count_all(df):
    count = df.groupby(['Count']).sum()
    return count

def Price_all(df):
    price = df.groupby(['Price']).sum()
    return price

def Analiz_status(df):
    stus_df = df.groupby(['Status'])
    return stus_df
def Search(df):
    max_price = df.groupby(['Price']).max()
    return max_price


def Delete(df, number):#видаляє
    df = df.drop(number)
    return df

def plot_count_data(df):
    if df.empty:
        print("Дані відсутні.")
        return
    plt.hist(df["Number"], bins=10, color='green', alpha=0.7)
    plt.title("count_data")
    plt.xlabel("number")
    plt.ylabel("Data")
    plt.grid(axis='y')
    plt.show()
def plot_price_data(df):
    if df.empty:
        print("")
        return
    plt.scatter(df["Number"], df["Price"])
    plt.title("price_data")
    plt.xlabel("number")
    plt.ylabel("price")
    plt.grid(axis='y')
    plt.show()
def plot_number_data(df):
    if df.empty:

        print("")
        return
    plt.pie(df["Number"])
    plt.title("number_data")
    plt.xlabel("number")
    plt.ylabel("data")
    plt.grid(axis='y')
    plt.show()
def Addd(df):
    txt=ent.get()
    texxt = txt.split(",")
    df=Add(df,texxt[1],texxt[2],texxt[3],texxt[4])
    return df
def Deletee(df):
    info =ent2.get()
    Delete(df,info)


df=Load()
root=tk.Tk()
root.title("window")
root.geometry("500x500")

lab1 = tk.Label(root,text="option")
lab1.pack()
but1 = tk.Button(root,text="Load",command=Load)
but1.pack()
lab2 = tk.Label(root,text="put info")
lab2.pack()
ent= tk.Entry(root)
ent.pack()
but2 = tk.Button(root,text="Add",command=Addd)
but2.pack()
but3 = tk.Button(root,text="Save",command=Save(df,"proga.csv"))
but3.pack()
but4 = tk.Button(root,text="Delete",command=Deletee)
ent2 = tk.Entry(root)
ent2.pack()
but4.pack()
but5 = tk.Button(root,text="pie",command=plot_number_data(df))
but5.pack()


root.mainloop()



