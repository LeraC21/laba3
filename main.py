def p2():
    a = []
    while (a:= str(input())) != "stop":
        print(" ".join(a))

def p3():
    while (a := str(input())) != "stop":
        if "Ф" in a or "ф" in a:
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не редкое слово!")

def p4():

    from random import randint
    h=0
    k=0
    while True:
        a = randint(1,100)
        b = randint(1, 100)
        print (f"{a}+{b} = ", end="")
        res = input()
        while not res.isdigit() and res != "stop":
            print("Вы ввели что-то не то,повторите ввод:",end="")
        res = input()
        if res == "stop":
            break
        if int(res) == a+b:
            k+=1
            print("Правильно")
        else:
            h += 1
            print("Ответ неверный")
        if  h == 3:
            print("Игра окончена.")

p4()


