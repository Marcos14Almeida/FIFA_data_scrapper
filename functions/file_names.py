# -*- coding:utf-8 -*-
"""
Created on Mon Mar 28 16:09:17 2022

@author:marcos
"""
from functions.get_list_players import getListPlayers

"""
ANTIGAMENTE - MAXIMO DE 18 TIMES POR ARQUIVO,
PARA O CSV NÃO TER MUITAS COLUNAS E DAR OVERFLOW
"""


# %%


def Inglaterra():
    list = [
        "https://sofifa.com/team/5/chelsea/",
        "https://sofifa.com/team/10/manchester-city/",
        "https://sofifa.com/team/11/manchester-united/",
        "https://sofifa.com/team/1/arsenal/",
        "https://sofifa.com/team/9/liverpool/",
        "https://sofifa.com/team/18/tottenham-hotspur/",
        "https://sofifa.com/team/7/everton/",
        "https://sofifa.com/team/95/leicester-city/",
        "https://sofifa.com/team/8/leeds-united/",
        "https://sofifa.com/team/19/west-ham-united/",
        "https://sofifa.com/team/13/newcastle-united/",
        "https://sofifa.com/team/17/southampton/",
        "https://sofifa.com/team/2/aston-villa/",
        "https://sofifa.com/team/110/wolverhampton-wanderers/",
        "https://sofifa.com/team/1799/crystal-palace/",
        "https://sofifa.com/team/109/west-bromwich-albion/",
    ]
    return getListPlayers(list)


# %%


def Inglaterra2():
    list = [
        "https://sofifa.com/team/88/birmingham-city/",
        "https://sofifa.com/team/3/blackburn-rovers/",
        "https://sofifa.com/team/1943/afc-bournemouth/",
        "https://sofifa.com/team/1796/burnley/",
        "https://sofifa.com/team/1808/brighton-hove-albion/",
        "https://sofifa.com/team/91/derby-county/",
        "https://sofifa.com/team/144/fulham/",
        "https://sofifa.com/team/12/middlesbrough/",
        "https://sofifa.com/team/1792/norwich-city/",
        "https://sofifa.com/team/14/nottingham-forest/",
        "https://sofifa.com/team/15/queens-park-rangers/",
        "https://sofifa.com/team/1793/reading/",
        "https://sofifa.com/team/1794/sheffield-united/",
        "https://sofifa.com/team/1806/stoke-city/",
        "https://sofifa.com/team/1960/swansea-city/",
        "https://sofifa.com/team/1795/watford/",
    ]

    return getListPlayers(list)


# %%


def Inglaterra3():
    list = [
        "https://sofifa.com/team/1932/barnsley/",
        "https://sofifa.com/team/1919/bristol-city/",
        "https://sofifa.com/team/1926/blackpool/",
        "https://sofifa.com/team/1925/brentford/",
        "https://sofifa.com/team/4/bolton-wanderers/",
        "https://sofifa.com/team/1961/cardiff-city/",
        "https://sofifa.com/team/1800/coventry-city/",
        "https://sofifa.com/team/89/charlton-athletic/",
        "https://sofifa.com/team/1952/hull-city/",
        "https://sofifa.com/team/1939/huddersfield-town/",
        "https://sofifa.com/team/1802/gillingham/",
        "https://sofifa.com/team/94/ipswich-town/",
        "https://sofifa.com/team/1923/luton-town/",
        "https://sofifa.com/team/97/millwall/",
        "https://sofifa.com/team/1798/milton-keynes-dons/",
        "https://sofifa.com/team/1951/oxford-united/",
    ]

    return getListPlayers(list)


# %%


def Inglaterra4():
    list = [
        "https://sofifa.com/team/1938/peterborough-united/",
        "https://sofifa.com/team/1929/plymouth-argyle/",
        "https://sofifa.com/team/1790/portsmouth/",
        "https://sofifa.com/team/1801/preston-north-end/",
        "https://sofifa.com/team/1807/sheffield-wednesday/",
        "https://sofifa.com/team/127/shrewsbury-town/",
        "https://sofifa.com/team/106/sunderland/",
        "https://sofifa.com/team/1797/rotherham-united/",
        "https://sofifa.com/team/1917/wigan-athletic/",
        "https://sofifa.com/team/1933/wycombe-wanderers/",
        "https://sofifa.com/team/112259/afc-wimbledon/",
    ]

    return getListPlayers(list)


# %%


def Espanha():
    list = [
        "https://sofifa.com/team/241/fc-barcelona/",
        "https://sofifa.com/team/243/real-madrid/",
        "https://sofifa.com/team/240/atletico-madrid/",
        "https://sofifa.com/team/481/sevilla-fc/",
        "https://sofifa.com/team/449/real-betis/",
        "https://sofifa.com/team/461/valencia-cf/",
        "https://sofifa.com/team/483/villarreal-cf/",
        "https://sofifa.com/team/448/athletic-club-de-bilbao/",
        "https://sofifa.com/team/457/real-sociedad/",
        "https://sofifa.com/team/1860/getafe-cf/",
        "https://sofifa.com/team/450/rc-celta-de-vigo/",
        "https://sofifa.com/team/452/espanyol/",
        "https://sofifa.com/team/1853/levante-union-deportiva/",
        "https://sofifa.com/team/479/ca-osasuna/",
        "https://sofifa.com/team/462/real-valladolid-cf/",
        "https://sofifa.com/team/453/rcd-mallorca/",
    ]

    return getListPlayers(list)


