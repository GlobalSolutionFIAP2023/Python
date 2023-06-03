import arrays as ar #importa o arquivo arrays.py

#FUNÇÃO DE INPUT, QUE TRATA ERROS COM TRY-CATCH, PASSANDO COMO PARÂMETRO (MENSAGEM EXIBIDA NORMALMENTE, TIPO DE VARIÁVEL, MENSAGEM DE POSSÍVEL ERRO E MENSAGEM DE ERRO DEFAULT)
def inputMaster(mensagem,type,possibleExecpt,execpMensage):
    while True:
        try:
            response = type(input(mensagem))
            #responde = int(input("\nDigite o número da região em que deseja saber sobre fruta: "))
        except possibleExecpt as execpMensage:
            print(execpMensage)
        except Exception as e:
            print(e)
        else:
            return response

#FUNÇÃO COM FOR-EACH, PEGANDO O PARÂMETRO DE ARRAY DE UM ALIMENTO DE DETERMINADA REGIÃO E IMPRIMINDO NA TELA, LINHA POR LINHA, ENUMERADAS
def Imprimir(objArray):
    for i in range(0, len(objArray)):
        print(f" {i+1} - " + objArray[i][0])


#FUNÇÃO QUE IMPRIME AS REGIÕES DO ARRAY DE 'REGIÕES' E REQUERE AO USUÁRIO, ATRAVÉS DO INPUT-MASTER, O NUMERO DE UMA REGIÃO QUE DESEJA CONSULTAR AS FRUTAS, LEGUMES E VERDURAS
#   A PARTIR DO NÚMERO DO USUÁRIO, ELE ESCOLHE NO ARRAY DE 'CLIMAS', PEGANDO O CLIMA DE DETERMINADA REGIÃO E EXIBINDO NA TELA
#   APÓS ISSO, ELE JOGA O PARÂMETRO 'REGIÃO' NA FUNÇÃO  alimentoAEscolher() PARA QUE O USUÁRIO ESCOLHA UM ALIMENTO DE DETERMINADA REGIÃO
def regiao(parametro):
    for i in range(0,len(ar.regioes)):
        print(f"[{i+1}] - {ar.regioes[i]}")
    
    regiao = inputMaster("\nDigite o número da região em que deseja: ", int, ValueError, "Digite um Numero!!\n")

    climas = ["\n\nA região Norte, apresenta clima:\n\n  EQUATORIAL ÚMIDO –> marcado por elevadas temperaturas – e tropical continental, que resulta em duas estações bem definidas (chuvosa e seca).\n", "\n\nA região Nordeste, apresenta clima:\n\n  TROPICAL ÚMIDO ->  Verão quente e úmido, com temperaturas elevadas o ano todo, que variam entre 25 e 31 graus.\n", "\n\nA região Centro-Oeste, apresenta clima:\n\n   TROPICAL SEMIÚMIDO ->  Duas estações bem definidas – um inverno seco e um verão muito quente e chuvoso. As temperaturas variam bastante: cerca de 40 °C nos meses mais quentes e 15 °C nos meses mais frios.\n", "\n\nA região Sudeste, apresenta clima:\n\n   TROPICAL  ->  Temperaturas altas e duas estações bem marcadas: o verão chuvoso, e o inverno seco.\n", "\n\nA região Sul, apresenta clima:\n\n   SUBTROPICAL  ->  Estações do ano bem diferenciadas, com grandes variações de temperatura. É a região mais fria do País, onde, durante o inverno, ocorrem geadas e até neve em alguns lugares.\n"]
    
    try:
        print(climas[regiao-1])
    except IndexError as IE:
        print("Opção não disponivel")
        regiao()
    except Exception as e:
        print(e)
    else:
        if(parametro == "fruta"):
            alimentoAEscolher(regiao, 0)
        elif(parametro == "verdura"):
            alimentoAEscolher(regiao, 1)
        elif(parametro == "legume"):
            alimentoAEscolher(regiao, 2)



