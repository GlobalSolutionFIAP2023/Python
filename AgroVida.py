regioes = ["Norte","Nordeste","Centro-Oeste","Sudeste","Sul"]


frutasNorte = [["Açaí",10,10,"arenoso"], ["Bacuri",8,17," terra roxa"], ["Camu-Camu",4,9,"de mange"], ["Cupuaçu",15,5,"enxarcado"], ["Guaraná",11,6,"arenoso"], ["Muruci",5,12,"argila"], ["Tapereba",17,3,"com logo"], ["Tucumã",21,20,"húmico"]]

frutasNordeste = [["Jambo Rosa",10, 12, "húmico"], ["Araçá",8,5,"Vulcânico"], ["Umbu",4,9,"arenoso"], ["Pitomba",12,4,"de mangue"], ["Sapoti",10,9,"arenoso"], ["Maracujá",9,20,"alagado"], ["Abacaxi",32,1,"duro"], ["Melão",3,8,"esburacado"], ["Banana",6,2,"Enxarcado"], ["Caju",3,10,"rochoso"], ["Mamão",9,3,"terra roxa"], ["Manga",12,5,"de argila"], ["Laranja",10,9,"vulcanico"]]

frutasCentroOeste = [["Pequi",10,12,"húmico"], ["Cajuí",8,5,"vulcânico"], ["Cagaita",4,9,"arenoso"], ["Guavira",4,10,"de argila"], ["Bacuri",15,9,"arenoso"], ["Jatobá",26,9,"vulcanico"], ["Cajuzinho-do-cerrado",2,19,"arenoso"], ["Bocaiuva",10,8,"de terra roxa"], ["Embaúba",19,12,"de mange"], ["Mama-cadela",19,10,"vulcanico"]]

frutasSudeste = [["Laranja",3,2,"arenoso"], ["Limão",4,1,"arenoso"], ["Banana",4,5,"equatorial"], ["Abacate",10,3,"arenoso"], ["Manga",65,2,"solo cagado"], ["Uva",10,4,"Molhadinho"], ["Pera",19,23,"solo fudido"], ["Maçã",60,5,"rico em filho da puta"], ["Morango",10,2,"sla"], ["Jabuticaba",32,42,"Sem ideia ja"]]

frutasSul = [["Maçã",19,3,"empedrado"], ["Uva",3,2,"rochoso"], ["Ameixa",4,8,"húmico"], ["Pêssego",6,10,"arenoso"], ["Acerola",8,10,"de mângue"], ["Caqui",52,9,"pisoteado"], ["Laranja",1,3,"adubado"], ["Tangerina",5,1,"seco"], ["Limão",8,10,"rochoso"]]

frutasRegioes = [frutasNorte, frutasNordeste, frutasCentroOeste, frutasSudeste, frutasSul] 


def inputMaster(mensagem,type,possibleExecpt,execpMensage):
    while True:
        try:
            response = type(input(mensagem))
            #responde = int(input("\nDigite o número da região em que deseja saber sobre fruta: "))
        except possibleExecpt as exec:
            print(execpMensage)
        except Exception as e:
            print(e)
        else:
            return response



def regiao():
    for i in range(0,len(regioes)):
        print(f"[{i+1}] - {regioes[i]}")
    
    regiao = inputMaster("\nDigite o número da região em que deseja saber sobre fruta: ", int, ValueError, "Digite um Numero!!\n")

    climas = ["A região Norte, apresenta clima:\n\n  EQUATORIAL ÚMIDO –> marcado por elevadas temperaturas – e tropical continental, que resulta em duas estações bem definidas (chuvosa e seca).", "A região Nordeste, apresenta clima:\n\n  TROPICAL ÚMIDO ->  Verão quente e úmido, com temperaturas elevadas o ano todo, que variam entre 25 e 31 graus.", "A região Centro-Oeste, apresenta clima:\n\n   TROPICAL SEMIÚMIDO ->  Duas estações bem definidas – um inverno seco e um verão muito quente e chuvoso. As temperaturas variam bastante: cerca de 40 °C nos meses mais quentes e 15 °C nos meses mais frios.", "A região Sudeste, apresenta clima:\n\n   TROPICAL  ->  Temperaturas altas e duas estações bem marcadas: o verão chuvoso, e o inverno seco.", "A região Sul, apresenta clima:\n\n   SUBTROPICAL  ->  Estações do ano bem diferenciadas, com grandes variações de temperatura. É a região mais fria do País, onde, durante o inverno, ocorrem geadas e até neve em alguns lugares."]
    
    try:
        print(climas[regiao-1])
    except IndexError as IE:
        print("Opção não disponivel")
        regiao()
    except Exception as e:
        print(e)
    else:
        frutasAEscolher(regiao)


def ImprimirFrutas(frutasArray):
    print("\nCombinando com essa frutas a seguir...")
    for i in range(0, len(frutasArray)):
        print(f" {i+1}º fruta: " + frutasArray[i][0])




