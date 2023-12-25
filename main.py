import sys
import os
import json
from Notes import Notes
from datetime import datetime as dt


data = {'note':[]}
safe = True


#Парсер аргументов при запуске из командной строки
   #Возможные команды:
   # -s               - Ставится первым аргументом, отменяет завершение программы после выполнения
   #                    других команд завершающих работу приложения после выполнения 

   # -a "header" ["text"] - создание новой заметки(после создания приложение закрывается)

   # -d               - Удаление последней заметки(Предварительно выводит все данные о
   #                    заметке на экран и просит подтверждение после чего закрывается) 

   # -e               - Редактирование последней заметки(Выводит все данные о
   #                    заметке на экран и предлагает на выбор изменение заголовка или текста, 
   #                    после изменения выводит измененный вариант и снова предлагает изменение 
   #                    или выход после чего закрывается) 
   # -r               - Чтение последней заметки(Переход в главный цикл)
def work_with_argv(argv:list,bias:int):
    if argv[1 + bias] == '-a':
        data['note'].append(Notes(title=argv[2 + bias],
                                text=argv[3 + bias]))
        return data
    elif argv[1 + bias] == '-d':
        data['note'][len(data['note']) - 1 ].Print_Note()
        ans = input('Remove this note?[y/any]: ')
        if ans == 'y':
            data['note'].pop()
        return data
    elif argv[1 + bias] == '-e':
        Notes.Editing(data['note'][len(data['note']) - 1])
        return data
    elif argv[1 + bias] == '-r':
        data['note'][len(data['note']) - 1 ].Print_Note()
        return data

def Parse_argv(argv:list):
      if argv[1] == "-s":
         return work_with_argv(argv,1)
      else:
         return work_with_argv(argv,0)
  
def Remove(index:int):
    for note in data['note']:
        if int(index) == note.id:
            remove_index = data['note'].index(note)
            list.pop(data['note'],remove_index)

def Print_Notes():
    os.system('cls||clear')
    for note in data["note"]:
        note.Print_Note()

def Load_file():
        notes = {'note':[]}
        fileBuffer = None
        with open('data.json') as file:
            fileBuffer = json.load(file)

        for note in fileBuffer['note']:
            try:
                buf:Notes = Notes(int(note['id']),note['title'],
                            note['text'],note['date'])
                notes['note'].append(buf)
            except AttributeError:
                    print("Invalid structure!")

        return dict(notes)

def Safe_file():
        res = {'note': []}
        for note in data['note']:
            res['note'].append(to_json(note)) 
        with open('data.json', "w") as file:
            json.dump(res,file,indent=4)
         
# Перевод в json-строку для сохранения
def to_json(note):
    if isinstance(note,Notes):
        return{
            'id': note.id,
            'title': note.title,
            'text': note.text,
            'date': note.date,
            }

# При отсутсвии файла создает его
file = open('data.json')
file.close()

if os.stat('data.json').st_size != 0:
    data = Load_file()
    data['note'].sort(key=lambda note: dt.strptime(note.date,'%x %H:%M'))

if len(sys.argv) > 1:
    print("!!!!!!!!!!!!!")
    print(sys.argv)
    data = Parse_argv(sys.argv)
    # data['note'].sort(key=lambda note: dt.strptime(note.date,'%x %H:%M'))
    Safe_file()
    if sys.argv[1] != '-s' and sys.argv[1] != '-r':
        sys.exit()

# Основной цикл программы
while True:
    com = input(
                '1.Add notes\n'+\
                '2.Edit notes\n'+\
                '3.Remove notes\n'+\
                '4.Safe changes\n'+\
                '5.All notes\n'+\
                '6.Choice of a number of the note\n'+\
                '0.Exit\n'+\
                'Enter command: ')
    match int(com):
        case 1:
            os.system('cls||clear')
            data['note'].append(Notes())
            safe = False
        case 2:
            # os.system('cls||clear')
            Print_Notes()
            index = input("Enter id editing note: ")
            for note in data['note']:
                if note.id == int(index):
                    Notes.Editing(note)
                    safe = False
                    break
        case 3: 
            os.system('cls||clear')
            Print_Notes()
            index = input("Enter id remove note: ")
            for note in data['note']:
                if note.id == int(index):
                    Remove(index)
                    safe = False
                    break
        case 4:
            os.system('cls||clear')
            Safe_file()
            safe = True
            print('Save!\n\n')
        case 5:
            os.system('cls||clear')
            data['note'].sort(key=lambda note: dt.strptime(note.date,'%x %H:%M'))
            Print_Notes() 
        case 6:
            os.system('cls||clear')
            index = input("Enter id note: ")
            for note in data['note']:
                if note.id == int(index):
                    Notes.Print_Note(note)
                    break
        case 0:
            if safe:
                os.system('cls||clear')
                sys.exit()
            else:
                os.system('cls||clear')
                ans = input("Safe changes?[y/any]:")
                if ans == 'y':
                    Safe_file(data)
                    sys.exit()
                else: sys.exit()
        case _:
            print('Incorrect input!')



        

    



    

    












