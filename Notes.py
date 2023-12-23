from datetime import datetime as dt
import json

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
            self.id = self.total_objects()
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

    def __repr__(self) -> str:
        return '<Note (id: {},date:{} title: {}, text: {})>'\
            .format(self.id,self.date,self.title,self.text)
    @classmethod
    def total_objects(cls):
        return cls.TOTAL_OBJECT
    
    def Print_Text(self):
        maxStr:int = 70
        count:int = 0
        for char in self.text:
            print(char)
            count += 1
            if count == maxStr:
                print('\n')

    def Print_Note(self):
        print('*' * 70)
        print(f'Number notes: {self.id}\n' +\
                    f'Create date: {self.date}\n' +\
                    f'Title: {self.title}\n' +\
                    f'Text:\n{self.Print_Text}')
        print('*' * 70)

    def Editing(self):
        ans:int = 0

        while ans != 3:
            self.Print_Notes()
            ans = int(input(f"Select what you want to change: \n\
                    1. Title \n\
                    2. Text \n\
                    3. Exit \n\
                    Enter: "))
            if ans == 3:
                dt.today().strftime('%x %H:%M')
                break
            elif ans == 1:
                self.title = input(f"Title now: {self.Print_Text}\n\
                                    Enter new title: ")
            elif ans == 2:
                self.text = input(f"Text now: {self.Print_Text}\n\
                                    Enter new text(one string): ")
            else: 
                print('Incorrect input\n')

    def Remove(self):
        pass

    def to_json(self):
        return json.dumps({
            
                "id": self.id,
                "title": self.title,
                "text": self.text,
                "date": self.date,
                })

    
    
