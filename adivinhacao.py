print("******************************************")
print("* Seja bem vindo ao jogo de adivinhação! *")
print("******************************************")

number_secret = 42

kick = int(input("Digite seu Número:"))
print("O número digitado foi: ", kick)

gotItRight = kick == number_secret
bigger = number_secret > kick
smaller = number_secret < kick


if (gotItRight):
    print("Você acertou!!!")
else:
    if(bigger):

        print("Você Errou!!! O Seu chute foi menor que o número secreto.")
    elif(smaller):
        print("Você Errou!!! O seu chute foi maior que o número secreto.")


print("Fim do Jogo")