# %%


def Espanha2():
    list = [
        "https://sofifa.com/team/1861/union-deportiva-almeria/",
        "https://sofifa.com/team/10846/burgos-cf/",
        "https://sofifa.com/team/1968/cadiz-cf/",
        "https://sofifa.com/team/463/deportivo-alaves/",
        "https://sofifa.com/team/467/sd-eibar/",
        "https://sofifa.com/team/468/elche-cf/",
        "https://sofifa.com/team/110832/granada-cf/",
        "https://sofifa.com/team/113981/ud-ibiza/",
        "https://sofifa.com/team/472/union-deportiva-las-palmas/",
        "https://sofifa.com/team/110062/girona-fc/",
        "https://sofifa.com/team/100888/cd-leganes/",
        "https://sofifa.com/team/100831/ad-alcorcon/",  # -> LA CORUNA
        "https://sofifa.com/team/573/malaga-cf/",
        "https://sofifa.com/team/480/rayo-vallecano/",
        "https://sofifa.com/team/110827/real-oviedo/",
        "https://sofifa.com/team/459/real-sporting-de-gijon/",
        "https://sofifa.com/team/260/cd-tenerife/",
        "https://sofifa.com/team/244/real-zaragoza/",
    ]
    return getListPlayers(list)


# %%


def Italia():
    list = [
        "https://sofifa.com/team/45/juventus/",
        "https://sofifa.com/team/44/inter/",
        "https://sofifa.com/team/48/napoli/",
        "https://sofifa.com/team/46/lazio/",
        "https://sofifa.com/team/47/milan/",
        "https://sofifa.com/team/52/roma/",
        "https://sofifa.com/team/39/atalanta/",
        "https://sofifa.com/team/189/bologna/",
        "https://sofifa.com/team/1842/cagliari/",
        "https://sofifa.com/team/110374/fiorentina/",
        "https://sofifa.com/team/110556/genoa/",
        "https://sofifa.com/team/1837/uc-sampdoria/",
        "https://sofifa.com/team/111974/us-sassuolo-calcio/",
        "https://sofifa.com/team/54/torino-fc/",
        "https://sofifa.com/team/55/udinese-calcio/",
    ]

    return getListPlayers(list)


# %%


def Italia2():
    list = [
        "https://sofifa.com/team/1847/ascoli/",
        "https://sofifa.com/team/1848/bari-1908/",
        "https://sofifa.com/team/112026/benevento/",
        "https://sofifa.com/team/190/brescia/",
        "https://sofifa.com/team/1745/como/",
        "https://sofifa.com/team/112168/cosenza/",
        "https://sofifa.com/team/111434/cremonese/",
        "https://sofifa.com/team/110734/crotone/",
        "https://sofifa.com/team/1746/empoli/",
        "https://sofifa.com/team/111657/frosinone/",
        "https://sofifa.com/team/206/hellas-verona/",
        "https://sofifa.com/team/347/lecce/",
        "https://sofifa.com/team/1744/modena/",
        "https://sofifa.com/team/111811/ac-monza/",
        "https://sofifa.com/team/1843/palermo/",
        "https://sofifa.com/team/50/parma/",
        "https://sofifa.com/team/199/perugia/",
        "https://sofifa.com/team/110738/pisa/",
        "https://sofifa.com/team/203/reggina/",
        "https://sofifa.com/team/110373/us-salernitana-1919/",
        "https://sofifa.com/team/112791/spal/",
        "https://sofifa.com/team/110741/spezia/",
        "https://sofifa.com/team/112494/sudtirol/",
        "https://sofifa.com/team/570/ternana/",
        "https://sofifa.com/team/205/venezia-fc/",
        "1586",  # Alessandria
        "3354",  # Podernone
        "134",  # Vicenza
        # "95",  # Ascoli
        # "97",  # Bari
        # "99",  # Brescia
        # "1671",  # Como
        # "1582",  # Cosenza
        # "479",  # Cremonese
        # "858",  # Frosinone
        # "117",  # Palermo
        # "119",  # Perugia
        # "872",  # Pisa
        # "122",  # Reggina
        # "1467",  # SPAL
        # "127",  # Ternana
    ]
    return getListPlayers(list)


# %%


def Alemanha():
    list = [
        "https://sofifa.com/team/21/fc-bayern-munchen/",
        "https://sofifa.com/team/22/borussia-dortmund/",
        "https://sofifa.com/team/112172/rb-leipzig/",
        "https://sofifa.com/team/32/bayer-04-leverkusen/",
        "https://sofifa.com/team/23/borussia-monchengladbach/",
        "https://sofifa.com/team/1824/eintracht-frankfurt/",
        "https://sofifa.com/team/10029/tsg-hoffenheim/",
        "https://sofifa.com/team/175/vfl-wolfsburg/",
        "https://sofifa.com/team/166/hertha-bsc/",
        "https://sofifa.com/team/31/1-fc-koln/",
        "https://sofifa.com/team/36/vfb-stuttgart/",
        "https://sofifa.com/team/100409/fc-augsburg/",
        "https://sofifa.com/team/38/sv-werder-bremen/",
        "https://sofifa.com/team/28/hamburger-sv/",
        "https://sofifa.com/team/34/fc-schalke-04/",
        "https://sofifa.com/team/25/sport-club-freiburg/",
    ]
    return getListPlayers(list)