#FUNÇÃO DE ESCOLHER AS FRUTAS, LEGUMES E VERDURAS DA REGIÃO ESCOLHIDA, PASSADA POR PARÂMETRO.
#   ATRIBUI NA VARIAVEL "alimentos", O ARRAY DE FRUTAS, VERDURAS OU LEGUMES DA REGIÃO ESCOLHIDA
#   DEPOIS PUXA A FUNÇÃO DE IMPRIMIR COM O FOR-EACH, PASSANDO O ARRAY DE FRUTAS, OU VERDURAS OU LEGUMES DA REGIÃO ESCOLHIDA
#   APÓS ISSO, TEM A VERIFICAÇÃO DE SELEÇÃO DA FRUTA, LEGUME OU VERDURA QUE O USUÁRIO SELECIONOU, PODENDO NÃO TER NO ARRAY, EXIBINDO UMA MENSAGEM DE ERRO E PEDINDO DENOVO PARA O USUÁRIO DIGITAR O NÚMERO, 
#   E, DEPOIS, UMA VERIFICAÇÃO COM 'SIM' OU 'NÃO'
#   APÓS CONFIRMAR, PASSA POR PARÂMETRO O NUMERO DA FRUTA, LEGUME OU VERDURA SELECIONADA JUNTO COM O ARRAY PRA EXIBIR AS INFORMAÇÕES SOBRE O ALIMENTO
def alimentoAEscolher(regiao, tipoAlimento):
    alimentos = ar.alimentosRegioes[tipoAlimento][regiao-1]
    Imprimir(alimentos) #entra o Array, faz o forEach e exibe todos os alimentos enumerados

    alimentoSelecionado = inputMaster("\nEscolha o número do alimento: ", int, ValueError, "Digite um Numero!!")
    if(alimentoSelecionado > len(alimentos) or alimentoSelecionado < 1):
        print("Número Inválido!")
        alimentoAEscolher(regiao, tipoAlimento)
    else:
        confirmacao = input(f"Deseja saber saber as informações sobre {alimentos[alimentoSelecionado-1][0]}?\n[S] - Sim\n[N] - Não \n> ")
        if confirmacao.lower() == "s":
            informacoes(alimentos[alimentoSelecionado-1])
        else:
            alimentoAEscolher(regiao, tipoAlimento)



#APÓS PEGAR O ARRAY DA FRUTA, DA VERDURA E DO LEGUME PELO PARÂMETRO, ELE ENTRA NO WHILE E EXIBE AS INFORMAÇÕES SOBRE A FRUTA, VERDURA OU LEGUME SELECIONADO
# PEGANDO DO ARRAY "RESPOSTAS", APOS O USUÁRIO DIGITAR O NUMERO DA OPÇÃO, ELE EXIBE A INFORMAÇÃO SOBRE A FRUTA, VERDURA OU LEGUME SELECIONADO
def informacoes(array):
    respostas = ["Tamanho Médio da(o) ", "Tempo Médio para Colheita da(o) ", "Tipo de Solo Ideal da(o) "]
    print("\n\nQual informação você deseja saber? \n> ")
    for i in range(len(respostas)):
        print(f"[{i+1}] - {respostas[i]}{array[0]}") 

    opcao = inputMaster("\n> ", int, ValueError, "Digite um Numero!!") 
    if opcao > 0 and opcao <= len(respostas):
        print(f"\n{respostas[opcao-1].upper()}{array[0].upper()} => {array[opcao].upper()}")

        repetir = input(f"\nDeseja saber mais alguma informação sobre {array[0]}?\n[S] - Sim\n[N] - Não\n> ")
        if repetir.lower() == "s":
            informacoes(array)
    else:
        print("\nOpção Inválida!\n")
        informacoes(array)



#APÓS O USUÁRIO SELECIONAR A OPÇÃO DE TECNICAS SUSTENTÁVEIS, ELE PERGUNTA QUAL TÉCNICA ELE DESEJA APRENDER
# FAZ UM FOR-EACH DAS TÉCNICAS, PUXANDO APENAS O INDEX DO NOME DAS TÉCNICAS, EXIBINDO AO USUÁRIO E REQUISITANDO O NUMERO DE ESCOLHA
# SE ESCOLHER RECICLAGEM, FARÁ UM FOR-EACH NOVAMENTE EXIBINDO OS TIPO DE RECICLAGEM, SENDO PUXADO APENAS O INDEX DO NOME DO ARRAY DOS TIPOS DE RECICLAGEM
# CASO ESCOLHER OUTRO TIPO DE TÉCNICA, EXIBIRÁ O NOME E O CONTEÚDO DO TIPO DE TÉCNICA SUSTENTÁVEL
def tecnicasSustentaveis():
    print("\n\n\nQual técnica você deseja aprender?\n")
    Imprimir(ar.tecnicas)
    tecnica = int(input("\n\nQual numero? -> "))

    if tecnica == 1: # SE O USUÁRIO ESCOLHER A OPÇÃO 1, ELE SERÁ DIRECIONADO PARA ESTA FUNÇÃO
        for i in range(0, len(ar.tecnicas[0][1])): # AQUI SERÁ IMPRESSO TODAS AS OPÇÕES DE ADUBAGEM
            print(f"[{i+1}] - {ar.tecnicas[0][1][i][0]}")
        escolha = int(input("Qual numero?\n> ")) # APÓS O USUÁRIO ESCOLHER A OPÇÃO DE ADUBAGEM, IRA EXIBIR O NOME E A DESCRIÇÃO DA TECNICA SUSTENTAVEL
        print(ar.tecnicas[0][1][escolha-1][1])

        repetir = input(f"\n\nDeseja saber mais alguma informação sobre Técnicas Sustentáveis?\n[S] - Sim\n[N] - Não\n> ")
        if repetir.lower() == "s":
            tecnicasSustentaveis()
    else:
        print(ar.tecnicas[tecnica-1][1]) # CASO A ESCOLHA DO USUARIO FOR != 1, IRA EXIBIR O NOME E A DESCRIÇÃO DA TECNICA SUSTENTAVEL
    


