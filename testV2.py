
from colorama import init
from  colorama  import  Fore ,  Back ,  Style 

init()

print(Fore.BLACK)
print(Back.WHITE)

what = input( "Что делаем? (+, -):")

print(Back.CYAN)

a = float( input("Введи первое число:") )
b = float( input("Введи второе число:") )

print(Back.YELLOW)

if what == "+" :
    c = a + b
    print("Результат:" + str(c))
if what == "-" :
    c = a - b
    print("Результат:" + str(c))

else:
	print("Вы выбранли неверную операцыю!!!")

input()