# %%


def Alemanha2():
    list = [
        "https://sofifa.com/team/159/dsc-arminia-bielefeld/",
        "https://sofifa.com/team/160/vfl-bochum-1848/",
        "https://sofifa.com/team/110502/sv-darmstadt-98/",
        "https://sofifa.com/team/503/sg-dynamo-dresden/",
        "https://sofifa.com/team/110636/fortuna-dusseldorf/",
        "https://sofifa.com/team/165/spvgg-greuther-furth/",
        "https://sofifa.com/team/27/fc-hansa-rostock/",
        "https://sofifa.com/team/485/hannover-96/",
        "https://sofifa.com/team/1832/karlsruher-sc/",
        "https://sofifa.com/team/29/1-fc-kaiserslautern/",
        "https://sofifa.com/team/169/1-fsv-mainz-05/",
        "https://sofifa.com/team/171/1-fc-nurnberg/",
        "https://sofifa.com/team/10030/sc-paderborn-07/",
        "https://sofifa.com/team/110329/fc-st-pauli/",
        "https://sofifa.com/team/1831/1-fc-union-berlin/",
        "https://sofifa.com/team/33/tsv-1860-munchen/",
    ]
    return getListPlayers(list)


# %%


def Alemanha3():
    list = [
        "https://sofifa.com/team/111235/1-fc-heidenheim-1846/",
        "https://sofifa.com/team/543/ssv-jahn-regensburg/",
        "https://sofifa.com/team/1825/msv-duisburg/",
        "https://sofifa.com/team/110500/eintracht-braunschweig/",
        "https://sofifa.com/team/523/1-fc-saarbrucken/",
    ]
    return getListPlayers(list)


# %%


def França():
    list = [
        "https://sofifa.com/team/73/paris-saint-germain/",
        "https://sofifa.com/team/66/olympique-lyonnais/",
        "https://sofifa.com/team/219/olympique-de-marseille/",
        "https://sofifa.com/team/69/as-monaco/",
        "https://sofifa.com/team/65/losc-lille/",
        "https://sofifa.com/team/72/ogc-nice/",
        "https://sofifa.com/team/74/stade-rennais-fc/",
        "https://sofifa.com/team/70/montpellier-herault-sc/",
        "https://sofifa.com/team/1819/as-saint-etienne/",
        "https://sofifa.com/team/59/fc-girondins-de-bordeaux/",
        "https://sofifa.com/team/71/fc-nantes/",
        "https://sofifa.com/team/379/stade-de-reims/",
        "https://sofifa.com/team/68/fc-metz/",
        "https://sofifa.com/team/64/racing-club-de-lens/",
        "https://sofifa.com/team/76/rc-strasbourg-alsace/",
        "https://sofifa.com/team/111817/paris-fc/",
    ]
    return getListPlayers(list)


# %%


def França2():
    list = [
        "https://sofifa.com/team/614/ac-ajaccio/",
        "https://sofifa.com/team/1530/angers-sco/",
        "https://sofifa.com/team/1816/amiens-sc/",
        "https://sofifa.com/team/57/aj-auxerre/",
        "https://sofifa.com/team/378/stade-brestois-29/",
        "https://sofifa.com/team/210/stade-malherbe-caen/",
        "https://sofifa.com/team/1815/clermont-foot-63/",
        "https://sofifa.com/team/110569/dijon-fco/",
        "https://sofifa.com/team/62/en-avant-de-guingamp/",
        "https://sofifa.com/team/217/fc-lorient/",
        "https://sofifa.com/team/1823/as-nancy-lorraine/",
        "https://sofifa.com/team/1738/le-havre-ac/",
        "https://sofifa.com/team/1805/grenoble-foot-38/",
        "https://sofifa.com/team/226/fc-sochaux-montbeliard/",
        "https://sofifa.com/team/294/estac-troyes/",
    ]

    return getListPlayers(list)


# %%


def França3():
    list = [
        "https://sofifa.com/team/1809/toulouse-football-club/",
        "https://sofifa.com/team/110456/valenciennes-fc/",
        "https://sofifa.com/team/58/sc-bastia/",
        "https://sofifa.com/team/224/nimes-olympique/",
    ]
    return getListPlayers(list)


# %%


def Portugal():
    list = [
        "214",  # Coimbra
        "234",  # Nacional PT
        "217",  # Belenenses SAD
        "https://sofifa.com/team/234/sl-benfica/",
        "https://sofifa.com/team/237/sporting-cp/",
        "https://sofifa.com/team/236/fc-porto/",
        "https://sofifa.com/team/1896/sc-braga/",
        "https://sofifa.com/team/1898/boavista-fc/",
        "https://sofifa.com/team/114510/casa-pia/",
        "https://sofifa.com/team/518/chaves/",
        "https://sofifa.com/team/10020/estoril-praia/",
        "https://sofifa.com/team/112809/futebol-clube-de-famalicao/",
        "https://sofifa.com/team/1888/gil-vicente-fc/",
        "https://sofifa.com/team/1893/clube-sport-maritimo/",
        "https://sofifa.com/team/1900/moreirense-fc/",
        "https://sofifa.com/team/1892/fc-pacos-de-ferreira/",
        "https://sofifa.com/team/10031/portimonense-sc/",
        "https://sofifa.com/team/1438/santa-clara/",
        "https://sofifa.com/team/744/rio-ave/",
        "https://sofifa.com/team/1887/vitoria-de-guimaraes/",
        "https://sofifa.com/team/111539/vizela/",
        # "241",  # Rio Ave
    ]
    return getListPlayers(list)


