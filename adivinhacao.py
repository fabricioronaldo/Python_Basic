print("******************************************")
print("* Seja bem vindo ao jogo de adivinhação! *")
print("******************************************")

number_secret = 42

kick = int(input("Digite seu Número:"))
print("O número digitado foi: ", kick)

if (number_secret == kick):
    print("Você acertou!!!")
else:
    print("Você Errou!!!")


print("Fim do Jogo")