import argparse
from cowsay import cowsay
from cowsay import list_cows

def main():
    parser = argparse.ArgumentParser(description = 'Cowsay parameters')

    #Задание необязательных аргументов командной строки
    parser.add_argument('-e', '--eyes', type = str, default = '00')    #задание символа глаз
    parser.add_argument('-f', '--file', type = str, default = 'default') #конкретный файл коровы или животное из списка
    parser.add_argument('-l', '--list', action = 'store_true') #задание  cowsay.list_cows() 
    parser.add_argument('-n', '--wrap_text', type = bool, default = False)    #если установлен, сообщение не переносится по словам
    parser.add_argument('-T', '--tongue', type = str, default = 'U')    #задание символа языка
    parser.add_argument('-W', '--width', type = int, default = 40)     #где переносить сообщение на новую строку
    parser.add_argument('-m', '--message', type=str, help='Input message for cow') #сообщение



    cow_args = parser.parse_args()
    
    if cow_args.list:                 #если нужно вывести список
        print(list_cows())
    elif cow_args.file != 'default':  #если корова задается в файле или из списка
        if cow_args.file[0] == '/':
            print(cowsay(message = cow_args.message, eyes = cow_args.eyes, cowfile = cow_args.file,
                    wrap_text = cow_args.wrap_text, tongue = cow_args.tongue, width = cow_args.width))
        else:
            print(cowsay(message = cow_args.message, eyes = cow_args.eyes, cow = cow_args.file,
                    wrap_text = cow_args.wrap_text, tongue = cow_args.tongue, width = cow_args.width))
    else:
         print(cowsay(message = cow_args.message, eyes = cow_args.eyes,
                    wrap_text = cow_args.wrap_text, tongue = cow_args.tongue, width = cow_args.width))
         

        

    


if __name__ == "__main__":
    main()