# %%


def Holanda():
    list = [
        "https://sofifa.com/team/245/ajax/",
        "https://sofifa.com/team/247/psv/",
        "https://sofifa.com/team/246/feyenoord/",
        "https://sofifa.com/team/1906/az-alkmaar/",
        "https://sofifa.com/team/1908/fc-twente/",
        "https://sofifa.com/team/1909/vitesse/",
        "https://sofifa.com/team/1903/fc-utrecht/",
        "https://sofifa.com/team/1913/sc-heerenveen/",
        "https://sofifa.com/team/1915/fc-groningen/",
        "https://sofifa.com/team/100646/sparta-rotterdam/",
    ]

    return getListPlayers(list)


# %%


def Belgica():
    list = [
        "https://sofifa.com/team/673/krc-genk/",
        "https://sofifa.com/team/231/club-brugge/",
        "https://sofifa.com/team/232/standard-de-liege/",
        "https://sofifa.com/team/229/anderlecht/",
        "https://sofifa.com/team/674/kaa-gent/",  # Gent
        "https://sofifa.com/team/230/royal-antwerp-fc/",
        "https://sofifa.com/team/110724/mechelen/",
        "https://sofifa.com/team/670/sporting-charleroi/",
        "https://sofifa.com/team/2014/union-saint-gilloise/",
    ]

    return getListPlayers(list)


# %%


def EuropaOcidental():
    list = [
        # SUIÇA
        "https://sofifa.com/team/896/fc-basel-1893/",
        "https://sofifa.com/team/900/bsc-young-boys/",
        "https://sofifa.com/team/894/fc-zurich/",
        "https://sofifa.com/team/10032/fc-lugano/",
        "https://sofifa.com/team/322/grasshopper-club-zurich/",
        "https://sofifa.com/team/897/fc-luzern/",
        # AUSTRIA
        "https://sofifa.com/team/191/fc-red-bull-salzburg/",
        "https://sofifa.com/team/252/lask-linz/",
        "https://sofifa.com/team/254/sk-rapid-wien/",
        "https://sofifa.com/team/209/sk-sturm-graz/",
        "https://sofifa.com/team/256/fk-austria-wien/",
    ]

    return getListPlayers(list)


# %%


def EuropaOcidental2():
    list = [
        # ESCÓCIA
        "https://sofifa.com/team/78/celtic/",
        "https://sofifa.com/team/86/rangers-fc/",
        "https://sofifa.com/team/77/aberdeen/",
        "https://sofifa.com/team/181/dundee-united/",
        "https://sofifa.com/team/80/hearts/",
        "https://sofifa.com/team/81/hibernian/",
        # POLONIA
        "https://sofifa.com/team/110747/cracovia/",
        "https://sofifa.com/team/420/gornik-zabrze/",
        "https://sofifa.com/team/1871/legia-warszawa/",
        "https://sofifa.com/team/873/lech-poznan/",
        "https://sofifa.com/team/110746/pogon-szczecin/",
        "https://sofifa.com/team/114326/rakow-czestochowa/",
    ]

    return getListPlayers(list)


# %%


def Nordicos():
    list = [
        # NORUEGA
        "https://sofifa.com/team/298/rosenborg-bk/",
        "https://sofifa.com/team/417/molde-fk/",  # molde
        "https://sofifa.com/team/918/fk-bodoglimt/",  # Bodø/Glimt
        # SUÉCIA
        "https://sofifa.com/team/433/aik/",
        "https://sofifa.com/team/700/if-elfsborg/",
        "https://sofifa.com/team/708/hammarby-if/",
        "https://sofifa.com/team/319/ifk-goteborg/",
        "https://sofifa.com/team/320/malmo-ff/",
        # DINAMARCA
        "https://sofifa.com/team/820/aalborg-bk/",
        "https://sofifa.com/team/269/brondby-if/",
        "https://sofifa.com/team/819/fc-kobenhavn/",
        "https://sofifa.com/team/1516/fc-midtjylland/",
        "https://sofifa.com/team/1788/nordsjaelland/",
        "https://sofifa.com/team/272/odense-boldklub/",
        "https://sofifa.com/team/1786/randers-fc/",
        # FINLANDIA
        "https://sofifa.com/team/100325/hjk-helsinki/",
    ]

    return getListPlayers(list)


# %%


def TurquiaGrecia():
    list = [
        # TURQUIA
        "https://sofifa.com/team/327/besiktas/",
        "https://sofifa.com/team/326/fenerbahce/",
        "https://sofifa.com/team/325/galatasaray/",
        "https://sofifa.com/team/436/trabzonspor/",
        "https://sofifa.com/team/101014/istanbul-basaksehir/",
        "https://sofifa.com/team/101041/sivasspor/",
        "https://sofifa.com/team/741/antalyaspor/",
        # "351",  # Galatasaray
        # "349",  # Besiktas
        # "350",  # Fenerbahce
        # GRECIA
        "https://sofifa.com/team/393/paok/",
        "https://sofifa.com/team/278/aek-athens/",
        "https://sofifa.com/team/1884/panathinaikos-fc/",
        "373",  # Olympiakos
        "762",  # Aris
        # CHIPRE
        "834",  # AEK Larnaca
        "928",  # Apollon Limassol
        "764",  # Omonoia Nicosia
        "https://sofifa.com/team/100135/apoel/",
        # "719",  # Apoel
    ]

    return getListPlayers(list)


