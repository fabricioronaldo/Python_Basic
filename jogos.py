import forca
import adivinhacao

print("******************************************")
print("********** Escolha o seu jogo! ***********")
print("******************************************")

print("Escolha seu jogo - (1) Forca - (2) Adivinhação")

jogo = int(input("Qual sua escolha:"))

if (jogo == 1):
    print("Jogando Forca")
    forca.play()
elif (jogo == 2):
    print("Jogando Adivinhação")
    adivinhacao.play()