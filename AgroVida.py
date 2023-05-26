#utilizar alguma função
# def informacoesFrutas():
#     Frutas = ["banana", "maca", "abacate", "abacaxi", "acai", "acerola", "amora", "pinha", "mirtilo", "cacau", "caja", "caqui", "carambola", "cereja", "cidra", "coco", "cupuacu", "figo", "framboesa", "morango", "abacaxi", "pera", "melancia", "melao", "jabuticaba", "goiaba", "mamao", "laranja", "groselha", "jaca", "jenipapo", "kiwi", "limao", "manga", "maracuja", "pequi", "pessego", "pitanga", "pitaya", "roma", "siriguela", "tamara", "tamarindo", "tangerina", "tucuma", "uva"]

#     tipoFruta = input("\nQual o seu tipo de fruta? (digite sem acentos): ")

#     selecionado = -1
#     for i in range(0, len(Frutas)):
#         if Frutas[i].lower() == tipoFruta.lower():
#             selecionado = i
#             break
#     if selecionado < 0:
#         # Fruta nao encontrada
#         pass
#     print("%s Selecionada!" % Frutas[selecionado])


def regiao():

    print("\n[1] - Norte" +
          "\n[2] - Nordeste" +
          "\n[3] - Centro-Oeste" +
          "\n[4] - Sudeste" +
          "\n[5] - Sul")
    regiao = int(input("\nDigite o número da região em que você reside: "))
    
    match regiao:
        case 1:
            print("\nNorte Selecionado")
            frutasNorte()
        case 2:
            print("\nNordeste Selecionado")
            frutasNordeste()
        case 3:
            print("\nCentro-Oeste Selecionado")
        case 4:
            print("\nSudeste Selecionado")
        case 5:
            print("\nSul Selecionado")


def frutasNorte():
    frutas = ["Açaí", "Bacuri", "Camu-Camu", "Cupuaçu", "Guaraná", "Muruci", "Tapereba", "Tucumã"]

    for i in range(0, len(frutas)):
        print(f" {i+1}º fruta: " + frutas[i])

    continuar = True
    while(continuar == True):
        frutaSelecionada = int(input("\nEscolha o número da fruta: "))

        verificacao = input(f"{frutas[frutaSelecionada-1]} é a fruta que você deseja saber informações?: [s] ou [n]: ")

        if(verificacao == "s"):
            continuar = False

        nomeFruta = frutas[frutaSelecionada-1]

    opcao = int(input(f"\n[1] - Tempo para Colheita do fruto {nomeFruta}" +
                        f"\n[2] - Qual altura a/o {nomeFruta} pode alcançar" +
                        f"\n[3] - Qual tipo de solo é melhor para plantar a/o {nomeFruta}"+
                        "\nQual número? => "))
    
    match opcao:
        case 1:
            match nomeFruta:
                case "Açaí":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 10 meses")
                case "Bacuri":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 8 meses")
                case "Camu-Camu":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 4 meses")
                case "Cupuaçu":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 15 meses")
                case "Guaraná":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 11 meses")
                case "Muruci":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 5 meses")
                case "Tapereba":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 17 meses")
                case "Tucumã":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 21 meses")
        case 2:
            match nomeFruta:
                case "Açaí":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 10 metros aproximadamente")
                case "Bacuri":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 17 metros aproximadamente")
                case "Camu-Camu":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 9 metros aproximadamente")
                case "Cupuaçu":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 5 metros aproximadamente")
                case "Guaraná":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o arenoso")
                case "Muruci":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 12 metros aproximadamente")
                case "Tapereba":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 3 metros aproximadamente")
                case "Tucumã":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 20 metros aproximadamente")
        case 3:
            match nomeFruta:
                case "Açaí":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o arenoso")
                case "Bacuri":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o de terra roxa")
                case "Camu-Camu":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o de mangue")
                case "Cupuaçu":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o enxarcado")
                case "Guaraná":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o vulcanico")
                case "Muruci":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com argila")
                case "Tapereba":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com logo")
                case "Tucumã":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o húmico")