# %%


def URSS():
    list = [
        "265",  # Zenit
        "263",  # Spartak
        "254",  # CSKA
        "1673",  # Krasnodar
        "258",  # Lokomotiv Moskva
        "255",  # Dinamo Moscou
        "260",  # Rubin Kazan
        "4605",  # Sochi
        "348",  # Shaktar
        "347",  # Dinamo Kiev
        "5119",  # Dnipro
        "609",  # Metalist
        "1395",  # Sheriff Tiraspol
        "1105",  # BATE
        "1508",  # Astana
        "1539",  # Qarabag
    ]

    return getListPlayers(list)


# %%


def LesteEuropeu():
    list = [
        # CROACIA
        # "365",  # D. Zagreb
        "https://sofifa.com/team/211/dinamo-zagreb/",
        "https://sofifa.com/team/263/hajduk-split/",
        "941",  # Rijeka
        # ROMENIA
        "379",  # FCSB - Steaua Bucaresti
        "https://sofifa.com/team/110816/cfr-cluj/",
        # "https://sofifa.com/team/100761/fcsb-steaua/",
        # REP.TCHECA
        # "369",  # Sparta Praga
        "https://sofifa.com/team/267/sparta-praha/",
        "https://sofifa.com/team/266/sk-slavia-praha/",
        "https://sofifa.com/team/110468/viktoria-plzen/",
        # HUNGRIA
        "1416",  # Ferencvaros
        "1023",  # Honved
        "2592",  # Puskas
        "1014",  # Ujpest
        # BULGARIA
        "1763",  # Ludogorets
        "360",  # CSKA Sofia
        # SERVIA
        "381",  # Partizan
        "380",  # Estrela Vermelha
    ]

    return getListPlayers(list)


def EuropaOutros():
    list = [
        "1166",  # Maribor
        "1062",  # Vardar
        "807",  # Slovan Bratislava
        "605",  # Maccabi Tel-Aviv
        "474",  # Maccabi Haifa
        "1577",  # Hapoel Beer Sheva
        "1119",  # Dinamo Minsk
        "722",  # Zrinjski-BOS
    ]

    return getListPlayers(list)


###################################################
###################################################
###################################################
# %%


def Brasil():
    list = [
        "300",  # Palmeiras
        "290",  # Corinthians
        "306",  # SP
        "304",  # Santos
        "286",  # Atl-MG
        "298",  # Internacional
        "294",  # Flamengo
        "288",  # Botafogo
        "295",  # Fluminense
        "287",  # Atl-PR
        "291",  # Coritiba
        "296",  # Fortaleza
        "1458",  # Ceará
        "1447",  # RB Bragantino
        "1581",  # Atl-GO
        "297",  # Goias
    ]

    return getListPlayers(list)


# %%


def Brasil2():
    list = [
        "602",  # Grêmio
        "1614",  # América-MG
        "1473",  # Bahia
        "2379",  # Chape
        "2416",  # Cuiaba
        "1772",  # Criciuma
        "292",  # Cruzeiro
        "293",  # Figueirense
        "1515",  # Guarani
        "299",  # Juventude
        "922",  # Naútico
        "301",  # Paraná
        "303",  # Ponte Preta
        "923",  # Sport
        "307",  # Vasco
        "1457",  # Vila Nova
    ]

    return getListPlayers(list)


# %%


def Brasil3():
    list = [
        "2455",  # Ituano
        "3481",  # Novorizontino
        "2813",  # Mirassol
        "1785",  # ABC
        "2814",  # CSA
        "2015",  # CRB
        "5536",  # Manaus
        "603",  # Santa Cruz
        "2395",  # Sampaio Corrêa
        "1414",  # Avaí
        "2881",  # Londrina
        "2478",  # Brasil de Pelotas
        "2476",  # Remo
        "302",  # Paysandu
        "3005",  # Tombense
        "1237",  # Vitória
    ]

    return getListPlayers(list)


# %%


def Brasil4():
    list = [
        "3017",  # Botafogo-PB
        "2396",  # Campinense
        "3067",  # Ibis = Juazeirense
        "3506",  # Confiança
        "2396",  # Campinense
        "4314",  # River-PI
        "289",  # Brasiliense
        "3485",  # Gama
        "2063",  # Joinville
        "2014",  # Caxias do Sul
        "4483",  # Brusque
        "2848",  # Operário
        "2815",  # Bangu
        "2378",  # Madureira
        "2475",  # Volta Redonda
        "3503",  # Agua Santa
        "2802",  # Botafogo-SP
        "3426",  # Ferroviária
        "3245",  # Inter Limeira
        "3062",  # Juventus Mooca
        "2813",  # Mirassol
        "1232",  # Portuguesa
        "3042",  # Paulista Jundiai = Monte Azul
        "3547",  # Sao Bento
        "305",  # São Caetano
        "1419",  # Santo André
        "3035",  # XV de Piracicaba
    ]

    return getListPlayers(list)


# %%


