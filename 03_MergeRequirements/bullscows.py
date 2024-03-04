import sys
import random
import urllib
from urllib.request import urlopen
from cowsay import cowsay, get_random_cow



#Предполагается, что слова одинаковой длины
def bullscows(guess: str, secret: str) -> tuple[int, int]:
    bulls = sum([guess[i] == secret[i]  for i in range(len(secret))])
    cows = len(list(set(guess) & set(secret)))
    return bulls, cows


#Функция, спрашивающая слово у игрока
def ask(prompt: str, valid: list[str] = None) -> str:
    if valid == None:
        cow_tmp = get_random_cow()
        print(cowsay(prompt, cow_tmp))
        guess_word = input()
        return guess_word
    else:
        cow_tmp = get_random_cow()
        print(cowsay('Введите слово только из Вашего списка:', cow_tmp))
        guess_word = input()
        if guess_word in valid:
            return guess_word
        else:
            print('Неизвестное слово! Введите еще раз!')
            return ask(prompt, valid)



#Функция вывода результата предположения игрока
def inform(format_string: str, bulls: int, cows: int) -> None:
    cow_tmp = get_random_cow()
    print(cowsay(format_string.format(bulls, cows), cow_tmp))
    return




def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret_word = words[random.randint(0, len(words) - 1)]
    bulls = 0
    cows = 0
    c = 0
    while (bulls != len(secret_word) or cows != len(secret_word)):
        guess_word = ask("Введите слово:", words)
        bulls, cows = bullscows(guess_word, secret_word)
        inform("Быки: {}, Коровы: {}", bulls, cows)
        c += 1
        if (guess_word == secret_word):
            print("Слово угадано! слово: {}", guess_word)
            return c
    return






def main():
    if len(sys.argv) < 2:
        print("Ошибка аргументов вызова")
        return
    
    url = sys.argv[1]
    word_length = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    #Открытие словаря
    if url.startswith("http"):
        link = urllib.request.urlopen(url)
        dict_all = link.readlines()
        link.close()

        #Переводим bytes в str
        for i in range(len(dict_all)):
            dict_all[i] = dict_all[i].decode('utf-8')
            dict_all[i] = dict_all[i].strip().replace("\n", '')
    else:
        with open(url, 'r', encoding='utf-8') as file:
            dict_all = file.readlines()
    
    dict = [x for x in dict_all if len(x) == word_length]

    #Начало игры
    attempts = gameplay(ask, inform, dict)
    print(attempts)
    return



if __name__ == "__main__":
    main()