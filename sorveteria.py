import time
from time import sleep
print ('Olá seja bem-vindo a nossa sorveteria, que sabor você vai quere hoje?')
sleep(2)
print("""As opções são:
[ 1 ] Menta
[ 2 ] Chocolate)
[ 3 ] Caramelo)
[ 4 ] Paçoca
[ 5 ] Coco"""
)
escolha = int(input('Qual você vai escolher? '))
if escolha == 1:
    print("Bela escolha, menta é ótimo para se refrescar")
    sleep(2)
    print("São R$ 4,50")
    sleep(2)
    print("Volte sempre!!!")
elif escolha == 2:
    print("Chocolate é um clássico")
    sleep(2)
    print ("São R$ 4,00")
    sleep(2)
    print("Volte sempre!!!")
elif escolha == 3:
    print("Caramelo vende bastante")
    sleep(2)
    print ("São R$ 6,00")
    sleep(2)
    print("Volte sempre!!!")
elif escolha == 4:
    print("Paçoca é uma ótima escolha")
    sleep(2)
    print ("São R$ 7,00")
    sleep(2)
    print("Volte sempre!!!")
elif escolha == 5:
    print("Que sorte, esse é o último")
    sleep(2)
    print ("São R$ 6,00")
    sleep(2)
    print("Volte sempre!!!")
else:
    print("Infelizmente eu não tenho esse sabor")
    print("Volte sempre!!!")