def Argentina():
    list = [
        "https://sofifa.com/team/1876/river-plate/",
        "https://sofifa.com/team/1877/boca-juniors/",
        "https://sofifa.com/team/110406/club-atletico-colon/",
        "https://sofifa.com/team/101085/racing-club/",
        "https://sofifa.com/team/110093/club-atletico-independiente/",
        "https://sofifa.com/team/101088/velez-sarsfield/",
        "https://sofifa.com/team/110395/club-atletico-lanus/",
        "https://sofifa.com/team/101083/estudiantes-de-la-plata/",
        "https://sofifa.com/team/110580/rosario-central/",
        "https://sofifa.com/team/1013/san-lorenzo-de-almagro/",
        "https://sofifa.com/team/110396/newells-old-boys/",
        "https://sofifa.com/team/111019/argentinos-juniors/",
        "https://sofifa.com/team/112670/club-atletico-talleres/",
        "https://sofifa.com/team/110394/arsenal-de-sarandi/",
        "https://sofifa.com/team/110404/club-atletico-banfield/",
        "https://sofifa.com/team/111710/defensa-y-justicia/",
    ]
    return getListPlayers(list)


# %%


def Argentina2():
    list = [
        "https://sofifa.com/team/111711/club-atletico-huracan/",  # Huracan
        "https://sofifa.com/team/111706/godoy-cruz/",
        "https://sofifa.com/team/111708/atletico-tucuman/",
        "https://sofifa.com/team/101084/gimnasia-y-esgrima-la-plata/",
        "https://sofifa.com/team/111716/union-de-santa-fe/",
        "https://sofifa.com/team/112689/platense/",
        "https://sofifa.com/team/111707/club-atletico-aldosivi/",
        "https://sofifa.com/team/112965/club-atletico-central-cordoba/",
        "https://sofifa.com/team/110581/patronato/",
        "https://sofifa.com/team/112713/sarmiento/",
        "https://sofifa.com/team/113044/barracas-central/",
        "https://sofifa.com/team/111715/tigre/",
        "720",  # Belgrano
        # "280",  # Quilmes
        # "1358",  # Chacarita Juniors
        # "1193",  # Tigre
    ]

    return getListPlayers(list)


# %%


def UruguaiParaguai():
    list = [
        # URUGUAI
        "https://sofifa.com/team/101110/penarol/",
        "https://sofifa.com/team/111325/nacional/",
        "https://sofifa.com/team/111325/nacional/",
        "https://sofifa.com/team/111001/wanderers/",
        "https://sofifa.com/team/111326/liverpool/",
        "623",  # Danubio
        "624",  # Defensor
        "2409",  # Montevideo City Torque
        # "376",  # Penarol
        # "375",  # Nacional-URU
        # "2409",  # Montevideo Wanderers
        # "1011",  # River Plate-URU
        # PARAGUAI
        "https://sofifa.com/team/112716/cerro-porteno/",
        "https://sofifa.com/team/111008/libertad/",
        "https://sofifa.com/team/101108/olimpia/",
        "https://sofifa.com/team/112671/nacional-asuncion/",  # Nacional -PAR
        "https://sofifa.com/team/101108/olimpia/",
        "https://sofifa.com/team/114688/guairena/",
        "617",  # Club Guaraní
        # "613",  # Olimpia
        # "615",  # Cerro
        # "616",  # Libertad
    ]

    return getListPlayers(list)


def Chile():
    list = [
        # "362",  # colo-colo
        # "363",  # Catolica
        # "978",  # Union Espanola
        # "https://sofifa.com/team/111328/club-deportivo-palestino/",
        # "https://sofifa.com/team/111327/cd-huachipato/",
        "https://sofifa.com/team/110975/universidad-catolica/",
        "https://sofifa.com/team/110980/colo-colo/",
        "https://sofifa.com/team/110977/union-espanola/",
        "https://sofifa.com/team/112535/union-la-calera/",
        "364",  # laU
        "974",  # Everton-CHI
        "925",  # Cobreloa
        "975",  # Huachipato
        "976",  # Palestino
        # "362",  # colo-colo
        # "363",  # Catolica
        # "978",  # Union Espanola
        # "https://sofifa.com/team/111328/club-deportivo-palestino/",
        # "https://sofifa.com/team/111327/cd-huachipato/",
    ]

    return getListPlayers(list)


# %%


def PeruBolivia():
    list = [
        # PERU
        "622",  # Universitario
        "https://sofifa.com/team/111010/alianza-lima/",
        "https://sofifa.com/team/111013/sporting-cristal/",
        "https://sofifa.com/team/111011/cienciano/",
        "https://sofifa.com/team/110974/club-deportivo-jorge-wilstermann/",
        "https://sofifa.com/team/111334/fbc-melgar/",
        "https://sofifa.com/team/111016/sport-boys/",
        # "896",  # Cienciano
        # "509",  # Sporting Cristal
        # "621",  # Alianza Lima
        # "https://sofifa.com/team/111014/club-universitario-de-deportes/",
        # BOLIVIA
        "1238",  # Bolivar
        "https://sofifa.com/team/110969/club-the-strongest/",
        "https://sofifa.com/team/114577/club-always-ready/",
        "https://sofifa.com/team/114600/guabira/",
        "https://sofifa.com/team/110970/oriente-petrolero/",
        "https://sofifa.com/team/115517/independiente-petrolero/",
        "https://sofifa.com/team/114579/royal-pari/",
        "https://sofifa.com/team/110974/wilstermann/",
        "1356",  # Blooming
        # "5728",  # Independiente petrolero
        # "1407",  # Oriente Petrolero
        # "1486",  # Universitario de Sucre
    ]

    return getListPlayers(list)


