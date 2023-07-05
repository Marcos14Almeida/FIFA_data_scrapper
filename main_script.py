"""
Created on Thu Jan  5 19:50:24 2023
@author: marcos
"""

# Link for classificação em tempo real
# 'https://www.msn.com/en-au/sport/football/epl/ladder'

# HOW TO USE BEAUTIFUL SOUP
# https://beautiful-soup-4.readthedocs.io/en/latest/

# FAZER UMA VERSÃO COM WWW.FIFAINDEX NO FUTURO

# Ao acrescentar novo time:
# 1ºAcrescentar site em "FILENAMES.PY"
# 2º mudar "RENAMEClubs.py"
# Se ele tiver poucos jogadores
#       -> adicionar EM FILENAMES.PY na função "addTeamPlayers()"

# =============================================================================
# ================================= Libraries =================================
# =============================================================================

from datetime import datetime
from functions import file_names
from functions.save_file import save_file_asrows
import time
import logging


# =============================================================================
# Functions
# =============================================================================
def print_time(start_time):
    time_passed = time.time() - start_time
    print()
    print("Tempo total:", round(time_passed, 2))


def play_sound():
    import winsound

    # Play sound when finished
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)


def write_log(message):
    with open('log_file.log', 'a') as file:
        file.write(str(datetime.now()) + ' - ' + message + "\n")


# =============================================================================
# Main Code
# =============================================================================
start_time = time.time()

# Configure logging
logging.basicConfig(filename='log_file.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

write_log("Started")

# %%
listAll = file_names.Inglaterra()
save_file_asrows(listAll)
write_log("England1 done")
listAll += file_names.Inglaterra2()
listAll += file_names.Inglaterra3()
listAll += file_names.Inglaterra4()
save_file_asrows(listAll)
listAll += file_names.Espanha()
listAll += file_names.Espanha2()
listAll += file_names.Italia()
listAll += file_names.Italia2()
listAll += file_names.Alemanha()
listAll += file_names.Alemanha2()
listAll += file_names.Alemanha3()
listAll += file_names.França()
listAll += file_names.França2()
listAll += file_names.França3()
write_log("TOP LEAGUES done")
listAll += file_names.Portugal()
listAll += file_names.Holanda()
listAll += file_names.Belgica()
listAll += file_names.EuropaOcidental()
listAll += file_names.EuropaOcidental2()
listAll += file_names.Nordicos()
listAll += file_names.TurquiaGrecia()
listAll += file_names.URSS()
listAll += file_names.LesteEuropeu()
listAll += file_names.EuropaOutros()
save_file_asrows(listAll)
write_log("Europe done")
# %%
listAll += file_names.Brasil()
listAll += file_names.Brasil2()
listAll += file_names.Brasil3()
listAll += file_names.Brasil4()
save_file_asrows(listAll)
write_log("Brazil done")
# %%
listAll += file_names.Argentina()
listAll += file_names.Argentina2()
listAll += file_names.UruguaiParaguai()
listAll += file_names.Chile()
listAll += file_names.PeruBolivia()
listAll += file_names.Colombia()
listAll += file_names.EquadorVenezuela()
save_file_asrows(listAll)
write_log("South America done")
# %%
listAll += file_names.Mexico()
listAll += file_names.MLS()
listAll += file_names.MLS2()
listAll += file_names.CONCACAF()
save_file_asrows(listAll)
write_log("North America done")
# %%
listAll += file_names.Asia()
listAll += file_names.Japao()
listAll += file_names.OrienteMedio()
save_file_asrows(listAll)
write_log("Asia done")
# listAll += file_names.Africa()
save_file_asrows(listAll)
write_log("Africa done")
# listAll += file_names.Oceania()
save_file_asrows(listAll)
write_log("Oceania done")


# %%
# JOIN DATAFRAMES
# SAVE THEM IN A NEW FILE WITH THE CURRENT DAY

# filenameGlobal = "database/global_final.csv"
# df = pd.read_csv(filenameGlobal, sep=",")
# df_global1 = pd.read_csv(filename, sep=",")
# df_global = pd.read_csv(filenameGlobal, sep=",")
# df = pd.concat([df_global, df_global1], axis=0)
# df = df.drop_duplicates(subset=["name", "age", "position"], keep="first")
# save_df(df_global)

# FINISH CODE
print_time(start_time)
play_sound()
write_log("Finish")
write_log("")
