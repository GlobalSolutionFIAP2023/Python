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
            frutasCentroOeste()
        case 4:
            print("\nSudeste Selecionado")
            frutasSudeste()
        case 5:
            print("\nSul Selecionado")
            frutasSul()


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
    return "Norte"


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
    return "Nordeste"


def frutasCentroOeste():
    frutas = ["Pequi", "Cajuí", "Cagaita", "Guavira", "Bacuri", "Jatobá", "Cajuzinho-do-cerrado", "Bocaiuva", "Embaúba", "Mama-cadela"]

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
                case "Pequi":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 10 meses")
                case "Cajuí":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 8 meses")
                case "Guavira":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 4 meses")
                case "Bacuri":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 15 meses")
                case "Jatobá":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 11 meses")
                case "Cajuzinho-do-cerrado":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 5 meses")
                case "Bocaiuva":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 17 meses")
                case "Embaúba":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 21 meses")
                case "Mama-cadela":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 3 meses")
        case 2:
            match nomeFruta:
                case "Pequi":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 12 metros aproximadamente")
                case "Cajuí":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 5 metros aproximadamente")
                case "Guavira":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 9 metros aproximadamente")
                case "Bacuri":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 5 metros aproximadamente")
                case "Jatobá":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 3 metros aproximadamente")
                case "Cajuzinho-do-cerrado":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 11 metros aproximadamente")
                case "Bocaiuva":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 10 metros aproximadamente")
                case "Embaúba":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 2 metros aproximadamente")
                case "Mama-cadela":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 13 metros aproximadamente")
        case 3:
            match nomeFruta:
                case "Pequi":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o húmico")
                case "Cajuí":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o vulcânico")
                case "Guavira":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o arenoso")
                case "Bacuri":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o semi-arenoso")
                case "Jatobá":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o solo com lodo")
                case "Cajuzinho-do-cerrado":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o de mangue")
                case "Bocaiuva":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com minhocas")
                case "Embaúba":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com restos mortais")
                case "Mama-cadela":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com muito adubo")
    return "CentroOeste"


def frutasSudeste():
    frutas = ["Laranja", "Limão", "Banana", "Abacate", "Manga", "Uva", "Pera", "Maçã", "Morango", "Jabuticaba"]

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
                case "Laranja":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 10 meses")
                case "Limão":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 8 meses")
                case "Banana":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 4 meses")
                case "Abacate":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 15 meses")
                case "Manga":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 11 meses")
                case "Uva":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 5 meses")
                case "Pera":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 17 meses")
                case "Maçã":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 21 meses")
                case "Morango":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 3 meses")
                case "Jabuticaba":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 9 meses")
        case 2:
            match nomeFruta:
                case "Laranja":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 12 metros aproximadamente")
                case "Limão":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 5 metros aproximadamente")
                case "Banana":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 9 metros aproximadamente")
                case "Abacate":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 5 metros aproximadamente")
                case "Manga":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 3 metros aproximadamente")
                case "Uva":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 11 metros aproximadamente")
                case "Pera":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 10 metros aproximadamente")
                case "Maçã":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 2 metros aproximadamente")
                case "Morango":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 13 metros aproximadamente")
                case "Jabuticaba":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 8 metros aproximadamente")
        case 3:
            match nomeFruta:
                case "Laranja":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o húmico")
                case "Limão":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o vulcânico")
                case "Banana":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o arenoso")
                case "Abacate":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o semi-arenoso")
                case "Manga":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o solo com lodo")
                case "Uva":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o de mangue")
                case "Pera":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com minhocas")
                case "Maçã":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com restos mortais")
                case "Morango":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com muito adubo")
                case "Jabuticaba":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com muito adubo")
    return "Sudeste"


