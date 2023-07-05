# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 18:02:23 2022

@author: marcos
"""

import csv
from functions.renameClubs import renameClubs

# %%
# Nova versao melhor -> usar essa


def save_file_asrows(listAllClubs):
    import pandas as pd

    path = "C:/Users/marco/OneDrive/Documentos/python/fifa_scrapper/"
    print("SALVAR")
    print(path)
    print("Criando Dataframe...")
    allplayers = pd.DataFrame()
    for listplayers in listAllClubs:
        for player in listplayers:
            newplayer = pd.DataFrame(
                {
                    "club": renameClubs(player.clubName),
                    "name": player.name,
                    "position": player.position,
                    "age": player.age,
                    "overall": player.overall,
                    "nationality": player.nationality,
                    "image": player.imageUrl,
                },
                index=[0],
            )
            allplayers = pd.concat([allplayers, newplayer], axis=0)
    # Join with extra database
    df = pd.read_csv(path + "database/extras.csv", sep=",")

    allplayers = pd.concat([allplayers, df], axis=0)

    # Remove Duplicates - alguns times podem se repetir
    allplayers = allplayers.drop_duplicates(
        subset=["club", "name", "age"], keep="first"
    )

    # Remove players in 2 different clubs - Ex: Coutinho no Barça e Liverpool
    allplayers = allplayers.drop_duplicates(
        subset=["name", "age", "position"], keep="first"
    )
    print(allplayers)
    print("DATAFRAME SHAPE: ")
    print(allplayers.shape)

    print("Salvando...")

    # Save
    import datetime

    x = datetime.datetime.now()
    day = x.strftime("%d")
    month = x.strftime("%m")
    year = x.strftime("%Y")
    save_in = path + f"database/global {year}_{month}_{day}.csv"
    print(allplayers)
    allplayers.to_csv(save_in, sep=",", index=False)

    # Save copy
    copy_allplayers = allplayers
    copy_allplayers.to_csv(path + "database/global_copy.csv", sep=",", index=False)

    print("End")


def save_df(df):
    df.to_csv("database/global.csv", sep=",", index=False)

    # Save copy
    import datetime

    x = datetime.datetime.now()
    day = x.strftime("%d")
    month = x.strftime("%m")
    year = x.strftime("%Y")
    df.to_csv(f"database/global {year}_{month}_{day}.csv", sep=",", index=False)


# %%

# VERSAO ANTIGA PARA SALVAR OS ARQUIVOS


def saveToFile(filename, listAllPlayers):
    # limpa os dados anteriores do arquivo
    with open("data/" + filename + ".csv", "w", encoding="utf-8") as csvFile:
        csvFile.close()

    row_string = []

    commas = ",,,,,,,"

    # ADD 1 LINHA
    string = ""
    for clubsIndex in range(0, len(listAllPlayers)):
        player = listAllPlayers[clubsIndex][0]
        player.clubName = renameClubs(player.clubName)
        string += player.clubName + commas
    row_string.append(["a," + string])

    # TRANSFORM LIST OF PLAYERS INTO ROWS TO SAVE IN CSV
    for playerIndex in range(0, 50):
        string = ""
        for clubsIndex in range(0, len(listAllPlayers)):
            # todo: Check if position exist
            # print(listAllPlayers[clubsIndex][playerIndex].name)
            if len(listAllPlayers[clubsIndex]) > playerIndex:
                player = listAllPlayers[clubsIndex][playerIndex]
                string += (
                    player.name
                    + ","
                    + player.position
                    + ","
                    + str(player.age)
                    + ","
                    + str(player.overall)
                    + ","
                    + player.nationality
                    + ","
                    + player.imageUrl
                    + ",,"
                )
            else:
                string += commas
        row_string.append(["a," + string])

    # %%
    # SAVE TO CSV
    with open("data/" + filename + ".csv", "a", encoding="utf-8") as csvFile:
        writer = csv.writer(
            csvFile, quoting=csv.QUOTE_NONE, escapechar="\\"
        )  # remove quotes in the beggining and end of row
        for string in row_string:
            writer.writerow(string)
    csvFile.close
    # %%

    # Remove // character do escapechar adiconado um pouco antes
    # Alem de remover \\ ele tambem da uma quebra de linha a mais desnecessária
    text = open("data/" + filename + ".csv", "r", encoding="utf8")
    text = "".join([i for i in text]).replace("\\", "").replace("\na", "a")
    x = open("data/" + filename + ".csv", "w", encoding="utf8")
    x.writelines(text)
    x.close()
