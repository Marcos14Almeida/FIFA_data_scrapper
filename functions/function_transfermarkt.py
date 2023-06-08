# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:46:32 2023

@author: marcos
"""
import random
import requests
import re  # regular expressions
from bs4 import BeautifulSoup
import pickle
import numpy as np
import math
from functions.renameNationality import renameNationality
from functions.class_player import Player
from functions.renameClubs import renameClubs


# %%
def rename_url(url):
    url = url.replace("kader", "startseite")
    if "/plus/1" not in url:
        url = url + "/plus/1"
    return url


# %%
def transfermarkt(clubID):
    # Ex: clubID = "aa-ponte-preta/startseite/verein/1134"
    siteUrl = rename_url(clubID)
    siteUrl = "https://www.transfermarkt.com.br/" + str(siteUrl)
    print("Loading...")
    print(siteUrl)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"
    }
    response = requests.get(siteUrl, headers=headers)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    header = soup.find(
        "h1",
        {
            "class": "data-header__headline-wrapper data-header__headline-wrapper--oswald"
        },
    )
    clubName = header.text.strip()

    # Find the table containing the players' information
    table = soup.find("table", {"class": "items"})
    # print(table)

    # Extract the players' names and ages from the table
    players = []
    listAllPlayers = []
    x = 0
    for row in table.find_all("tr", {"class": ["odd", "even"]}):
        name = row.find("td", {"class": "hauptlink"}).text.strip()
        name = name.split(".")[0][:-1]  # Ex: Antonio MeloA. Melo -> Antonio MeloA
        name = name[:-1]  # Remove Last Word
        # name = name[:round(len(name)/2)] # Os nomes estao duplicados: Ex: BrunoMazengaBrunoMazenga
        age = row.find_all("td", {"class": "zentriert"})[1].text.strip()
        # Age format: 13/12/1993 (29)
        if "-" in age:
            age = "0"
        else:
            age = re.search(r"\((\d+)\)", age).group(1)
        # pos = row.find('td', {'class': 'zentriert'}).get('title')
        pos = row.find_all("td")[1].find_all("td")[-1].text.strip()
        pos = rename_pos(pos)
        country = (
            row.find("td", {"class": "zentriert"}).find_next_sibling("td").img["title"]
        )
        flag_img = soup.find("img", class_="flaggenrahmen")
        country = flag_img.get("title")
        country = renameNationality(country)
        value = row.find_all("td", {"class": "rechts"})[0].text.strip()
        value = get_money_value(value)
        ovr = predict_ovr(age, value, pos)
        image_url = row.find("td", {"rowspan": "2"}).find("img").get("data-src")
        image_url = image_url.replace("medium", "header").replace("small", "header")
        image_url = image_url.replace(
            "https://img.a.transfermarkt.technology/portrait/", ""
        )

        # SAVE DATA TO CLASS
        # print(name_list[x],nationalities[x], imageUrls[x])
        if age != "0" and "-" not in age:
            player = Player(
                x,
                clubName,
                name,
                pos,
                age,
                ovr,
                country,
                image_url,
            )
            listAllPlayers.append(player)
            x += 1

            players.append(
                {
                    "club": clubName,
                    "name": name,
                    "pos": pos,
                    "age": age,
                    "ovr": ovr,
                    "value": value,
                    "country": country,
                    "image_url": image_url,
                }
            )

    printPlayers(players)

    return listAllPlayers


def rename_pos(pos):
    if pos == "Goleiro":
        pos = "GOL"
    elif pos == "Zagueiro":
        pos = "ZAG"
    elif pos == "Defensores":
        pos = "ZAG"
    elif pos == "Defensor":
        pos = "ZAG"
    elif pos == "Lateral Esq.":
        pos = "LE"
    elif pos == "Lateral Dir.":
        pos = "LD"
    elif pos == "Volante":
        pos = "VOL"
    elif pos == "Meia Central":
        pos = "MC"
    elif pos == "Meio-Campo":
        pos = "MEI"
    elif pos == "Meia Ofensivo":
        pos = "MEI"
    elif pos == "Meia Direita":
        pos = "MD"
    elif pos == "Meia Esquerda":
        pos = "ME"
    elif pos == "Ponta Esquerda":
        pos = "PE"
    elif pos == "Ponta Direita":
        pos = "PD"
    elif pos == "Centroavante":
        pos = "ATA"
    elif pos == "Atacante":
        pos = "ATA"
    elif pos == "Seg. Atacante":
        pos = "ATA"
    return pos


def get_money_value(value):
    if "mil" in value:
        value = value.replace(",", ".").replace("mil €", "")
        value = float(value) / 1000
    elif "mi." in value:
        value = value.replace(",", ".").replace("mi. €", "")
        value = float(value)
    elif "-" in value:
        value = 0.0
    else:
        value = 0.0

    return value


def printPlayers(players):
    print(players[0]["club"])
    players = sorted(players, key=lambda k: k["ovr"], reverse=False)
    for i, player in enumerate(players):
        print(
            str(i + 1).ljust(2),
            "-",
            player["name"].ljust(20),
            player["ovr"],
            player["pos"].ljust(3),
            player["age"],
            player["country"],
            "  $",
            str(player["value"]).ljust(5),
            # player['image_url'].replace("https://img.a.transfermarkt.technology/portrait/header/","").replace(".jpg?lm=1",""),
        )
    print(players[0]["club"], " -> ", renameClubs(players[0]["club"]))
    print("-" * 50)


def predict_ovr(age, value, pos):
    # print(pos)
    if pos == "GOL":
        pos = 0
    elif pos == "ZAG":
        pos = 1
    elif pos == "LE":
        pos = 1
    elif pos == "LD":
        pos = 1
    elif pos == "VOL":
        pos = 2
    elif pos == "MC":
        pos = 2
    elif pos == "MEI":
        pos = 3
    elif pos == "MD":
        pos = 3
    elif pos == "ME":
        pos = 3
    elif pos == "PE":
        pos = 4
    elif pos == "PD":
        pos = 4
    elif pos == "ATA":
        pos = 4
    age = int(age)
    value = float(value)

    # load the model from file
    with open(model_path, "rb") as file:
        model = pickle.load(file)

    # make predictions with the loaded model
    X_test = np.array([[age, value, pos]])
    y_pred = model.predict(X_test)
    y_pred = math.floor(y_pred)

    if value == 0.0:
        y_pred -= random.randint(1, 3)

    return y_pred


# Clicar em Tabela Completa
list_europa = [
    # Portugal
    "cf-os-belenenses/startseite/verein/68608",
    "academica-coimbra/startseite/verein/2990",
    "moreirense-fc/kader/verein/979/saison_id/2022",
    "cd-nacional/startseite/verein/982",
    # Russia
    "zska-moskau/startseite/verein/2410/saison_id/2022",
    "dinamo-moskau/startseite/verein/121/saison_id/2022",
    "fk-krasnodar/startseite/verein/16704/saison_id/2022",
    "krylya-sovetov-samara/startseite/verein/2696/saison_id/2022",
    "lokomotiv-moskau/startseite/verein/932/saison_id/2022",
    "fk-rostov/startseite/verein/1083/saison_id/2022",
    "fk-sochi/startseite/verein/41231/saison_id/2022",
    "spartak-moskau/startseite/verein/232/saison_id/2022",
    "ural-ekaterinburg/startseite/verein/11127/saison_id/2022",
    "zenit-st-petersburg/startseite/verein/964",
    # Ucrania
    "sk-dnipro-1/startseite/verein/60551/saison_id/2022",
    "dynamo-kiew/startseite/verein/338",
    "shakhtar-donetsk/startseite/verein/660/saison_id/2022",
    "zorya-lugansk/startseite/verein/10690/saison_id/2022",
    # EX-URSS
    "fc-astana/startseite/verein/22220",
    "bate-borisov/startseite/verein/713",
    "dinamo-tiflis/startseite/verein/663",
    "qarabağ-fk/startseite/verein/10625",
    "fc-sheriff-tiraspol/startseite/verein/2481",
    "fc-riga/startseite/verein/48325",
    "fk-rfs/startseite/verein/33783/saison_id/2022",
    "zalgiris-vilnius/startseite/verein/602",
    # Balcãs
    # Bosnia
    "hsk-zrinjski-mostar/startseite/verein/6808/saison_id/2022",
    "fk-zeljeznicar-sarajevo/startseite/verein/2573/saison_id/2022",
    # Bulgaria
    "zska-sofia/startseite/verein/208/saison_id/2022",
    "levski-sofia/startseite/verein/156/saison_id/2022",
    "pfk-ludogorets-razgrad/startseite/verein/31614",
    # Croacia
    "hnk-rijeka/startseite/verein/144",
    # Eslovenia
    "nk-maribor/startseite/verein/790",
    "nk-olimpija-ljubljana/startseite/verein/4772/saison_id/2022",
    # Eslovaquia
    "dac-dunajska-streda/startseite/verein/4529/saison_id/2022",
    "slovan-bratislava/startseite/verein/540",
    "spartak-trnava/startseite/verein/365/saison_id/2022",
    # Hungria
    "ferencvaros-budapest/startseite/verein/279",
    "budapest-honved-fc/spielplan/verein/709/saison_id/2022",
    "kecskemeti-te/startseite/verein/12423/saison_id/2022",
    "puskas-akademia-fc/startseite/verein/37169/saison_id/2022",
    "ujpest-fc/kader/verein/708/saison_id/2022",
    # Israel
    "hapoel-beer-sheva/startseite/verein/2976/saison_id/2022",
    "maccabi-haifa/startseite/verein/1064",
    "maccabi-tel-aviv/startseite/verein/119/saison_id/2022",
    # Macedonia
    "vardar-skopje/startseite/verein/77"
    # Romenia
    "fcsb/startseite/verein/301",
    "cfr-cluj/startseite/verein/7769/saison_id/2022"
    "fc-viitorul-constanța/startseite/verein/29831/saison_id/2022",
    # Sérvia
    "fk-tsc-backa-topola/startseite/verein/3137/saison_id/2022",
    "roter-stern-belgrad/startseite/verein/159/saison_id/2022",
    "fk-partizan-belgrad/startseite/verein/669",
    "fk-vojvodina-novi-sad/startseite/verein/448/saison_id/2022",
]

list_america = [
    # Brasil
    "ec-bahia/kader/verein/10010",
    "esporte-clube-vitoria/startseite/verein/2125",
    "ceara-sporting-club/startseite/verein/2029",
    "fortaleza-esporte-clube/startseite/verein/10870",
    "sport-club-do-recife/startseite/verein/8718",
    "clube-de-regatas-brasil-al-/startseite/verein/11449",
    "centro-sportivo-alagoano-al-/startseite/verein/18545",
    "sampaio-correa-fc-ma-/startseite/verein/3319",
    "clube-nautico-capibaribe/startseite/verein/2646",
    "abc-futebol-clube-rn-/startseite/verein/7209",
    "santa-cruz-futebol-clube-pe-/startseite/verein/1785",
    "club-sportivo-sergipe-se-/startseite/verein/7816",
    "fluminense-ec-pi-/startseite/verein/87817",
    "campinense-clube-pb-/startseite/verein/1753",
    "ferroviario-atletico-clube-ce-/startseite/verein/11931",
    "alagoinhas-atletico-clube-ba-/startseite/verein/25229",
    "botafogo-futebol-clube-pb-/startseite/verein/17964",
    "associacao-desportiva-confianca-se-/startseite/verein/3280",
    "river-atletico-clube-pi-/startseite/verein/35388",
    "moto-club-de-sao-luis-ma-/startseite/verein/12009",
    "america-mineiro/kader/verein/2863",
    "atletico-mineiro/kader/verein/330",
    "ec-cruzeiro-belo-horizonte/startseite/verein/609",
    "tombense-futebol-clube-mg-/startseite/verein/3234",
    "gremio-porto-alegre/startseite/verein/210",
    "sc-internacional-porto-alegre/startseite/verein/6600",
    "esporte-clube-juventude/startseite/verein/10492",
    "ypiranga-futebol-clube-rs-/startseite/verein/16869",
    "gremio-esportivo-brasil-rs-/startseite/verein/10560",
    "ser-caxias-do-sul-rs-/startseite/verein/9141",
    "esporte-clube-novo-hamburgo-rs-/startseite/verein/8794",
    "club-athletico-paranaense/startseite/verein/679",
    "coritiba-fc/startseite/verein/776",
    "londrina-esporte-clube-pr-/startseite/verein/1693",
    "avai-fc-sc-/startseite/verein/2035",
    "chapecoense/startseite/verein/17776",
    "criciuma-esporte-clube/startseite/verein/7178",
    "brusque-futebol-clube-sc-/startseite/verein/14390",
    "figueirense-fc/startseite/verein/4064",
    "joinville-ec/kader/verein/3330",
    "atletico-clube-goianiense/startseite/verein/15172",
    "goias-ec/startseite/verein/3197",
    "vila-nova-futebol-clube-go-/startseite/verein/5677",
    "cuiaba-ec-mt-/startseite/verein/28022",
    "luverdense-esporte-clube-mt-/startseite/verein/21599",
    "paysandu-sport-club-pa-/startseite/verein/6347",
    "clube-do-remo-pa-/startseite/verein/10997",
    "manaus-futebol-clube/startseite/verein/46022",
    "brasiliense-futebol-clube-df-/startseite/verein/3973",
    "sociedade-esportiva-do-gama-df-/startseite/verein/7014",
    "bangu-atletico-clube-rj-/startseite/verein/4745",
    "botafogo-rio-de-janeiro/startseite/verein/537",
    "flamengo-rio-de-janeiro/startseite/verein/614",
    "fluminense-rio-de-janeiro/startseite/verein/2462",
    "madureira-esporte-clube-rj-/startseite/verein/4907",
    "vasco-da-gama-rio-de-janeiro/startseite/verein/978",
    "volta-redonda-futebol-clube-rj-/startseite/verein/4176",
    "aa-ponte-preta/kader/verein/1134",
    "red-bull-bragantino/startseite/verein/8793",
    "esporte-clube-sao-bento-sp-/startseite/verein/8433",
    "esporte-clube-santo-andre-sp-/startseite/verein/7478",
    "portuguesa-sao-paulo/startseite/verein/10247",
    "aa-internacional-limeira/startseite/verein/308",
    "associacao-ferroviaria-de-esportes-sp-/startseite/verein/15882",
    "botafogo-futebol-clube-sp-/startseite/verein/9030",
    "sao-bernardo-futebol-clube-sp-/startseite/verein/16439",
    "esporte-clube-agua-santa-sp-/startseite/verein/45176",
    "ad-sao-caetano-sp-/startseite/verein/291",
    "ituano-futebol-clube-sp-/startseite/verein/4773",
    "guarani-fc-sp-/startseite/verein/1755",
    "mirassol-futebol-clube-sp-/startseite/verein/3876",
    "fc-santos/startseite/verein/221",
    "fc-sao-paulo/startseite/verein/585",
    "corinthians-sao-paulo/startseite/verein/199",
    "se-palmeiras-sao-paulo/startseite/verein/1023",
    "gremio-novorizontino-sp-/startseite/verein/37474",
    "xv-de-piracicaba/kader/verein/55335",
    "clube-atletico-juventus-sp-/startseite/verein/8144",
    "paulista-fc-sp-/kader/verein/10857/saison_id/2005/plus/1",
    # Argentina
    "club-atletico-aldosivi/startseite/verein/12301",
    "club-almagro/spielplan/verein/14977",
    "argentinos-juniors/startseite/verein/1030",
    "club-atletico-tucuman/startseite/verein/14554",
    "club-atletico-banfield/startseite/verein/830",
    "ca-belgrano/startseite/verein/2417",
    "club-atletico-boca-juniors/startseite/verein/189",
    "club-atletico-central-cordoba-sde-/startseite/verein/31284",
    "ca-chacarita-juniors/startseite/verein/2154",
    "club-atletico-colon/startseite/verein/1070",
    "defensa-y-justicia/startseite/verein/2402",
    "club-estudiantes-de-la-plata/startseite/verein/288",
    "club-ferro-carril-oeste/startseite/verein/4557",
    "club-deportivo-godoy-cruz-antonio-tomba/startseite/verein/12574",
    "club-de-gimnasia-y-esgrima-la-plata/startseite/verein/1106",
    "club-atletico-huracan/startseite/verein/2063",
    "club-atletico-independiente/startseite/verein/1234",
    "instituto-ac-cordoba/startseite/verein/1829",
    "club-atletico-lanus/startseite/verein/333",
    "club-atletico-newells-old-boys/startseite/verein/1286",
    "club-atletico-patronato/kader/verein/19806/plus/1",
    "club-atletico-platense/startseite/verein/928",
    "quilmes-atletico-club/startseite/verein/1826",
    "racing-club/startseite/verein/1444",
    "club-atletico-river-plate/startseite/verein/209",
    "club-atletico-rosario-central/startseite/verein/1418",
    "club-atletico-san-lorenzo-de-almagro/startseite/verein/1775",
    "club-atletico-sarmiento-junin-/startseite/verein/12454",
    "club-atletico-talleres/startseite/verein/3938",
    "club-atletico-tigre/startseite/verein/11831",
    "club-atletico-union/startseite/verein/7097",
    "club-atletico-velez-sarsfield/startseite/verein/1029",
    # Paraguai
    "club-cerro-porteno/startseite/verein/1214",
    "guairena-fc/startseite/verein/63181",
    "club-guarani/startseite/verein/11855",
    "club-libertad-asuncion/startseite/verein/9875",
    "club-nacional-asuncion/startseite/verein/7098",
    "olimpia-asuncion/startseite/verein/629",
    "club-sol-de-america/kader/verein/14491",
    "sportivo-ameliano/startseite/verein/95571",
    "sportivo-luqueno/startseite/verein/7656",
    "tacuary-football-club/kader/verein/6880",
    # Bolivia
    "club-aurora/spielplan/verein/12621",
    "club-always-ready/startseite/verein/42208",
    "blooming-santa-cruz/kader/verein/8056",
    "bolivar-la-paz/kader/verein/6878",
    "club-deportivo-guabira/kader/verein/17422",
    "club-jorge-wilstermann/spielplan/verein/4862",
    "ca-nacional-potosi/spielplan/verein/23171",
    "cd-oriente-petrolero/startseite/verein/6985",
    "atletico-palmaflor/kader/verein/78591",
    "club-real-santa-cruz/kader/verein/35165",
    "royal-pari-futbol-club/startseite/verein/64676",
    "the-strongest-la-paz/startseite/verein/5570",
    "universitario-de-vinto/startseite/verein/92977",
    # Chile
    "audax-italiano/kader/verein/6363",
    "deportes-cobreloa/startseite/verein/9103",
    "cd-cobresal/startseite/verein/17482",
    "csd-colo-colo/kader/verein/2433",
    "cd-everton/startseite/verein/7020",
    "cd-huachipato/kader/verein/6368",
    "magallanes-cf/kader/verein/13394",
    "cd-nublense/kader/verein/14723",
    "cd-ohiggins/kader/verein/11470",
    "cd-palestino/kader/verein/6536",
    "union-espanola/kader/verein/4321",
    "cd-union-la-calera/kader/verein/20514",
    "cd-universidad-catolica/kader/verein/3277",
    "cf-universidad-de-chile/kader/verein/1037",
    # Colombia
    "cd-america-de-cali/startseite/verein/2352",
    "atletico-bucaramanga/startseite/verein/6495",
    "atletico-nacional/startseite/verein/8172",
    "deportivo-cali/startseite/verein/9961",
    "deportivo-pereira/startseite/verein/9811",
    "junior-fc/startseite/verein/11854",
    "independiente-medellin/startseite/verein/10093",
    "independiente-santa-fe/startseite/verein/11648",
    "cd-la-equidad-seguros-sa/startseite/verein/17425",
    "millonarios-fc/startseite/verein/2350",
    "once-caldas/startseite/verein/6984",
    "deportivo-pasto/startseite/verein/10090",
    "rionegro-aguilas/startseite/verein/20590",
    "deportes-tolima/kader/verein/10503",
    # Equador
    "sd-aucas/startseite/verein/6362/saison_id/2022",
    "barcelona-sc-guayaquil/startseite/verein/3523/saison_id/2022",
    "delfin-sc/spielplan/verein/19304/saison_id/2022",
    "deportivo-cuenca/startseite/verein/8781/saison_id/2022",
    "cd-el-nacional/startseite/verein/1143/saison_id/2022",
    "cs-emelec/startseite/verein/4561/saison_id/2022",
    "guayaquil-city-fc/startseite/verein/25569/saison_id/2022",
    "independiente-del-valle/startseite/verein/19309/saison_id/2022",
    "ldu-quito/startseite/verein/9855",
    "cd-universidad-catolica/startseite/verein/17584/saison_id/2022",
    # Peru
    "carlos-a-mannucci/kader/verein/19520",
    "club-alianza-lima/startseite/verein/184",
    "club-cienciano/kader/verein/2729",
    "cusco-fc/kader/verein/28999",
    "deportivo-municipal/kader/verein/17974",
    "fbc-melgar/kader/verein/2734",
    "universidad-cesar-vallejo/kader/verein/6889",
    "sport-boys-association/kader/verein/2730",
    "club-sporting-cristal/kader/verein/1450",
    "universitario-de-deportes/kader/verein/6593",
    "universidad-tecnica-de-cajamarca/kader/verein/21170",
    # Uruguai
    "liverpool-fc-montevideo/startseite/verein/10663",
    "cerro-largo-fc/startseite/verein/20189",
    "defensor-sc/startseite/verein/2619",
    "montevideo-city-torque/startseite/verein/37535",
    "ca-boston-river/startseite/verein/18074",
    "danubio-fc/startseite/verein/1306",
    "cd-maldonado/startseite/verein/18075",
    "montevideo-wanderers/startseite/verein/2403",
    "club-nacional/startseite/verein/866",
    "ca-penarol/startseite/verein/861",
    "club-plaza-colonia/startseite/verein/6044",
    "atletico-river-plate-montevideo/startseite/verein/2419",
    # Venezuela
    "academia-puerto-cabello/startseite/verein/45193",
    "carabobo-fc/startseite/verein/14682",
    "caracas-fc/startseite/verein/531",
    "deportivo-tachira/startseite/verein/13297",
    "estudiantes-de-merida/startseite/verein/14555",
    "metropolitanos-fc/startseite/verein/42918",
    "monagas-sc/startseite/verein/14596",
    "deportivo-la-guaira/startseite/verein/26468",
    "dvo-rayo-zuliano/startseite/verein/93338",
    "portuguesa-fc/startseite/verein/22918",
    "universidad-central-de-venezuela/startseite/verein/43146",
    "zamora-futbol-club/startseite/verein/18018",
]

list_concacaf = [
    "ld-alajuelense/startseite/verein/6478",
    "deportivo-saprissa/startseite/verein/4720",
    # Guatemala
    "comunicaciones-fc/startseite/verein/9709",
    "csd-municipal/startseite/verein/13047",
    # Haiti
    "violette-athletic-club/startseite/verein/14182",
    # Honduras
    "cd-olimpia/startseite/verein/2720",
    "cd-motagua-tegucigalpa/startseite/verein/9708",
    "rcd-espana-san-pedro-sula/kader/verein/13293/saison_id/2022",
]

list_asia = [
    "beijing-sinobo-guoan/startseite/verein/3176",
    "shandong-taishan/startseite/verein/3182",
    "shanghai-port/startseite/verein/27190",
    "shanghai-shenhua/startseite/verein/3183",
    "wuhan-three-towns/startseite/verein/70657",
    "zhejiang-fc/startseite/verein/17276",
    "buriram-united/startseite/verein/25449",
    # Bahrein
    "al-muharraq-sc/startseite/verein/8546",
    # Qatar
    "al-arabi-sc/startseite/verein/1230/saison_id/2022",
    "al-duhail-sc/startseite/verein/26091/saison_id/2022",
    "al-gharafa-sc/startseite/verein/6297/saison_id/2022",
    "al-sadd-sc/startseite/verein/656",
    "qatar-sc/startseite/verein/965/saison_id/2022",
    # EAU
    "al-ain-fc/startseite/verein/2150/saison_id/2022",
    "al-jazira-abu-dhabi-/startseite/verein/2524",
    "al-wahda-fc-abu-dhabi/startseite/verein/161/saison_id/2022",
    "fc-shabab-al-ahli-dubai/startseite/verein/60529/saison_id/2022",
    "sharjah-cultural-sports-club/startseite/verein/13613/saison_id/2022",
    # Irã
    "esteghlal-fc/startseite/verein/1076",
    "persepolis-fc/startseite/verein/6079",
    # Iraque
    "al-shorta-sc/startseite/verein/13593/saison_id/2021",
    "al-zawraa-sc/startseite/verein/23806/saison_id/2016",
]

list_oceania = [
    "auckland-city-fc/startseite/verein/11391",
]

list_africa = [
    # Argelia
    "cr-belouizdad/startseite/verein/13365",
    "cs-constantine/kader/verein/30685",
    "es-setif/startseite/verein/18272",
    "mc-algier/startseite/verein/8850",
    "usm-algier/startseite/verein/6772",
    # Egito
    "zamalek-sc/startseite/verein/664",
    "el-ahly-kairo/startseite/verein/7",
    # Marrocos
    "far-rabat/startseite/verein/9099",
    "raja-casablanca/startseite/verein/2068",
    "wydad-casablanca/startseite/verein/6603",
    # Sudao
    "al-hilal-omdurman/startseite/verein/8430",
    "al-merreikh-omdurman/startseite/verein/10721",
    # Tunisia
    "club-africain-tunis/startseite/verein/819",
    "esperance-tunis/startseite/verein/3342",
    "etoile-sportive-du-sahel/startseite/verein/250",
    "club-sportif-sfaxien/startseite/verein/581",
    # Africa do sul
    "cape-town-city-fc/startseite/verein/2303",
    "kaizer-chiefs/startseite/verein/568",
    "mamelodi-sundowns-fc/startseite/verein/6356",
    "orlando-pirates/startseite/verein/2557",
    # Angola
    "ca-petroleos-luanda/startseite/verein/7084",
    "cd-1-ordm-de-agosto/startseite/verein/14503",
    # Camaroes
    "cotonsport-de-garoua/startseite/verein/4675",
    # Costa do Marfim
    "asec-mimosas/startseite/verein/3891",
    # Congo
    "tp-mazembe/startseite/verein/8428",
    "as-vita-club-kinshasa/startseite/verein/2225",
    # Nigéria
    "enyimba-aba/startseite/verein/645",
    # Tanzania
    "simba-sc/startseite/verein/14191",
]

my_list = list_america + list_concacaf + list_africa + list_asia + list_oceania


def run_transf_one_club(search):
    clubID = [x for x in my_list if search in x]
    transfermarkt(clubID[0])


def run_transf_all():
    for clubID in my_list[1:]:
        pass
        transfermarkt(clubID)


model_path = "functions/model.pkl"
run_transf_one_club("constantine")
# run_transf_all()
