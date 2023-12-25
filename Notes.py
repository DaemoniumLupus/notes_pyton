from datetime import datetime as dt
import json
import os

class Notes():
    TOTAL_OBJECT:int = 0

    title: str = ''
    text: str = ''
    date: str = ''
    id: int

    def __init__(self, id:int = 0, 
                 title:str = '', 
                 text:str = '', 
                 date_in:str = ''):
        Notes.TOTAL_OBJECT = Notes.TOTAL_OBJECT + 1

        if id == 0:
            self.id = Notes.TOTAL_OBJECT
        else:
            self.id = id

        if date_in == '':
            self.date = dt.today().strftime('%x %H:%M')    
        else:
            self.date = date_in

        if title == '':
            self.title = input("Enter heading: ")
        else:
            self.title = title
        
        if text == '':
            self.text = input("Enter text(one string): ")
        else:
            self.text = text
 

    def Print_Note(self):
        print('*' * 70)
        print(f'Number notes: {self.id}\n' +\
                    f'Create date: {self.date}\n' +\
                    f'Title: {self.title}\n' +\
                    f'Text:\n{self.text}')
        print('*' * 70)

    def Editing(self):
        ans:int = 0

        while ans != 3:
            os.system('cls||clear')
            self.Print_Note()
            ans = int(input(f"Select what you want to change: \n" +\
                    '1. Title \n' +\
                    '2. Text \n'\
                    '3. Exit \n'\
                    'Enter: '))
            if ans == 3:
                self.date = dt.today().strftime('%x %H:%M')
                break
            elif ans == 1:
                os.system('cls||clear')
                self.Print_Note()
                self.title = input("Enter new title: ")
            elif ans == 2:
                os.system('cls||clear')
                self.Print_Note()
                self.text = input("Enter new text(one string): ")
            else: 
                os.system('cls||clear')
                #через заглушку
                i = input('Incorrect input\n')

    
    
    
    