def frutasNordeste():
    frutas = ["Jambo Rosa", "Araçá", "Umbu", "Pitomba", "Sapoti", "Maracujá", "Abacaxi", "Melão", "Banana", "Caju", "Mamão", "Manga", "Laranja"]

    for i in range(0, len(frutas)):
        print(f" {i+1}º fruta: " + frutas[i])

    continuar = True
    while(continuar == True):
        frutaSelecionada = int(input("\nEscolha o número da fruta: "))

        verificacao = input(f"{frutas[frutaSelecionada-1]} é a fruta que você deseja saber informações?: [s] ou [n]: ")

        if(verificacao == "s"):
            continuar = False

        nomeFruta = frutas[frutaSelecionada-1]

    opcao = int(input(f"\n[1] - Tempo para Colheita do fruto {nomeFruta}" +
                        f"\n[2] - Qual altura a/o {nomeFruta} pode alcançar" +
                        f"\n[3] - Qual tipo de solo é melhor para plantar a/o {nomeFruta}" +
                        "\nQual número? => "))
    
    match opcao:
        case 1:
            match nomeFruta:
                case "Jambo Rosa":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 10 meses")
                case "Araçá":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 8 meses")
                case "Umbu":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 4 meses")
                case "Pitomba":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 15 meses")
                case "Sapoti":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 11 meses")
                case "Maracujá":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 5 meses")
                case "Abacaxi":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 17 meses")
                case "Melão":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 21 meses")
                case "Banana":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 3 meses")
                case "Caju":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 6 meses")
                case "Mamão":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 13 meses")
                case "Manga":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 14 meses")
                case "Laranja":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 19 meses")
        case 2:
            match nomeFruta:
                case "Jambo Rosa":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 12 metros aproximadamente")
                case "Araçá":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 5 metros aproximadamente")
                case "Umbu":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 9 metros aproximadamente")
                case "Pitomba":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 5 metros aproximadamente")
                case "Sapoti":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 3 metros aproximadamente")
                case "Maracujá":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 11 metros aproximadamente")
                case "Abacaxi":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 10 metros aproximadamente")
                case "Melão":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 2 metros aproximadamente")
                case "Banana":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 13 metros aproximadamente")
                case "Caju":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 15 metros aproximadamente")
                case "Mamão":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 12 metros aproximadamente")
                case "Manga":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 7 metros aproximadamente")
                case "Laranja":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 4 metros aproximadamente")
        case 3:
            match nomeFruta:
                case "Jambo Rosa":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o húmico")
                case "Araçá":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o vulcânico")
                case "Umbu":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o arenoso")
                case "Pitomba":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o semi-arenoso")
                case "Sapoti":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o solo com lodo")
                case "Maracujá":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o de mangue")
                case "Abacaxi":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com minhocas")
                case "Melão":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com restos mortais")
                case "Banana":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com muito adubo")
                case "Caju":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o alagado")
                case "Mamão":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o firme")
                case "Manga":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o seco")
                case "Laranja":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o adubado")

def frutasCentroOeste():
    aawd

def frutasSudeste():
    awdawd

def frutasSul():
    awdawd


def tecnicasSustentaveis():
    awdawd



#COMEÇO DO CHATBOT #COMEÇO DO CHATBOT #COMEÇO DO CHATBOT

print("Bem vindo ao nosso CHATBOT AgroVida!")

print("Em que eu posso lhe ajudar?")
print("[1] - Informações sobre Frutas" + 
      "\n[2] - Técnicas de Sustentabilidade de Plantio")

opcao = int(input("Digite a opção desejada: "))

match opcao:
    case 1:
        print("Informações sobre Frutas SELECIONADA\n")
        regiao()
    case 2:
        print("Técnicas de Sustentabilidade de Plantio SELECIONADO\n")
        tecnicasSustentaveis()
        