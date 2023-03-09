import random

n = int(input("кол слов"))
f = str("")
word = str("")
for i in range(n):
    word = input("СЛОВА")
    f = f + " " + word
print(f)



def p2():
    stroka = [ ]
    while (new_word := str(input())) != "stop":
     stroka.append(new_word)

    print(" ".join(stroka))




def p3():
    stroka = [ ]
    while (new_word := str(input())) != "stop":
        if "ф" in new_word or "Ф" in new_word:
            print("Ого! Это редкое слово!")
        else:
            print("Эч, это не очень редкое слово...")

def p4():
    import random
    s = 3
    r = 0
    while s != 0:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        itog = a + b
        otvet = int(input(f"Сколько будет {a} + {b}"))
        if itog == otvet:
            print("Ответ правильный")
        else:
            s -= 1
            print("Ответ не тот")
        continue



p2()
p3()
p4()