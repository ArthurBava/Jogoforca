#Arthur B.Spada RA: 1136264
import os
import time

# Função para desenhar o boneco da forca
def desenhar_forca(vidas):
    if vidas == 6:
        print(" ________")
        print("|        |")
        print("|        |")
        print("         |")
        print("         |")
        print("         |")
        print("         |")
        print("=============")
    elif vidas == 5: 
        print(" ________")
        print("|        |")
        print("|        |")
        print("O        |")
        print("         |")
        print("         |")
        print("         |")
        print("=============")
    elif vidas == 4: 
        print(" ________")
        print("|        |")
        print("|        |")
        print("O        |")
        print("|        |")
        print("         |")
        print("         |")
        print("=============")
    elif vidas == 3:
        print("  ________")
        print(" |        |")
        print(" |        |")
        print(" O        |")
        print("/|        |")
        print("          |")
        print("          |")
        print(" =============")
    elif vidas == 2: 
        print("  ________")
        print(" |        |")
        print(" |        |")
        print(" O        |")
        print("/|\       |")
        print("          |")
        print("          |")
        print(" =============")
    elif vidas == 1:
        print("  ________")
        print(" |        |")
        print(" |        |")
        print(" O        |")
        print("/|\       |")
        print("  \       |")
        print("          |")
        print(" =============")


def exibir_info_atual(dicas, vidas, letras_incorretas):
    print(f"Você tem {dicas} dicas restantes.")
    print(f"Você tem {vidas} vidas restantes.")
    print("Letras incorretas:", ', '.join(letras_incorretas))
    desenhar_forca(vidas)

def jogar_novamente():
    while True:
        resposta = input("Deseja jogar novamente? (1 - Sim / 2 - Não): ")
        if resposta == "1":
            return True
        elif resposta == "2":
            return False
        else:
            print("Opção inválida. Por favor, escolha 1 para 'Sim' ou 2 para 'Não'.")

def main():
    os.system("cls")

    print("Bem-vindo ao jogo da forca!")
    jogador1 = input("Digite o nome do jogador 1: ")
    jogador2 = input("Digite o nome do desafiante: ")
    os.system("cls")

    # Obter a palavra chave e dicas
    palavrachave = input("Digite qual vai ser a palavra chave do jogo: ")
    dicas = 3
    dica1 = input("Escreva a dica número 1: ") 
    dica2 = input("Escreva a dica número 2: ")
    dica3 = input("Escreva a dica número 3: ")
    os.system("cls")

    # Inicializar as letras da palavra chave com asteriscos
    letras_jogo = "*" * len(palavrachave)
    print(letras_jogo)
    os.system("cls")

    # Inicializar o número de tentativas, vidas e lista de letras incorretas
    vidas = 6
    letras_incorretas = []

    while True:
        print("Escolha uma das opções abaixo:")
        print("Aperte (j) para Jogar")
        print("Aperte (d) para receber uma Dica")
        comecar = input()
        
        if comecar == "j":
            os.system("cls")
            exibir_info_atual(dicas, vidas, letras_incorretas)
            print("Sua Palavra chave é:", letras_jogo)
            letra = input("Escolha uma letra: ")
            os.system("cls")
            
            # Verificar se a letra escolhida está na palavra chave
            if letra in palavrachave:
                print("Letra correta!")
                for i in range(len(palavrachave)):
                    if palavrachave[i] == letra:
                        letras_jogo = letras_jogo[:i] + letra + letras_jogo[i+1:]
            else:
                print("Letra incorreta!")
                vidas -= 1
                letras_incorretas.append(letra)
            
            # Verificar se o jogador ganhou ou perdeu
            if letras_jogo == palavrachave:
                print("Parabéns! Você ganhou!")
                time.sleep(10)
                os.system("cls")
                if not jogar_novamente():
                    break
                else:
                    os.system("cls")
                    palavrachave = input("Digite qual vai ser a palavra chave do jogo: ")
                    dicas = 3
                    dica1 = input("Escreva a dica número 1: ") 
                    dica2 = input("Escreva a dica número 2: ")
                    dica3 = input("Escreva a dica número 3: ")
                    os.system("cls")
                    letras_jogo = "*" * len(palavrachave)
                    vidas = 6
                    letras_incorretas = []
            elif vidas == 0:
                os.system("cls")
                print("Você perdeu! A palavra chave era:", palavrachave)
                print("  ________")
                print(" |        |")
                print(" |        |")
                print(" O        |")
                print("/|\       |")
                print("/ \       |")
                print("          |")
                print("===========")
                time.sleep(8)
                os.system("cls")
                if not jogar_novamente():
                    break
                else:
                    os.system("cls")
                    palavrachave = input("Digite qual vai ser a palavra chave do jogo: ")
                    dicas = 3
                    dica1 = input("Escreva a dica número 1: ") 
                    dica2 = input("Escreva a dica número 2: ")
                    dica3 = input("Escreva a dica número 3: ")
                    os.system("cls")
                    letras_jogo = "*" * len(palavrachave)
                    vidas = 6
                    letras_incorretas = []
                
        elif comecar == "d":
            os.system("cls")
            if dicas > 0:
                print("Dica:", dica1 if dicas == 3 else (dica2 if dicas == 2 else dica3))
                dicas -= 1
            else:
                print("Você já usou todas as dicas!")
if __name__ == "__main__":
    main()
