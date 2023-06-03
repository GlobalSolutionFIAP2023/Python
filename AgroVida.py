import funcoes as f #importa o arquivo funcoes.py

#COMEÇO DO CHATBOT   #COMEÇO DO CHATBOT   #COMEÇO DO CHATBOT
print("\nBem vindo ao CHATBOT AgroVida!")

# EXIBE O MENU DE OPÇÕES PARA O USUÁRIO ESCOLHER O QUE DESEJA SABER SOBRE A AGRICULTURA SUSTENTÁVEL
while True:
    opcao = ["Informações sobre Frutas", "Informações sobre Verduras", "Informações sobre Legumes", "Técnicas de Sustentabilidade", "Informações sobre Adubagem de Solo", "Informações sobre Inseticidas Naturais"]
    print("\n\nO que você deseja saber sobre a agricultura sustentável? \n")
    for i in range(0, len(opcao)):
        print(f"[{i+1}] - {opcao[i]}") #imprime o menu de opções

    while True:
        opcao = int(input("\n\nQual número > ")) #recebe a opção escolhida pelo usuário
        if opcao == 1:
            f.regiao("fruta")
            break
        elif opcao == 2:
            f.regiao("verdura")
            break
        elif opcao == 3:
            f.regiao("legume")
            break
        elif opcao == 4:
            f.tecnicasSustentaveis()
            break
        elif opcao == 5:
            f.adubagem()
            break
        elif opcao == 6:
            f.inseticidaNatural()
            break
        elif opcao < 1 or opcao > 6:
            print("Opção Inválida!")

    # PERGUNTA SE O USUÁRIO DESEJA CONTINUAR COM O PROGRAMA OU ENCERRAR
    continuar = input("\n\n\nDeseja realizar outra consulta de informação conosco? [s] ou [n] \n> ")
    if(continuar.lower() == "n"):
        print("\nAjude o nosso planeta a ser mais sustentável, até mais!")
        break