def frutasSul():
    frutas = ["Maçã", "Uva", "Ameixa", "Pêssego", "Acerola", "Caqui", "Laranja", "Tangerina", "Limão"]
    
    for i in range(0, len(frutas)):
        print(f" {i+1}º fruta: " + frutas[i])

    continuar = True
    while(continuar == True):
        frutaSelecionada = int(input("\nEscolha o número da fruta: "))
        
        if(frutaSelecionada > 9 or frutaSelecionada == 0):
            print("Essa fruta não existe em nosso banco de dados!")
            print("Tente Novamente")
        else:
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
                case "Maçã":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 10 meses")
                    return "Sul"
                case "Uva":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 8 meses")
                    return "Sul"
                case "Ameixa":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 4 meses")
                    return "Sul"
                case "Pêssego":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 15 meses")
                    return "Sul"
                case "Acerola":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 5 meses")
                    return "Sul"
                case "Caqui":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 17 meses")
                    return "Sul"
                case "Laranja":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 21 meses")
                    return "Sul"
                case "Tangerina":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 3 meses")
                    return "Sul"
                case "Limão":
                    print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de 9 meses")
                    return "Sul"
        case 2:
            match nomeFruta:
                case "Maçã":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 12 metros aproximadamente")
                case "Uva":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 5 metros aproximadamente")
                case "Ameixa":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 9 metros aproximadamente")
                case "Pêssego":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 5 metros aproximadamente")
                case "Acerola":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 11 metros aproximadamente")
                case "Caqui":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 10 metros aproximadamente")
                case "Laranja":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 2 metros aproximadamente")
                case "Tangerina":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 13 metros aproximadamente")
                case "Limão":
                    print(f"\nO tamanho médio do(a) {nomeFruta} é entre 8 metros aproximadamente")
        case 3:
            match nomeFruta:
                case "Maçã":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o húmico")
                case "Uva":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o vulcânico")
                case "Ameixa":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o arenoso")
                case "Pêssego":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o semi-arenoso")
                case "Acerola":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o de mangue")
                case "Caqui":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com minhocas")
                case "Laranja":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com restos mortais")
                case "Tangerina":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com muito adubo")
                case "Limão":
                    print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o com muito adubo")
    
    return "Sul"


