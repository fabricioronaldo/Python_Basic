import random
def play():
    print("******************************************")
    print("* Seja bem vindo ao jogo de adivinhação! *")
    print("******************************************")

    number_secret = random.randrange(1, 101)
    totalAttempts = 3
    print(number_secret)
    for round in range(1,totalAttempts + 1):
        cont = -1
        while cont < 0:
            try:
                print("Tentativa {} de {}".format(round,totalAttempts))
                kick = int(input("Digite seu Número:"))
                print("O número digitado foi: ", kick)
                break
            except:
                print("Erro!!! Só é permitido números inteiros positivos")
                continue

        gotItRight = kick == number_secret
        bigger = number_secret > kick
        smaller = number_secret < kick

        if (gotItRight):
            print("Você acertou!!!")
            break
        else:
            if(bigger):

                print("Você Errou!!! O Seu chute foi menor que o número secreto.")
            elif(smaller):
                print("Você Errou!!! O seu chute foi maior que o número secreto.")


    print("Fim do Jogo")