# APÓS O USUÁRIO ESCOLHER A OPÇÃO DE ADUBAGEM NO MENU, ELE SERÁ DIRECIONADO PARA ESTA FUNÇÃO
# AQUI ELE PODERÁ ESCOLHER ENTRE AS OPÇÕES DE ADUBAGEM E APÓS ESCOLHER, SERÁ MOSTRADO A DESCRIÇÃO DA ADUBAGEM
def adubagem():
    # EXISTE UM ARRAY 'adubagem' QUE POSSUI INFORMAÇÕES EM SEU INDEX, MAS TAMBEM EXISTEM OUTROS CONJUNTOS DE ARRAYS DENTRO DELE, QUE POSSUEM MAIS INFORMAÇÕES
    
    print(f"\n\n{ar.adubagem[0][0].upper()}\n{ar.adubagem[0][1]}")
    # IMPRIME O TITULO.UPPER() E A DESCRIÇÃO DO TIPO DE ADUBO
    i = True
    while i == True:
        print("\n\nQual tipo de adubagem você deseja aprender?") # PERGUNTA QUAL TIPO DE ADUBO O USUARIO DESEJA APRENDER
        Imprimir(ar.adubagem[1]) # IMPRIME OS TIPOS DE ADUBO DISPONIVEIS
        tipo = int(input("\n\nQual numero? -> ")) # PERGUNTA QUAL TIPO DE ADUBO O USUARIO DESEJA APRENDER

        if tipo <= len(ar.adubagem[1]) and tipo > 0: # VERIFICA SE O NUMERO DIGITADO É VALIDO
            print(f"\n\n[{ar.adubagem[1][tipo-1][0].upper()}] \n{ar.adubagem[1][tipo-1][1]}\n")   # IMPRIME O TITULO.UPPER() E A DESCRIÇÃO DO TIPO DE ADUBO
            i2 = True
            while i2 == True:
                Imprimir(ar.adubagem[1][tipo-1][2])  # IMPRIME OS TIPOS DO ADUBO SELECIONADO
                tipoAdubagemSelecionada = int(input("\n\nQual numero? \n> ")) # PERGUNTA QUAL TIPO DE ADUBO SELECIONADO, O USUARIO DESEJA APRENDER

                if tipoAdubagemSelecionada > 0 and tipoAdubagemSelecionada <= len(ar.adubagem[1][tipo-1][2]): # VERIFICA SE O NUMERO DIGITADO É VALIDO
                    print(f"\n\n[{ar.adubagem[1][tipo-1][2][tipoAdubagemSelecionada-1][0].upper()}] \n{ar.adubagem[1][tipo-1][2][tipoAdubagemSelecionada-1][1]}\n") # IMPRIME O TITULO.UPPER() E A DESCRIÇÃO DO TIPO DE ADUBO
        
                    repetir = input(f"\n\nDeseja saber mais alguma informação sobre Adubagem? \n[S] - Sim\n[N] - Não\n> ")
                    if repetir.lower() == "n":
                        i = False
                        i2 = False
                    else:
                        i2 = False
                else:
                    print("\nOpção inválida!\n")
        else:
            print("\nOpção inválida!\n")
    


# ARRAY COM AS INFORMAÇÕES SOBRE INSETICIDAS NATURAIS
def inseticidaNatural():
    #ARRAY CONTENDO 'INSETICIDAS NATURAIS', 'O QUE É INSETICIDA NATURAL' E UM ARRAY CONTENDO O TIPOS DE INSETICIDAS NATURAIS

    print(f"\n\n[{ar.inseticida[0].upper()}] \n{ar.inseticida[1]}\n")
    print("Existem vários tipos de inseticidas naturais, veja alguns exemplos: \n")
    
    while True:
        Imprimir(ar.inseticida[2]) #array de ForEach, passando parâmetro 3ª posição do array inseticida
        tipo = int(input("\nQual inseticida natural você deseja saber? \n> "))
        if tipo > 0 and tipo <= len(ar.inseticida[2]):
            print(f"\n\n{ar.inseticida[2][tipo-1][0].upper()} \n{ar.inseticida[2][tipo-1][1]} \n\nMODO DE USO: {ar.inseticida[2][tipo-1][2]}")
            # 3 index do array INSETICIDA, pegando a posição do TIPO DE INSETICIDA escolhido pelo usuário, e imprimindo as informações em UPPER(), depois fazendo o mesmo caminho, só que agora acessando o modo de uso do inseticida escolhido
            
            repetir = input(f"\n\nDeseja saber mais alguma informação sobre {ar.inseticida[0]}?\n[S] - Sim\n[N] - Não\n> ")
            if repetir.lower() == "n":
                break
        else:
            print("Opção Inválida!")