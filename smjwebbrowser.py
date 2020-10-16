#IMPORTING ALL NECESSARY MODULES
 
import youtube_dl

import urllib

import shutil

import tkinter

from tkinter import *

import webbrowser

from googlesearch import search

#CONFIGURING GUI

smj = Tk( )

'''
smj.geometry("630x150")
EDITABLE
'''

smj.title('SMJ BROWSER')

smj.configure(bg = 'black')

'''
SETTING THE FIRST LABEL
'''

Label1 = Label(smj , text = 'Enter Your Search Query: ' , fg ='blue' , bg = 'black' , font = ('times' , 21))

entry = Entry(smj , width = 99 , bg = 'white' , border = 7)

def u_sep( ):
	for j in search(entry.get( ) , tld = 'co.in' , num = 5 , pause = 2 , stop = 5):
		webbrowser.open(j)
		
sbutton = Button(smj , text = 'SEARCH' , fg = 'red' , bg = 'yellow' , font=('times' , 21) , command = u_sep)

#SETTING GRID
Label1.grid(row = 0 , column = 0)

entry.grid(row = 1 , column = 0)

sbutton.grid(row = 2 , column = 0)

smj.mainloop( )