def frutasAEscolher(regiao):
    frutas = frutasRegioes[regiao-1]
    ImprimirFrutas(frutas) #entra o Array, faz o forEach e exibe todos as frutas enumeradas
    
    frutaSelecionada = inputMaster("\nEscolha o número da fruta: ", int, ValueError, "Digite um Numero!!")
    confirmacao = input(f"Deseja saber saber as informações sobre {frutas[frutaSelecionada-1][0]}?\n[S] - Sim\n[N] - Não \n> ")
    
    if confirmacao.lower() == "s":
        infoFruta(frutas[frutaSelecionada-1])
    else:
        frutasAEscolher(regiao)

    


def infoFruta(fruta):
    nomeFruta = fruta[0]
    opcao = int(input(f"\n[1] - Tempo para Colheita do fruto {nomeFruta}" +
                        f"\n[2] - Qual altura a/o {nomeFruta} pode alcançar" +
                        f"\n[3] - Qual tipo de solo é melhor para plantar a/o {nomeFruta}"+
                        "\nQual número? => "))
    match opcao:
        case 1:
            print(f"\nO tempo médio para o(a) {nomeFruta} dar fruto é de {fruta[1]} meses")
        case 2:
            print(f"\nO tamanho médio do(a) {nomeFruta} é entre {fruta[2]} metros aproximadamente")
        case 3:
            print(f"\nO tipo de solo mais adequado para o(a) {nomeFruta} é o {fruta[3]}")



def tecnicasSustentaveis():
    print("\n\n\nQual técnica você deseja aprender?")
    
    tecnicas = [["Reciclagem",
                    [
                        ["Coleta Seletiva dos Residuos","[REALIZAR COLETA SELETIVA DOS RESÍDUOS] => método de coletar e separar os resíduos de acordo com suas características. Ou seja, se os resíduos possuem características similares são segregados e coletados juntos (papel, plástico, vidro, metal e resíduo orgânico). Isso ajuda a reciclagem, tornando-a mais fácil e viável economicamente."],
                        ["Reutilizar Objetos","[REUTILIZAR OBJETOS] => Sabe aquele pote de requeijão, que é de vidro? Então, você pode reutilizar ele como um copo. Adote esse tipo de pensamento sobre como utilizar uma coisa em outra, tornando o mundo mais sustentável."],
                        ["Embalagens Recicláveis","[EMBALAGENS RECICLÁVEIS] => Opte por usar embalagens recicláveis, que possam ser reutilizadas, após serem lavadas."]
                    ]
                ],
                ["Captação de Água da Chuva", "\n\n[CAPTAÇÃO DE ÁGUA DA CHUVA \nA água é um recurso essencial para vida humana, isso é indiscutível, e já existem várias alternativas para suprir a carência de água de qualidade aqui no Brasil, como utilizar os rios e mananciais. E uma excelente alternativa para economizar água em casa e fácil de replicar, que permite o melhor aproveitamento desse recurso natural é a captação de água da chuva e utilizar para tarefas domésticas. \n\nExiste também sistemas de captação de água de chuva, como um tanque de água da chuva usado para coletar e armazenar o escoamento da água da chuva, e outros como uma Cisternas que normalmente é instalada em telhados por meio de tubos, são soluções alternativas eficientes usadas na hora de economizar água. \n\nVale a pena avaliar a possibilidade de instalar um sistema de coleta de água de chuva e/ou simplesmente considerar a possibilidade de armazenar a água de chuva para utilizá-la em tarefas domésticas e assim economizar nosso recurso natural mais importante que é Água. Se cada um contribuir um pouco, o planeta agradece!"],
                    
                ["Restos de alimentos para compostagem","\n[RESTOS DE ALIMENTOS PARA COMPOSTAGEM]\n Existem várias possibilidades de reaproveitamento dos resíduos de alimentos, e a forma mais comum é através da compostagem doméstica, contribuindo para reduzir gases do efeito estufa e o lixo orgânico.\n\n  A compostagem é um processo de reciclagem do lixo orgânico, transforma a matéria orgânica encontrada no lixo em adubo natural, que pode ser usado na agricultura, em jardins e plantas, substituindo o uso de produtos químicos."],
                ["Inseticida Natural", "\n Como a sociedade já tem mais conhecimento da necessidade da sustentabilidade, e falamos no tópico acima sobre produzir alimentos orgânicos em casa, então com isso surge também a necessidade de alternativas para o controle biológico de pragas, insetos, pois o tradicional utiliza muita química e que prejudica as plantas e o solo. \n\nOs inseticidas naturais representam essa alternativa para produtores rurais que não querem utilizar agentes químicos em suas lavouras e até mesmo para pessoas comuns que estão em busca de uma solução útil contra a proliferação de insetos em suas residências. \n\nA sugestão é utilizar ingredientes naturais como alho, coentro, hortelã, tabaco, pimenta, essas são algumas opções de inseticidas naturais que podem ser usados para proteger plantações e combater pragas que atacam lavouras ou até mesmo hortas caseiras, contra larvas, borboletas, formigas, pulgões, lagartas, moscas, mosquitos entre outros, ok?"],
                ["Horta Orgânica", "\n[HORTA ORGÂNICA]\n Cultivar vegetais em casa, não é uma exclusividade de fazendas e chácaras, é possível ter uma horta orgânica até em espaços pequenos, além de promover o cultivo sem agredir o solo e o meio ambiente. \n\nPara hortas em ambientes internos e na utilização de vasos, potes, garrafas e outros recipientes, seja em hortas verticais ou horizontais, você não deve esquecer de providenciar furos no fundo para evitar o excesso de água no solo, isso pode contribuir para apodrecer as raízes. \n\nEntão a sugestão é se preocupar primeiro com solo que uma parte muito importante, ele precisa ser fofo e rico em nutrientes, isso deixará seus vegetais saudáveis e uma boa dica é utilizar adubos originados de itens naturais, como cascas e restos de vegetais."]]


    for i in range(0,len(tecnicas)):
        print(f"[{i+1}] - {tecnicas[i][0]}")
    tecnica = int(input("\n\nQual numero? -> "))

    if tecnica == 1:
        for i in range(0, len(tecnicas[0][1])):
            print(f"{i+1} - {tecnicas[0][1][i][0]}")
            
        escolha = int(input("Qual numero?\n> "))
        print(tecnicas[0][1][escolha-1][1])
    else:
        print(tecnicas[tecnica][1])
    





