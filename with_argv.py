import Notes

class With_argv():
   #Парсер аргументов при запуске из командной строки
   #Возможные команды:
   # -s               - Ставится первым аргументом, отменяет завершение программы после выполнения
   #                    других команд завершающих работу приложения после выполнения 

   # -a header [text] - создание новой заметки(после создания приложение закрывается)

   # -d               - Удаление последней заметки(Предварительно выводит все данные о
   #                    заметке на экран и просит подтверждение после чего закрывается) 

   # -e               - Редактирование последней заметки(Выводит все данные о
   #                    заметке на экран и предлагает на выбор изменение заголовка или текста, 
   #                    после изменения выводит измененный вариант и снова предлагает изменение 
   #                    или выход после чего закрывается) 
   # -r               - Чтение последней заметки(Переход в главный цикл)
   
    def Parse_argv(argv:list):
        for str in argv:
           pass