# %%


def Colombia():
    list = [
        # "620",  # América de Cali
        # "912",  # Atlético Nacional
        # "906",  # Deportivo Cali
        # "853",  # Junior
        # "911",  # DIM
        "619",  # Once Caldas
        "618",  # Millonarios
        "916",  # Santa fé
        # "917",  # Tolima
        "https://sofifa.com/team/101099/america-de-cali/",
        "https://sofifa.com/team/101100/atletico-nacional/",
        "https://sofifa.com/team/101103/independiente-medellin/",
        "https://sofifa.com/team/101102/deportivo-cali/",
        "https://sofifa.com/team/101101/junior/",
        "https://sofifa.com/team/112523/la-equidad/",
        "https://sofifa.com/team/111722/deportes-tolima/",
    ]

    return getListPlayers(list)


# %%


def EquadorVenezuela():
    list = [
        # EQUADOR
        # "658",  # Barcelona-EQU
        # "886",  # Emelec
        # "1562",  # I. Del Valle
        # "656",  # LDU
        # "1359",  # Univ. Católica Ecuador
        "660",  # Aucas
        "885",  # Deportivo Cuenca
        "2547",  # Guayaquil City
        "657",  # El Nacional
        "https://sofifa.com/team/112908/independiente-del-valle/",
        "https://sofifa.com/team/110986/ldu-quito/",
        "https://sofifa.com/team/110984/emelec/",
        "https://sofifa.com/team/114581/universidad-catolica/",
        "https://sofifa.com/team/110981/barcelona-guayaquil/",
        # VENEZUELA
        # "1211",  # Caracas
        "https://sofifa.com/team/110989/caracas/",
        "https://sofifa.com/team/110990/deportivo-tachira-fc/",
        "https://sofifa.com/team/112853/deportivo-la-guaira-fc/",
        "https://sofifa.com/team/111332/estudiantes-de-merida/",
        "https://sofifa.com/team/112914/metropolitanos-de-caracas-fc/",
        "1214",  # Monagas
        "1263",  # Zamora
    ]

    return getListPlayers(list)


###################################################
###################################################
###################################################
# %%


def Mexico():
    list = [
        "439",  # América
        "444",  # Chivas
        "443",  # Cruz Azul
        "445",  # Monterrey
        "447",  # Pachuca
        "453",  # Pumas
        "450",  # Tigres
        "451",  # Toluca
        "441",  # Atlas
        "3877",  # Juarez
        "1421",  # León
        "443",  # Mazatlan
        "667",  # Necaxa
        "449",  # Santos Laguna
        "2720",  # San Luis
        "1563",  # Tijuana
        "1180",  # Puebla
        "904",  # Querétaro
        # Not in FIFA 23 anymore
        # "https://sofifa.com/team/110144/santos-laguna/",
        # "https://sofifa.com/team/101114/club-atlas/",
        # "https://sofifa.com/team/110781/club-leon/",
        # "https://sofifa.com/team/111678/club-tijuana/",
        # "https://sofifa.com/team/110152/puebla-fc/",
        # "https://sofifa.com/team/110150/gallos-blancos-de-queretaro/",
        # "https://sofifa.com/team/101121/club-necaxa/",
        # "https://sofifa.com/team/113134/futbol-club-juarez/",
    ]
    return getListPlayers(list)


# %%


def MLS():
    list = [
        "https://sofifa.com/team/112885/atlanta-united/",
        "https://sofifa.com/team/687/columbus-crew/",
        "https://sofifa.com/team/688/dc-united/",
        "https://sofifa.com/team/112893/inter-miami-cf/",
        "https://sofifa.com/team/695/fc-dallas/",
        "https://sofifa.com/team/697/la-galaxy/",
        "https://sofifa.com/team/112996/los-angeles-fc/",
        "https://sofifa.com/team/111138/minnesota-united-fc/",
        "https://sofifa.com/team/691/new-england-revolution/",
        "https://sofifa.com/team/689/new-york-red-bulls/",
        "https://sofifa.com/team/112828/new-york-city-fc/",
        "https://sofifa.com/team/112606/orlando-city-soccer-club/",
        "https://sofifa.com/team/111140/portland-timbers/",
        "https://sofifa.com/team/111144/seattle-sounders-fc/",
    ]
    return getListPlayers(list)


def MLS2():
    list = [
        "https://sofifa.com/team/114161/austin-fc/",
        "https://sofifa.com/team/693/chicago-fire-football-club/",
        "https://sofifa.com/team/113149/fc-cincinnati/",
        "https://sofifa.com/team/694/colorado-rapids/",
        "https://sofifa.com/team/114640/charlotte/",
        "https://sofifa.com/team/698/houston-dynamo/",
        "https://sofifa.com/team/114162/nashville-sc/",
        "https://sofifa.com/team/112134/philadelphia-union/",
        "https://sofifa.com/team/111928/san-jose-earthquakes/",
        "https://sofifa.com/team/696/sporting-kc/",
        "https://sofifa.com/team/111139/club-de-foot-montreal/",
        "https://sofifa.com/team/111651/toronto-fc/",
        "https://sofifa.com/team/101112/vancouver-whitecaps-fc/",
    ]
    return getListPlayers(list)


def CONCACAF():
    list = [
        "661",  # Saprissa
        "1412",  # Olimpia Honduras
    ]
    return getListPlayers(list)