def tecnicasSustentaveis():
    print("\n\n\nQual técnica você deseja aprender?")
    
    tecnica = int(input("\n[1] - Reciclagem" +
          "\n[2] - Captação de Água da Chuva" +
          "\n[3] - Restos de alimentos para compostagem" +
          "\n[4] - Inseticida Natural" +
          "\n[5] - Horta Orgânica" +
          "\n\nQual numero? -> "))
     
    if(tecnica == 1):
        print("\n\nTécnicas de Reciclagem\n")

        tecRecicle = int(input("[1] - Coleta Seletiva dos Residuos" + 
              "\n[2] - Reutilizar Objetos" +
              "\n[3] - Embalagens Recicláveis"))

        if(tecRecicle == 1):
            print("[REALIZAR COLETA SELETIVA DOS RESÍDUOS] => " + "método de coletar e separar os resíduos de acordo com suas características. Ou seja, se os resíduos possuem características similares são segregados e coletados juntos (papel, plástico, vidro, metal e resíduo orgânico). Isso ajuda a reciclagem, tornando-a mais fácil e viável economicamente.")

        elif(tecRecicle == 2):
            print("[REUTILIZAR OBJETOS] => " + "Sabe aquele pote de requeijão, que é de vidro? Então, você pode reutilizar ele como um copo. Adote esse tipo de pensamento sobre como utilizar uma coisa em outra, tornando o mundo mais sustentável.")

        elif(tecRecicle == 3):
            print("[EMBALAGENS RECICLÁVEIS] => " + "Opte por usar embalagens recicláveis, que possam ser reutilizadas, após serem lavadas.")
    elif(tecnica == 2):
        print("\n\n[CAPTAÇÃO DE ÁGUA DA CHUVA]")
        print("\nA água é um recurso essencial para vida humana, isso é indiscutível, e já existem várias alternativas para suprir a carência de água de qualidade aqui no Brasil, como utilizar os rios e mananciais. E uma excelente alternativa para economizar água em casa e fácil de replicar, que permite o melhor aproveitamento desse recurso natural é a captação de água da chuva e utilizar para tarefas domésticas. \n\nExiste também sistemas de captação de água de chuva, como um tanque de água da chuva usado para coletar e armazenar o escoamento da água da chuva, e outros como uma Cisternas que normalmente é instalada em telhados por meio de tubos, são soluções alternativas eficientes usadas na hora de economizar água. \n\nVale a pena avaliar a possibilidade de instalar um sistema de coleta de água de chuva e/ou simplesmente considerar a possibilidade de armazenar a água de chuva para utilizá-la em tarefas domésticas e assim economizar nosso recurso natural mais importante que é Água. Se cada um contribuir um pouco, o planeta agradece!")
    elif(tecnica == 3):
        print("\n[RESTOS DE ALIMENTOS PARA COMPOSTAGEM]")
        print("  Existem várias possibilidades de reaproveitamento dos resíduos de alimentos, e a forma mais comum é através da compostagem doméstica, contribuindo para reduzir gases do efeito estufa e o lixo orgânico.\n\n  A compostagem é um processo de reciclagem do lixo orgânico, transforma a matéria orgânica encontrada no lixo em adubo natural, que pode ser usado na agricultura, em jardins e plantas, substituindo o uso de produtos químicos.")
    elif(tecnica == 4):
        print("\n   [INSETICIDA NATURAL]")
        print("Como a sociedade já tem mais conhecimento da necessidade da sustentabilidade, e falamos no tópico acima sobre produzir alimentos orgânicos em casa, então com isso surge também a necessidade de alternativas para o controle biológico de pragas, insetos, pois o tradicional utiliza muita química e que prejudica as plantas e o solo. \n\nOs inseticidas naturais representam essa alternativa para produtores rurais que não querem utilizar agentes químicos em suas lavouras e até mesmo para pessoas comuns que estão em busca de uma solução útil contra a proliferação de insetos em suas residências. \n\nA sugestão é utilizar ingredientes naturais como alho, coentro, hortelã, tabaco, pimenta, essas são algumas opções de inseticidas naturais que podem ser usados para proteger plantações e combater pragas que atacam lavouras ou até mesmo hortas caseiras, contra larvas, borboletas, formigas, pulgões, lagartas, moscas, mosquitos entre outros, ok?")
    elif(tecnica == 5):
        print("\n   [HORTA ORGÂNICA]")
        print("Cultivar vegetais em casa, não é uma exclusividade de fazendas e chácaras, é possível ter uma horta orgânica até em espaços pequenos, além de promover o cultivo sem agredir o solo e o meio ambiente. \n\nPara hortas em ambientes internos e na utilização de vasos, potes, garrafas e outros recipientes, seja em hortas verticais ou horizontais, você não deve esquecer de providenciar furos no fundo para evitar o excesso de água no solo, isso pode contribuir para apodrecer as raízes. \n\nEntão a sugestão é se preocupar primeiro com solo que uma parte muito importante, ele precisa ser fofo e rico em nutrientes, isso deixará seus vegetais saudáveis e uma boa dica é utilizar adubos originados de itens naturais, como cascas e restos de vegetais.")







#COMEÇO DO CHATBOT #COMEÇO DO CHATBOT #COMEÇO DO CHATBOT

print("Bem vindo ao nosso CHATBOT AgroVida!")

print("Em que eu posso lhe ajudar?")
print("\n[1] - Informações sobre Frutas" + 
      "\n[2] - Técnicas de Sustentabilidade de Plantio")

opcao = int(input("\nDigite a opção desejada: "))

match opcao:
    case 1:
        regiao()

        while(finalizacao == "n"):
            finalizacao = input("\nDeseja finalizar o nosso atendimento? [s] ou [n] -> ")

            regiao()

        print("\nVolte Sempre!")

    case 2:
        tecnicasSustentaveis()

        print("\nVolte Sempre!")