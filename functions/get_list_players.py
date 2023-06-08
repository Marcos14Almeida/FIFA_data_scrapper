# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:05:46 2022

@author: marcos
"""
from functions.function_soccer_wiki import soccerWiki
from functions.function_so_fifa import soFifa
from functions.function_transfermarkt import transfermarkt
from functions.global_file import globalErrors

# RUN FOR EACH TEAM LIST OF PLAYERS
# Retorna list of list with Player Class -> "List[Clubs][Jogador] = Player"


def getListPlayers(list):
    listAllClubsPlayers = []
    for indexUrl in range(0, len(list)):
        print(list[indexUrl])
        if "sofifa" in list[indexUrl]:
            listPlayers = soFifa(list[indexUrl])
        elif "verein" in list[indexUrl]:
            listPlayers = transfermarkt(list[indexUrl])
        else:
            listPlayers = soccerWiki(list[indexUrl])

        # Se o time tem poucos jogadores, pega mais dados de outros clubes
        if len(listPlayers) < 16:
            clubNameError = listPlayers[0].clubName
            globalErrors.append(
                "%s - Poucos Jogadores: %s" % (clubNameError, len(listPlayers))
            )
            urlAdd = addTeamPlayers(clubNameError)
            additionListPlayers = soccerWiki(urlAdd)
            for (
                players
            ) in additionListPlayers:  # Muda o nome do clube pro nome do time original
                players.clubName = clubNameError
            listPlayers.extend(additionListPlayers)
            if len(listPlayers) > 15:
                # Se continuar com o problema,
                # o globalErrors continua com a mensagem de erro
                globalErrors.pop()

        # Organize players in order of Overall
        listPlayers = organizeBestPlayers(listPlayers)
        # Show RESULT
        printResult(list[indexUrl], listPlayers)

        listAllClubsPlayers.append(listPlayers)

    return listAllClubsPlayers


# %%
def printResult(siteUrl, listPlayers):
    # PRINT RESULT
    print("\n----------------------------------------------------------------")
    print("SiteUrl: %s" % siteUrl)
    print("Time: %s" % listPlayers[0].clubName)
    print("NÚMERO DE JOGADORES: %i\n" % len(listPlayers))
    for x in range(0, len(listPlayers)):
        player = listPlayers[x]
        print(
            player.name.ljust(20),
            player.position.ljust(3),
            player.age,
            player.overall,
            player.nationality,
            player.imageUrl,
        )
    print("Time: %s" % listPlayers[0].clubName)


# %%
# SORT PLAYERS BY OVERALL
def organizeBestPlayers(listPlayers):

    for i in range(0, len(listPlayers)):
        for k in range(i, len(listPlayers)):
            if listPlayers[k].overall > listPlayers[i].overall:
                aux = listPlayers[i]
                listPlayers[i] = listPlayers[k]
                listPlayers[k] = aux

    return listPlayers


# %%
# ADICIONAR JOGADORES AOS TIMES QUE TEM POUCOS JOGADORES:
def addTeamPlayers(clubNameError):

    additionalUrl = ""

    # Place here original team name from Url Database
    if clubNameError == "Académica de Coimbra":
        additionalUrl = "4290"  # Vilafranquense
    elif clubNameError == "US Alessandria":
        additionalUrl = "1644"  # Gubbio
    elif clubNameError == "US Alessandria":
        additionalUrl = "1644"  # Gubbio
    elif clubNameError == "FC Krasnodar":
        additionalUrl = "5535"  # Veles Moskva
    elif clubNameError == "FC Metalist 1925 Kharkiv":
        additionalUrl = "5353"  # FC Minaj
    elif clubNameError == "FC Astana":
        additionalUrl = "2192"  # FC Kaisar
    elif clubNameError == "BATE":
        additionalUrl = "1106"  # Neman Grodno
    elif clubNameError == "Dinamo Minsk":
        additionalUrl = "1113"  # Dinamo Brest
    elif clubNameError == "FK Vardar":
        additionalUrl = "4846"  # Skopje
    elif clubNameError == "Figueirense":
        additionalUrl = "4764"  # Sergipe
    elif clubNameError == "Paraná Clube":
        additionalUrl = "2797"
    elif clubNameError == "Ferroviária":
        additionalUrl = "4794"  # Fluminense de Feira
    elif clubNameError == "Brasiliense":
        additionalUrl = "3249"  # Anapolina
    elif clubNameError == "São Caetano":
        additionalUrl = "2801"  # Tupi
    elif clubNameError == "SER Caxias do Sul":
        additionalUrl = "3519"  # guarani palhoça
    elif clubNameError == "EC Santo André":
        additionalUrl = "3532"  # américa-PE
    elif clubNameError == "Santa Cruz":
        additionalUrl = "2394"  # macaé
    elif clubNameError == "Botafogo PB":
        additionalUrl = "4322"  # atletico cearense
    elif clubNameError == "Botafogo SP":
        additionalUrl = "5581"  # floresta
    elif clubNameError == "Campinense Clube":
        additionalUrl = "4758"  # altos
    elif clubNameError == "Manaus FC":
        additionalUrl = "2216"  # aguia maraba
    elif clubNameError == "Ituano FC":
        additionalUrl = "4792"  # Rio Branco - ES
    elif clubNameError == "Grêmio Novorizontino":
        additionalUrl = "2816"  # Linense
    elif clubNameError == "Volta Redonda FC":
        additionalUrl = "1880"  # Shirak
    elif clubNameError == "Bangu AC":
        additionalUrl = "3057"  # Cabofriense
    elif clubNameError == "Madureira EC":
        additionalUrl = "5772"  # Hercilio Luz
    elif clubNameError == "SE Gama":
        additionalUrl = "2877"  # Aguia Negra
    elif clubNameError == "ABC":
        additionalUrl = "4509"  # Barra
    elif clubNameError == "Brasil de Pelotas":
        additionalUrl = "3505"  # Cametá
    elif clubNameError == "Paulista FC":
        additionalUrl = "3441"  # Rio Preto
    elif clubNameError == "AA Internacional":
        additionalUrl = "3205"  # Coruripe
    elif clubNameError == "CA Juventus":
        additionalUrl = "3678"  # Juventus Jaraguá
    elif clubNameError == "XV de Piracicaba":
        additionalUrl = "3724"  # XV de Jaú
    elif clubNameError == "Joinville EC":
        additionalUrl = "2831"  # Brasilia EC
    elif clubNameError == "EC São Bento":
        additionalUrl = "3244"  # Friburguense
    elif clubNameError == "Portuguesa":
        additionalUrl = "3967"  # Concórdia
    elif clubNameError == "SD Juazeirense":
        additionalUrl = "3102"  # Alecrim
    elif clubNameError == "Atlético Monte Azul":
        additionalUrl = "3042"  # Monte Azul
    elif clubNameError == "AD Confiança":
        additionalUrl = "3502"  # Passo Fundo
    elif clubNameError == "Clube do Remo":
        additionalUrl = "3431"  # EC Cruzeiro
    elif clubNameError == "Ríver AC":
        additionalUrl = "3059"  # EC Pelotas
    elif clubNameError == "Tigre":
        additionalUrl = "3464"  # Deportivo Maipú
    elif clubNameError == "Chacarita Juniors":
        additionalUrl = "4267"  # Deportivo Riestra
    elif clubNameError == "Universitario de Sucre":
        additionalUrl = "5729"  # Real Tomayapo
    elif clubNameError == "Monagas SC":
        additionalUrl = "4263"  # Estudiantes de Caracas
    elif clubNameError == "Zamora FC":
        additionalUrl = "1483"  # Llaneros
    elif clubNameError == "Al Ain":
        additionalUrl = "1346"
    elif clubNameError == "Al Duhail SC":
        additionalUrl = "1213"
    elif clubNameError == "Al Sadd SC":
        additionalUrl = "1408"
    elif clubNameError == "Al Jazira":
        additionalUrl = "1253"
    elif clubNameError == "Persepolis":
        additionalUrl = "1394"
    elif clubNameError == "Al Wahda":
        additionalUrl = "1432"  # Ajman Club
    elif clubNameError == "Al Rayyan":
        additionalUrl = "1694"  # Al Sailiya
    elif clubNameError == "Raja Casablanca":
        additionalUrl = "1944"
    elif clubNameError == "TP Mazembe":
        additionalUrl = "3208"  # AS Vita
    elif clubNameError == "Espérance de Tunis":
        additionalUrl = "567"  # Club Africain
    elif clubNameError == "Wydad AC":
        additionalUrl = "3942"  # MC Oujda
    elif clubNameError == "1º de Agosto":
        additionalUrl = "4194"  # Sagrada Esperança
    elif clubNameError == "Petro Atlético":
        additionalUrl = "4290"  # UD Vilafranquense
    elif clubNameError == "ES Sétif":
        additionalUrl = "2273"  # MC Oran
    elif clubNameError == "Étoile du Sahel":
        additionalUrl = "569"  # CS Sfaxien
    elif clubNameError == "Auckland City":
        additionalUrl = "566"  # Brisbane Roar
    elif clubNameError == "Simba SC":
        additionalUrl = "5943"  # Singida
    else:
        raise ValueError("Time Sem Jogadores Suficientes: " + clubNameError)

    # tem que passar o parametro como lista pra funcao getListPlayers
    return additionalUrl
