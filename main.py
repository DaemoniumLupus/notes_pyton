import sys
import os
import json
from with_argv import With_argv
from Notes import Notes

data = []
safe = True

def Print_Notes(notes:list):
    os.system('cls||clear')
    for note in notes:
        note.Print_Note()

def Load_file():
        notes:list
        fileBuffer = None
        with open('data.json') as file:
            fileData = file.read()
            fileBuffer = json.loads(fileData)

        # for notes in fileBuffer:
        notes = fileBuffer
        try:
            buf = Notes(int(notes['id']),notes['title'],
                        notes['text'],notes['date'])
            notes.append(buf)
        except AttributeError:
                print("Invalid structure!")
        return list(notes)

def Safe_file(data:list):
        res = ''
        for note in data:
            res += to_json(note) 
        with open('data.json', "w") as file:
            file.write(res)
         

def to_json(o):
    if isinstance(o,Notes):
        return json.dumps({
            "id": o.id,
            "title": o.title,
            "text": o.text,
            "date": o.date,
            },indent=4)


file = open('data.json')
file.close()

if os.stat('data.json').st_size != 0:
    data = Load_file()


while True:
    com = input(f"\
1.Add notes\n\
2.Edit notes\n\
3.Remove notes\n\
4.Safe changes\n\
5.All notes\n\
6.Exit\n\
Enter command: ")
    match int(com):
        case 1:
            os.system('cls||clear')
            data.append(Notes())
            safe = False
        case 2:
            Print_Notes(data)
            index = input("Enter id editing note: ")
            for note in data:
                if note.id == index:
                    Notes.Editing(note)
                    safe = False
                    break
        case 3: 
            Print_Notes(data)
            index = input("Enter id remove note: ")
            for note in data:
                if note.id == index:
                    Notes.Remove(note)
                    safe = False
                    break
        case 4:
            Safe_file(data)
            safe = True
        case 5:
            Print_Notes(data)  
        case 6:
            if safe:
                sys.exit()
            else:
                ans = input("Safe changes?[y/any]:")
                if ans == 'y':
                    Safe_file(data)
                    sys.exit()
                else: sys.exit()
        case _:
            print('Incorrect input!')



        

    


# if len(sys.argv) > 1:
#     With_argv.Parse_argv(sys.argv)
    

    