################################################
################################################
################################################
# %%


def Asia():
    list = [
        # CHINA
        # "2288",  # Shanghai
        # "1521",  # Ghuangzou
        # "1068",  # Shandong
        "https://sofifa.com/team/112540/shanghai-sipg/",
        "https://sofifa.com/team/111724/shandong-luneng/",
        "https://sofifa.com/team/111768/beijing-guoan-fc/",
        "https://sofifa.com/team/110955/shanghai-shenhua-fc/",
        "https://sofifa.com/team/116361/wuhan-three-towns/",
        # COREIA
        "https://sofifa.com/team/1474/pohang-steelers/",  # Pohang Steelers
        "https://sofifa.com/team/1477/jeonbuk-hyundai-motors/",
        "https://sofifa.com/team/982/fc-seoul/",
        "https://sofifa.com/team/983/suwon-samsung-bluewings/",
        "https://sofifa.com/team/1473/ulsan/",  # Ulsan Hyundai
        "https://sofifa.com/team/110765/incheon-united-fc/",
        # TAILANDIA
        "1943",  # Buriram United
        # India
        "https://sofifa.com/team/113298/fc-goa/",
        "https://sofifa.com/team/113300/mumbai-city-fc/",
    ]

    return getListPlayers(list)


# %%


def Japao():
    list = [
        # JAPÃO
        "553",  # Avispa Fukuoka
        "554",  # Cerezo Osaka
        "528",  # FC Tokyo
        "516",  # Gamba Osaka
        "1348",  # Hokkaido Consadole Sapporo
        "534",  # Júbilo Iwata
        "518",  # Kashima Antlers
        "1078",  # Kashiwa Reysol
        "527",  # Kawasaki Frontale
        "552",  # Kyoto Sanga
        "500",  # Nagoya Grampus
        "1804",  # Sagan Tosu
        "555",  # Sanfrecce Hiroshima
        "523",  # Shimizu S-Pulse
        "1592",  # Shonan Bellmare
        "517",  # Urawa
        "1079",  # Vissel Kobe
        "506",  # Yokohama F. Marinos
        # Fora do FIFA 23
        # "https://sofifa.com/team/101148/cerezo-osaka/",
        # "https://sofifa.com/team/101150/fc-tokyo/",
        # "https://sofifa.com/team/112093/gamba-osaka/",
        # "https://sofifa.com/team/101145/kashiwa-reysol/",
        # "https://sofifa.com/team/112092/nagoya-grampus/",
        # "https://sofifa.com/team/113157/sanfrecce-hiroshima/",
        # "https://sofifa.com/team/101149/shimizu-s-pulse/",
        # "https://sofifa.com/team/101151/yokohama-f-marinos/",
    ]

    return getListPlayers(list)


# %%


def OrienteMedio():
    list = [
        # ARABIA SAUDITA
        "https://sofifa.com/team/605/al-hilal/",  # Al-Hilal
        "https://sofifa.com/team/112139/al-nassr/",  # Al-Nassr
        # "https://sofifa.com/team/112387/al-ahli/",  # Al-Ahli
        "https://sofifa.com/team/112390/al-fateh/",
        "https://sofifa.com/team/112096/al-ittifaq/",
        "https://sofifa.com/team/607/al-ittihad/",
        "https://sofifa.com/team/111674/al-shabab/",
        "https://sofifa.com/team/112393/al-taawon/",
        # QATAR
        "1610",  # Al-Duhail
        "1252",  # Al-Sadd
        "691",  # Al-Rayyan
        # EAU
        "1347",  # Al-Jazira
        "1324",  # Al Wahda
        "1323",  # Al-Ain
        # IRÃ
        "685",  # Persepolis
    ]

    return getListPlayers(list)


# %%


def Africa():
    list = [
        # Argelia
        "cr-belouizdad/startseite/verein/13365",
        "cs-constantine/kader/verein/30685",
        "mc-algier/startseite/verein/8850",
        "usm-algier/startseite/verein/6772",
        # Marrocos
        "far-rabat/startseite/verein/9099",
        "as-vita-club-kinshasa/startseite/verein/2225",
        # Sudao
        "al-hilal-omdurman/startseite/verein/8430",
        "al-merreikh-omdurman/startseite/verein/10721",
        # NORTE AFRICA
        "522",  # Al-Ahly
        "521",  # Zamalek
        "573",  # Raja Casablanca
        "570",  # Wydad
        "564",  # Espérance de Tunis
        "1608",  # ES Sétif
        "568",  # Étoile du Sahel
        # AFRICA
        "549",  # Mamelodi Sundown
        "https://sofifa.com/team/110929/kaizer-chiefs/",
        "https://sofifa.com/team/110930/orlando-pirates/",
        "1205",  # Mazembe
        "3010",  # 1º de Agosto
        "1503",  # Petro de Luanda
        "2973",  # Simba
    ]

    return getListPlayers(list)


# %%


def Oceania():
    list = [
        # OCEANIA
        "https://sofifa.com/team/111397/melbourne-victory/",
        "https://sofifa.com/team/111400/sydney-fc/",
        "https://sofifa.com/team/112224/melbourne-city-fc/",
        "https://sofifa.com/team/112427/western-sydney-wanderers/",
        "https://sofifa.com/team/111393/adelaide-united/",
        "1886",  # Auckland City
    ]

    return getListPlayers(list)