#COMEÇO DO CHATBOT   #COMEÇO DO CHATBOT   #COMEÇO DO CHATBOT

print("\nBem vindo ao CHATBOT AgroVida!")

nomeUsuario = input("Primeiramente, nos informe seu nome: ")
sobrenomeUsuario = input("Agora seu sobrenome: ")
telefoneUsuario = int(input("Informe seu telefone: "))
idadeUsuario = int(input("Digite sua idade: "))

generos = ["Masculino", "Feminino", "Prefiro não dizer"]
for i in range(0, len(generos)):
    print(f"[{i+1}] - {generos[i]}")

inputGenero = int(input("Escolha seu gênero: \n> "))
generoUsuario = generos[inputGenero-1]

usuario = {"Nome":nomeUsuario,"Sobrenome":sobrenomeUsuario,"Telefone":telefoneUsuario,"Idade":idadeUsuario, "Gênero":generoUsuario}

for key in usuario:
    print(f"{key} - {usuario[key]}")


# dadosUsuario = True
# while (dadosUsuario):
#     print("\n\n[1] - Nome: " + nomeUsuario)
#     print("[2] - Sobrenome: " + sobrenomeUsuario)
#     print("[3] - Telefone: " + str(telefoneUsuario))
#     print("[4] - Idade: " + str(idadeUsuario))
#     print("[5] - Gênero: " + generos[-1])
#     print("[6] - Prosseguir com o atendimento...")
#     alterarDado = input("Deseja alterar algum dado? : ")

#     if(alterarDado == 1):
#         nomeUsuario = input("Informe seu nome: ")
#         print("Nome Atualizado -> " + nomeUsuario)
#     elif(alterarDado == 2):
#         sobrenomeUsuario = input("Informe seu sobrenome: ")
#         print("Sobrenome Atualizado -> " + sobrenomeUsuario)
#     elif(alterarDado == 3):
#         telefoneUsuario = int(input("Informe seu telefone: "))
#         print("Telefone Atualizado -> " + telefoneUsuario)
#     elif(alterarDado == 4):
#         idadeUsuario = int(input("Digite sua idade: "))
#         print("Idade Atualizada -> " + idadeUsuario)
#     elif(alterarDado == 5):
#         escolhaGenero = int(input("Escolha seu gênero: " +
#                              "\n[1] - Masculino" + 
#                              "\n[2] - Feminino" +
#                              "\n[3] - Prefiro nao dizer"))
#         print("Gênero Atualizado!" + generos[escolhaGenero-1])
#     elif(alterarDado == 6):
#         dadosUsuario = False



# usuarios = ["Agricultor", "Admin"]
# escolhaUsuario = int(input("Você é um usuário: " +
#                                "\n[1] - Agricultor" +
#                                "\n[2] - Admin" +
#                                "\n\nEscolha o número: "))

# # if(usuarios[escolhaUsuario-1] == "Admin"):



loop = True
while(loop):
    print("--------------------------------------")
    print("\nEm que eu posso lhe ajudar?")
    print("\n[1] - Informações sobre Frutas" + 
        "\n[2] - Técnicas de Sustentabilidade de Plantio")

    opcao = int(input("\nDigite a opção desejada: "))

    match opcao:
        case 1:
            regiao()
            print("\nVolte Sempre!")

        case 2:
            tecnicasSustentaveis()
            print("\nVolte Sempre!")
    
    continuar = input("\nDeseja realizar outra consulta de informação conosco? [s] ou [n]: ")
    if(continuar == "s"):
        loop = True
    else:
        loop = False
        print("\nAjude o nosso planeta a ser mais sustentável, até mais!")