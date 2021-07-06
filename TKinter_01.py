from tkinter import *

from flipkart_sectionB import populateDB
from flipkart_page import addEntry
from bs4 import BeautifulSoup
import scraper_functions
import pandas as pd
import requests
import time
import csv
import os


root=Tk()
root.title('Flipkart product tracker')

#functions

def btn1():
    url = entry1.get()
    addEntry(url)
    entry1.delete(0,len(url))
    
def btn2():
    url = entry2.get()
    populateDB(url)
    entry2.delete(0,len(url))

def btn3(srch):
    url = 'https://flipkart.com/search?q='
    string = entry3.get()
    tagList = string.split()
    for tag in tagList:
        url += tag
        url += '+'
    url = url[:-1]
    url += srch
    populateDB(url)
    print(url)
    entry3.delete(0,len(url))
    
def btn4(val):
    df = pd.read_csv('database.csv', index_col=0)
    df = df.drop(index=int(val))
    df = df.reset_index(drop=True)
    df.to_csv("database.csv")
    entry4.delete(0,len(str(val)))
    
def btn5():
    new_window=Tk()
    new_window.title('Database')

    scroll = Scrollbar(new_window, orient=VERTICAL)
    scroll.pack()

    var = []
    state = []
    i = 0
    with open('database.csv', 'r') as in_file:
    	csv_reader = csv.reader(in_file)
    	next(csv_reader)
    	for line in csv_reader:
    		var.append(IntVar)
    		c = Checkbutton(new_window, text=line[1], variable=var[i])
    		c.pack()
    		state.append(var[i])
    		i=i+1
    btn = Button(new_window, text="remove them! ahaha", command=lambda: delbtn(state))
    btn.pack()

def delbtn(l):
	j = 0
	for i in l:
		if i:
			btn4(j)
		j+=1



#single page funtionality start
label1 = Label(root, text="Enter product page url")
entry1 = Entry(root)
button1 = Button(root, text="Add entry", command=btn1)

label1.grid(row=0, column=0)
entry1.grid(row=1, column=0)
button1.grid(row=2, column=0)

#section functionality start
midlabel1 = Label(root, pady=10).grid(row=3,column=0)

label2 = Label(root, text="Enter section page url")
entry2 = Entry(root)
button2 = Button(root, text="Add entries", command=btn2)

label2.grid(row=10, column=0)
entry2.grid(row=11, column=0)
button2.grid(row=12, column=0)

#search & get functionality start
midlabel2 = Label(root, padx=20).grid(row=0,column=1)

label3 = Label(root, text="Search for product")
entry3 = Entry(root)
button3 = Button(root, text="Add entries", command=lambda: btn3(r.get()))

r = StringVar(value='&sort=popularity')
radiobtn3_1 = Radiobutton(root, text="Sort by popularity", variable=r, value='&sort=popularity')
radiobtn3_2 = Radiobutton(root, text="Sort by price-Low to High", variable=r, value='&sort=price_asc')
radiobtn3_3 = Radiobutton(root, text="Sort by price-High to Low", variable=r, value='&sort=price_desc')
radiobtn3_4 = Radiobutton(root, text="Sort by Newest first", variable=r, value='&sort=recency_desc')

label3.grid(row=0, column=2)
entry3.grid(row=1, column=2)
button3.grid(row=2, column=2)
radiobtn3_1.grid(row=0, column=3) 
radiobtn3_2.grid(row=1, column=3)
radiobtn3_3.grid(row=2, column=3)
radiobtn3_4.grid(row=3, column=3)

#delete row functionality start

label4 = Label(root, text="Entry number to be deleted")
entry4 = Entry(root)
button4 = Button(root, text="Delete entry", command=lambda: btn4(entry4.get()))

label4.grid(row=10, column=2)
entry4.grid(row=11, column=2)
button4.grid(row=12, column=2)

#diplay DB
midlabel3 = Label(root, padx=20).grid(row=13,column=0)
label5 = Label(root, bd=6, text="Press to get DB")
button5 = Button(root, text="lol ok", command=btn5)

label5.grid(row=18, column=0)
button5.grid(row=19, column=0)



root.mainloop()