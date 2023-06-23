# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 23:37:06 2022

@author: marcos
"""


def renameClubs(clubName):

    #%%
    if "West Ham" in clubName:
        clubName = "West Ham"
    elif clubName == "Leicester City":
        clubName = "Leicester"
    elif clubName == "Tottenham Hotspur":
        clubName = "Tottenham"
    elif clubName == "Newcastle United":
        clubName = "Newcastle"
    elif clubName == "Wolverhampton Wanderers":
        clubName = "Wolves"
    elif clubName == "West Bromwich Albion":
        clubName = "West Bromwich"
    #%%
    elif clubName == "Birmingham City":
        clubName = "Birmingham"
    elif clubName == "Derby County":
        clubName = "Derby County"
    elif clubName == "Blackburn Rovers":
        clubName = "Blackburn"
    elif clubName == "Bolton Wanderers":
        clubName = "Bolton"
    elif clubName == "AFC Bournemouth":
        clubName = "Bournemouth"
    elif clubName == "Brighton & Hove Albion":
        clubName = "Brighton"
    elif clubName == "Coventry City":
        clubName = "Coventry"
    elif clubName == "Luton Town":
        clubName = "Luton Town"
    elif clubName == "Norwich City":
        clubName = "Norwich"
    elif clubName == "Queens Park Rangers":
        clubName = "QPR"
    elif clubName == "Peterborough United":
        clubName = "Peterborough"
    elif clubName == "Swansea City":
        clubName = "Swansea"
    elif clubName == "Shrewsbury Town":
        clubName = "Shrewsbury"
    elif clubName == "Wycombe Wanderers":
        clubName = "Wycombe"
    elif clubName == "AFC Wimbledon":
        clubName = "Wimbledon"
    #%%
    elif clubName == "FC Barcelona":
        clubName = "Barcelona"
    elif clubName == "Real Madrid CF":
        clubName = "Real Madrid"
    elif clubName == "Atlético de Madrid":
        clubName = "Atlético Madrid"
    elif clubName == "Sevilla FC":
        clubName = "Sevilla"
    elif clubName == "Real Betis Balompié":
        clubName = "Real Betis"
    elif clubName == "Villarreal CF":
        clubName = "Villarreal"
    elif clubName == "Valencia CF":
        clubName = "Valencia"
    elif clubName == "Athletic Club":
        clubName = "Athletic Bilbao"
    elif clubName == "Getafe CF":
        clubName = "Getafe"
    elif clubName == "RC Celta de Vigo":
        clubName = "Celta de Vigo"
    elif clubName == "RCD Espanyol de Barcelona":
        clubName = "Espanyol"
    elif clubName == "Levante Unión Deportiva":
        clubName = "Levante"
    elif clubName == "CA Osasuna":
        clubName = "Osasuna"
    elif clubName == "Real Valladolid":
        clubName = "Valladolid"
    elif clubName == "RCD Mallorca":
        clubName = "Mallorca"
    #%%
    elif clubName == "Almería":
        clubName = "Almería"
    elif clubName == "Alcorcón":
        clubName = "La Coruna"
    elif clubName == "Burgos CF":
        clubName = "Burgos"
    elif clubName == "Cádiz CF":
        clubName = "Cádiz"
    elif clubName == "Elche CF":
        clubName = "Elche"
    elif clubName == "SD Eibar":
        clubName = "Eibar"
    elif clubName == "Elche CF":
        clubName = "Elche"
    elif clubName == "Granada CF":
        clubName = "Granada"
    elif clubName == "Girona":
        clubName = "Girona FC"
    elif clubName == "UD Ibiza":
        clubName = "Ibiza"
    elif clubName == "AD Alcorcón":
        clubName = "La Coruna"
    elif clubName == "Unión Deportiva Las Palmas":
        clubName = "Las Palmas"
    elif clubName == "CD Leganés":
        clubName = "Leganés"
    elif clubName == "Málaga CF":
        clubName = "Málaga"
    elif clubName == "Real Oviedo":
        clubName = "Real Oviedo"
    elif clubName == "Sporting Gijón":
        clubName = "Sporting de Gijón"
    elif clubName == "CD Tenerife":
        clubName = "Tenerife"
    #%%
    elif clubName == "AC Milan":
        clubName = "Milan"
    elif clubName == "U.C. Sampdoria":
        clubName = "Sampdoria"
    elif clubName == "Torino F.C.":
        clubName = "Torino"
    elif clubName == "U.S. Sassuolo Calcio":
        clubName = "Sassuolo"
    elif clubName == "Udinese Calcio":
        clubName = "Udinese"
    #%%
    elif clubName == "Ascoli Calcio":
        clubName = "Ascoli"
    elif clubName == "US Alessandria":
        clubName = "Alessandria"
    elif clubName == "SSC Bari" or clubName == "Bari 1908":
        clubName = "Bari"
    elif clubName == "Brescia Calcio":
        clubName = "Brescia"
    elif clubName == "Como 1907":
        clubName = "Como"
    elif clubName == "US Cremonese":
        clubName = "Cremonese"
    elif clubName == "Cosenza Calcio":
        clubName = "Cosenza"
    elif clubName == "Frosinone Calcio":
        clubName = "Frosinone"
    elif clubName == "AC Monza":
        clubName = "Monza"
    elif clubName == "Palermo FC":
        clubName = "Palermo"
    elif clubName == "Pisa SC":
        clubName = "Pisa"
    elif clubName == "Pordenone Calcio":
        clubName = "Pordenone"
    elif "Perugia" in clubName:
        clubName = "Perugia"
    elif clubName == "Reggina 1914":
        clubName = "Reggina"
    elif clubName == "Ternana Calcio":
        clubName = "Ternana"
    elif clubName == "LR Vicenza":
        clubName = "Vicenza"
    elif clubName == "Venezia":
        clubName = "Venezia FC"
    elif clubName == "US Salernitana 1919":
        clubName = "Salernitana"
    #%%
    elif clubName == "FC Bayern München":
        clubName = "Bayern Munique"
    elif clubName == "Bayer 04 Leverkusen":
        clubName = "Bayer Leverkusen"
    elif clubName == "Borussia Mönchengladbach":
        clubName = "Moenchengladbach"
    elif clubName == "TSG Hoffenheim":
        clubName = "Hoffenheim"
    elif clubName == "VfL Wolfsburg":
        clubName = "Wolfsburg"
    elif clubName == "Hertha BSC":
        clubName = "Hertha Berlim"
    elif clubName == "FC Köln":
        clubName = "Colonia"
    elif clubName == "VfB Stuttgart":
        clubName = "Stuttgart"
    elif clubName == "FC Augsburg":
        clubName = "Augsburg"
    elif clubName == "SV Werder Bremen":
        clubName = "Werder Bremen"
    elif clubName == "Hamburger SV":
        clubName = "Hamburgo"
    elif clubName == "Schalke 04":
        clubName = "Schalke-04"
    elif clubName == "SC Freiburg":
        clubName = "Freiburg"
    elif clubName == "TSV 1860 München":
        clubName = "Munique 1860"
    elif clubName == "MSV Duisburg":
        clubName = "Duisburg"
    elif clubName == "Saarbrücken":
        clubName = "Saarbrücken"
    #%%
    elif clubName == "FSV Mainz 05":
        clubName = "Mainz 05"
    elif clubName == "DSC Arminia Bielefeld":
        clubName = "Arminia Bielefeld"
    elif clubName == "VfL Bochum 1848":
        clubName = "Bochum 1848"
    elif clubName == "Darmstadt 98":
        clubName = "Darmstadt"
    elif clubName == "SG Dynamo Dresden":
        clubName = "Dynamo Dresden"
    elif clubName == "Fortuna Düsseldorf":
        clubName = "Fortuna Dusseldorf"
    elif clubName == "Greuther Furth":
        clubName = "Greuther Furth"
    elif clubName == "F.C. Hansa Rostock":
        clubName = "Hansa Rostock"
    elif clubName == "Heidenheim":
        clubName = "Heidenheim"
    elif clubName == "SSV Jahn Regensburg":
        clubName = "Jahn Regensburg"
    elif clubName == "Kaiserslautern":
        clubName = "Kaiserslautern"
    elif clubName == "Karlsruher SC":
        clubName = "Karlsruher"
    elif clubName == "Nürnberg":
        clubName = "Nurnberg"
    elif clubName == "SC Paderborn 07":
        clubName = "Paderborn"
    elif clubName == "FC St. Pauli":
        clubName = "St. Pauli"
    elif clubName == "FC Union Berlin":
        clubName = "Union Berlin"
    #%%
    elif clubName == "Paris Saint Germain":
        clubName = "PSG"
    elif clubName == "Olympique Lyonnais":
        clubName = "Lyon"
    elif clubName == "Olympique Marseille":
        clubName = "Olympique Marselha"
    elif clubName == "AS Monaco":
        clubName = "Monaco"
    elif clubName == "LOSC Lille":
        clubName = "Lille"
    elif clubName == "OGC Nice":
        clubName = "Nice"
    elif clubName == "Stade Rennais FC":
        clubName = "Rennes"
    elif clubName == "Montpellier Hérault SC":
        clubName = "Montpellier"
    elif clubName == "Saint-Étienne":
        clubName = "Saint-Etienne"
    elif clubName == "FC Girondins de Bordeaux":
        clubName = "Bordeaux"
    elif clubName == "FC Nantes":
        clubName = "Nantes"
    elif clubName == "Olympique de Marseille":
        clubName = "Olympique Marselha"
    elif clubName == "Reims":
        clubName = "Stade de Reims"
    elif clubName == "FC Metz":
        clubName = "Metz"
    elif clubName == "Racing Club de Lens":
        clubName = "Lens"
    elif clubName == "RC Strasbourg Alsace":
        clubName = "Strasbourg"
    #%%
    elif clubName == "AC Ajaccio":
        clubName = "Ajaccio"
    elif clubName == "Amiens SC":
        clubName = "Amiens"
    elif clubName == "Angers SCO":
        clubName = "Angers"
    elif clubName == "AJ Auxerre":
        clubName = "Auxerre"
    elif clubName == "SC Bastia":
        clubName = "Bastia"
    elif clubName == "Brest":
        clubName = "Stade Brestois"
    elif clubName == "Clermont Foot 63":
        clubName = "Clermont"
    elif clubName == "Stade Malherbe Caen":
        clubName = "Caen"
    elif clubName == "Dijon FCO":
        clubName = "Dijon"
    elif clubName == "Grenoble Foot 38":
        clubName = "Grenoble"
    elif clubName == "En Avant de Guingamp":
        clubName = "Guingamp"
    elif clubName == "Le Havre AC":
        clubName = "Le Havre"
    elif clubName == "Lorient":
        clubName = "FC Lorient"
    elif clubName == "Nîmes":
        clubName = "Nimes"
    elif clubName == "AS Nancy Lorraine":
        clubName = "Nancy"
    elif clubName == "Paris":
        clubName = "Paris FC"
    elif clubName == "FC Sochaux-Montbéliard":
        clubName = "Sochaux"
    elif clubName == "ESTAC Troyes":
        clubName = "Troyes"
    elif clubName == "Toulouse Football Club":
        clubName = "Toulouse"
    elif clubName == "Valenciennes FC":
        clubName = "Valenciennes"
    #%%
    elif clubName == "SL Benfica":
        clubName = "Benfica"
    elif clubName == "Sporting CP":
        clubName = "Sporting"
    elif clubName == "FC Porto":
        clubName = "Porto"
    elif clubName == "Sporting Braga":
        clubName = "Braga"
    elif clubName == "Vitória SC":
        clubName = "Vitória Guimarães"
    elif clubName == "Boavista FC":
        clubName = "Boavista"
    elif clubName == "Clube Sport Marítimo":
        clubName = "Marítimo"
    elif clubName == "Portimonense SC":
        clubName = "Portimonense"
    elif clubName == "Futebol Clube de Famalicão":
        clubName = "Famalicão"
    elif clubName == "FC Paços de Ferreira":
        clubName = "Paços de Ferreira"
    elif clubName == "Gil Vicente FC":
        clubName = "Gil Vicente"
    elif clubName == "Estoril Praia":
        clubName = "Estoril"
    elif clubName == "Belenenses SAD" or clubName == "B SAD":
        clubName = "Belenenses"
    elif clubName == "Académica de Coimbra":
        clubName = "Coimbra"
    elif clubName == "Moreirense FC":
        clubName = "Moreirense"
    elif clubName == "CD Nacional":
        clubName = "Nacional PT"
    #%%
    elif clubName == "AZ":
        clubName = "AZ Alkmaar"
    elif clubName == "SC Heerenveen":
        clubName = "Heerenveen"
    elif clubName == "FC Utrecht":
        clubName = "Utrecht"
    elif clubName == "FC Twente":
        clubName = "Twente"
    elif clubName == "FC Twente":
        clubName = "Twente"
    elif clubName == "FC Groningen":
        clubName = "Groningen"
    elif clubName == "Sparta Rotterdam":
        clubName = "Sparta Rotterdam"

    elif clubName == "Club Brugge":
        clubName = "Brugge"
    elif clubName == "Standard Liège":
        clubName = "Standard Liege"
    elif clubName == "RSC Anderlecht":
        clubName = "Anderlecht"
    elif clubName == "KRC Genk":
        clubName = "Genk"
    elif clubName == "KAA Gent":
        clubName = "Gent"
    elif clubName == "Royal Antwerp FC":
        clubName = "Royal Antwerp"
    elif clubName == "KV Mechelen":
        clubName = "Mechelen"
    #%%
    elif clubName == "Rangers":
        clubName = "Glasgow Rangers"
        # SUIÇA
    elif clubName == "BSC Young Boys":
        clubName = "Young Boys"
    elif clubName == "FC Basel 1893":
        clubName = "Basel"
    elif clubName == "Zürich":
        clubName = "Zurich"
    elif clubName == "FC Lugano":
        clubName = "Lugano"
    elif clubName == "Grasshopper Club Zürich":
        clubName = "Grasshopper"
    elif clubName == "FC Luzern":
        clubName = "Luzern"
        # AUSTRIA
    elif clubName == "SK Sturm Graz":
        clubName = "Sturm Graz"
    elif clubName == "FK Austria Wien":
        clubName = "Austria Wien"
    elif clubName == "Salzburg":
        clubName = "RB Salzburg"
    elif clubName == "Rapid Vienna":
        clubName = "Rapid Wien"
        # POLONIA
    elif clubName == "Lech Poznań":
        clubName = "Lech Poznan"
    elif clubName == "Cracovia Kraków":
        clubName = "Cracovia"
    elif clubName == "Wisła Kraków":
        clubName = "Wisla Krakow"
    #%%
    # NORUEGA
    elif clubName == "Rosenborg BK":
        clubName = "Rosenborg"
    elif clubName == "Molde FK":
        clubName = "Molde"
    elif clubName == "Bodø / Glimt":
        clubName = "Bodø/Glimt"
    # SUÉCIA
    elif clubName == "Malmö FF":
        clubName = "Malmo"
    elif clubName == "AIK":
        clubName = "AIK"
    elif clubName == "Hammarby IF":
        clubName = "Hammarby"
    elif clubName == "IF Elfsborg":
        clubName = "Elfsborg"
    elif clubName == "IFK Goteborg":
        clubName = "IFK Göteborg"
    # DINAMARCA
    elif clubName == "København":
        clubName = "Copenhague"
    elif clubName == "FC Midtjylland":
        clubName = "Midtjylland"
    elif clubName == "Brøndby":
        clubName = "Brøndby"
    elif clubName == "AaB":
        clubName = "Aalborg"
    elif clubName == "Randers":
        clubName = "Randers"
    elif clubName == "Nordsjælland":
        clubName = "Nordsjaelland"
    elif clubName == "OB":
        clubName = "Odense Boldklub"
    # FINLANDIA
    elif clubName == "HJK":
        clubName = "Helsinki"

    #%%
    elif clubName == "Zenit Saint Petersburg":
        clubName = "Zenit"
    elif clubName == "Spartak Moskva":
        clubName = "Spartak Moscou"
    elif clubName == "CSKA Moskva":
        clubName = "CSKA"
    elif clubName == "FC Krasnodar":
        clubName = "Krasnodar"
    elif clubName == "Lokomotiv Moskva":
        clubName = "Locomotiv Moscou"
    elif clubName == "Dynamo Moskva":
        clubName = "Dinamo Moscou"
    elif clubName == "FC Sochi":
        clubName = "Sochi"

    elif clubName == "Shakhtar Donetsk":
        clubName = "Shakhtar Donetsk"
    elif clubName == "Dynamo Kyiv":
        clubName = "Dinamo Kiev"
    elif clubName == "SC Dnipro-1":
        clubName = "Dnipro"
    elif clubName == "FC Metalist 1925 Kharkiv":
        clubName = "Metalist"
    elif clubName == "FK Qarabag":
        clubName = "Qarabag"
    elif clubName == "FC Astana":
        clubName = "Astana"
    #%%
    # TURQUIA
    elif clubName == "Galatasaray SK":
        clubName = "Galatasaray"
    elif clubName == "Beşiktaş JK":
        clubName = "Besiktas"
    elif clubName == "Fenerbahçe SK":
        clubName = "Fenerbahce"
    elif clubName == "İstanbul Başakşehir":
        clubName = "Instanbul Basaksehir"
    elif clubName == "Demir Grup Sivasspor":
        clubName = "Sivasspor"
    elif clubName == "Antalyaspor":
        clubName = "Antalyaspor"
    # GRÉCIA
    elif clubName == "Olympiacos":
        clubName = "Olympiacos"
    elif clubName == "AEK Athens":
        clubName = "AEK"
    elif clubName == "Panathinaikos FC":
        clubName = "Panathinaikos"
    elif clubName == "Aris Thessaloniki":
        clubName = "Aris Thessaloniki"
    #%%
    # CROACIA
    elif clubName == "HNK Rijeka":
        clubName = "Rijeka"
    # ROMENIA
    elif clubName == "FCSB":
        clubName = "Steaua Bucareste"
    elif clubName == "CFR Cluj":
        clubName = "Cluj"
    # REP.TCHECA
    elif clubName == "Sparta Praha":
        clubName = "Sparta Praga"
    elif clubName == "SK Slavia Praha":
        clubName = "Slavia Praha"
    elif clubName == "Viktoria Plzeň":
        clubName = "Viktoria Plzen"
    # HUNGRIA
    elif clubName == "Ferencvárosi TC":
        clubName = "Ferencvaros"
    elif clubName == "Budapest Honvéd":
        clubName = "Honved"
    elif clubName == "Puskás Akadémia FC":
        clubName = "Puskas Akademia"
    elif clubName == "Újpest FC":
        clubName = "Ujpest"
    # BULGARIA
    elif clubName == "Ludogorets Razgrad":
        clubName = "Ludogorets"
    # SERVIA
    elif clubName == "FK Partizan":
        clubName = "Partizan"
    elif clubName == "Crvena Zvezda":
        clubName = "Estrela Vermelha"
    #%%
    elif clubName == "FK Vardar":
        clubName = "FK Vardar"
    elif clubName == "NK Maribor":
        clubName = "Maribor"
    elif clubName == "FK Sarajevo":
        clubName = "Sarajevo"
    elif clubName == "HŠK Zrinjski":
        clubName = "Zrinjski"
    ###################################################
    ###################################################
    ###################################################
    #%%
    elif clubName == "São Paulo FC":
        clubName = "São Paulo"
    elif clubName == "Santos FC":
        clubName = "Santos"
    elif clubName == "SE Palmeiras":
        clubName = "Palmeiras"
    elif clubName == "SC Internacional":
        clubName = "Internacional"
    elif "Cruzeiro" in clubName:
        clubName = "Cruzeiro"
    elif clubName == "Atlético Mineiro":
        clubName = "Atlético-MG"
    elif clubName == "Botafogo FR":
        clubName = "Botafogo"
    elif clubName == "Fluminense FC":
        clubName = "Fluminense"
    elif clubName == "Vasco da Gama":
        clubName = "Vasco"
    elif clubName == "Athletico Paranaense":
        clubName = "Atlético-PR"
    #%%
    # Nordeste
    elif "ABC" in clubName:
        clubName = "ABC"
    elif clubName == "EC Bahia":
        clubName = "Bahia"
    elif clubName == "Botafogo PB":
        clubName = "Botafogo-PB"
    elif clubName == "Ceará SC":
        clubName = "Ceará"
    elif clubName == "AD Confiança":
        clubName = "Confiança"
    elif clubName == "CS Alagoano":
        clubName = "CSA"
    elif clubName == "Clube de Regatas Brasil":
        clubName = "CRB"
    elif "Fortaleza" in clubName:
        clubName = "Fortaleza"
    elif clubName == "Náutico":
        clubName = "Naútico"
    elif "Campinense" in clubName:
        clubName = "Campinense"
    elif clubName == "SD Juazeirense":
        clubName = "Íbis"
    elif "Moto Club" in clubName:
        clubName = "Moto Club"
    elif clubName == "Sport Recife":
        clubName = "Sport"
    elif clubName == "EC Vitória":
        clubName = "Vitória"

    # Sul
    elif clubName == "SER Caxias do Sul":
        clubName = "Caxias do Sul"
    elif clubName == "Brusque FC":
        clubName = "Brusque"
    elif clubName == "Avaí FC":
        clubName = "Avaí"
    elif clubName == "Chapecoense AF":
        clubName = "Chapecoense"
    elif clubName == "Criciúma EC":
        clubName = "Criciúma"
    elif clubName == "Joinville EC":
        clubName = "Joinville"
    elif clubName == "Londrina EC":
        clubName = "Londrina"
    elif clubName == "Operário Ferroviário EC":
        clubName = "Operário-PR"
    elif clubName == "Paraná Clube":
        clubName = "Paraná"

    # Copa Verde
    elif clubName == "Atlético Goianiense":
        clubName = "Atlético-GO"
    elif clubName == "SE Gama":
        clubName = "Gama"
    elif clubName == "Cuiabá EC":
        clubName = "Cuiabá"
    elif clubName == "Clube do Remo":
        clubName = "Remo"
    elif clubName == "Paysandu SC":
        clubName = "Paysandu"
    elif clubName == "Manaus FC":
        clubName = "Manaus"

    # Minas MG
    elif clubName == "América Mineiro":
        clubName = "América-MG"
    elif clubName == "Tombense FC":
        clubName = "Tombense"

    # RJ
    elif clubName == "Bangu AC":
        clubName = "Bangu"
    elif clubName == "Madureira EC":
        clubName = "Madureira"
    elif clubName == "Volta Redonda FC":
        clubName = "Volta Redonda"

    # SP
    elif clubName == "Botafogo SP":
        clubName = "Botafogo-SP"
    elif clubName == "RB Bragantino":
        clubName = "Bragantino"
    elif clubName == "AA Internacional":
        clubName = "Inter Limeira"
    elif clubName == "CA Juventus":
        clubName = "Juventus Mooca"
    elif clubName == "Ituano FC":
        clubName = "Ituano"
    elif clubName == "Guarani FC":
        clubName = "Guarani"
    elif clubName == "Mirassol FC":
        clubName = "Mirassol"
    elif clubName == "Paulista FC":
        clubName = "Paulista Jundiaí"
    elif clubName == "EC Santo André":
        clubName = "Santo André"
    elif clubName == "EC São Bento":
        clubName = "São Bento"
    #%%
    elif clubName == "Club Atlético Colón":
        clubName = "Colón"
    elif clubName == "Racing Club":
        clubName = "Racing"
    elif clubName == "Club Atlético Independiente":
        clubName = "Independiente"
    elif clubName == "Club Atlético Lanús":
        clubName = "Lanús"
    elif clubName == "Estudiantes de La Plata":
        clubName = "Estudiantes"
    elif clubName == "San Lorenzo de Almagro":
        clubName = "San Lorenzo"
    elif clubName == "Talleres Córdoba":
        clubName = "Talleres"
    elif clubName == "Club Atlético Banfield":
        clubName = "Banfield"
    elif clubName == "Arsenal de Sarandi":
        clubName = "Arsenal Sarandí"

    elif clubName == "Club Atlético Huracán":
        clubName = "Huracán"
    elif clubName == "Gimnasia La Plata":
        clubName = "Gimnasia y Esgrima"
    elif clubName == "Unión Santa Fe":
        clubName = "Unión de Santa Fe"
    elif clubName == "Club Atlético Aldosivi":
        clubName = "Aldosivi"
    elif clubName == "Club Atlético Central Córdoba":
        clubName = "Central Córdoba"
    elif clubName == "CA Tigre":
        clubName = "Tigre"
    elif clubName == "Belgrano":
        clubName = "Belgrano"
    elif clubName == "Quilmes AC":
        clubName = "Quilmes"
    #%%
    # URUGUAI
    elif clubName == "River Plate de Montevideo":
        clubName = "River Plate de Montevideo"
    elif clubName == "Montevideo City Torque":
        clubName = "Montevideo City"
    elif clubName == "Danubio":
        clubName = "Danubio"
    elif clubName == "Defensor Sporting":
        clubName = "Defensor"
    # PARAGUAI
    elif clubName == "Club Olimpia":
        clubName = "Olimpia"
    elif clubName == "Club Libertad":
        clubName = "Libertad"
    elif clubName == "Club Nacional":
        clubName = "Club Nacional"
    # CHILE
    elif clubName == "Colo Colo":
        clubName = "Colo-Colo"
    elif clubName == "Universidad de Chile":
        clubName = "LaU"
    elif clubName == "Universidad Católica":
        clubName = "Univ. Católica"
    elif "Palestino" in clubName:
        clubName = "Palestino"
    elif "Huachipato" in clubName:
        clubName = "Huachipato"
    elif clubName == "CD Everton":
        clubName = "Everton-CHI"
    elif clubName == "CD Cobreloa":
        clubName = "Cobreloa"
    #%%
    # PERU
    elif (
        clubName == "Club Universitario de Deportes"
        or clubName == "Universitario de Deportes"
    ):
        clubName = "Universitario"
    elif "Cienciano" in clubName:
        clubName = "Cienciano"
    elif clubName == "FBC Melgar":
        clubName = "Melgar"
    elif clubName == "Sport Boys":
        clubName = "Sport Boys"
    elif clubName == "Wilstermann":
        clubName = "Jorge Wilstermann"
    # BOLIVIA
    elif clubName == "Club The Strongest":
        clubName = "The Strongest"
    elif clubName == "Club Deportivo Jorge Wilstermann":
        clubName = "Jorge Wilstermann"
    elif clubName == "Club Always Ready":
        clubName = "Always Ready"
    elif clubName == "Oriente Petrolero":
        clubName = "Oriente Petrolero"
    elif clubName == "CS Blooming":
        clubName = "Blooming"

    #%%
    # COLÔMBIA
    elif clubName == "Junior FC":
        clubName = "Junior"
    elif clubName == "Independiente Medellín":
        clubName = "I. Medellín"
    elif clubName == "Independiente Santa Fé":
        clubName = "Santa Fé"
    elif clubName == "Deportes Tolima":
        clubName = "Tolima"
    elif clubName == "La Equidad":
        clubName = "La Equidad"
    # EQUADOR
    elif clubName == "SD Aucas":
        clubName = "Aucas"
    elif clubName == "Independiente del Valle":
        clubName = "I. Del Valle"
    elif clubName == "Liga de Quito" or clubName == "LDU Quito":
        clubName = "LDU"
    elif clubName == "CS Emelec":
        clubName = "Emelec"
    elif clubName == "Barcelona SC" or clubName == "Barcelona Guayaquil":
        clubName = "Barcelona-EQU"
    elif clubName == "Guayaquil City":
        clubName = "Guayaquil City"
    elif clubName == "Universidad Católica del Ecuador":
        clubName = "U. Católica del Ecuador"
    # VENEZUELA
    elif clubName == "Caracas FC":
        clubName = "Caracas"
    elif clubName == "Deportivo Táchira FC":
        clubName = "Deportivo Táchira"
    elif clubName == "Deportivo La Guaira":
        clubName = "La Guaira"
    elif clubName == "Estudiantes Mérida":
        clubName = "Estudiantes de Mérida"
    elif clubName == "Metropolitanos de Caracas FC":
        clubName = "Metropolitanos de Caracas"
    elif clubName == "Monagas SC":
        clubName = "Monagas"
    elif clubName == "Zamora FC":
        clubName = "Zamora"
    ###################################################
    ###################################################
    ###################################################
    #%%
    elif clubName == "Club América":
        clubName = "América-MEX"
    elif clubName == "Guadalajara":
        clubName = "Chivas Guadalajara"
    elif clubName == "UNAM Pumas":
        clubName = "Pumas"
    elif clubName == "Tigres UANL":
        clubName = "Tigres"
    elif clubName == "FC Juárez":
        clubName = "Juárez"
    elif "Toluca" in clubName:
        clubName = "Toluca"
    elif "Atlas" in clubName:
        clubName = "Atlas"
    elif "Tijuana" in clubName:
        clubName = "Tijuana"
    elif "Puebla" in clubName:
        clubName = "Puebla"
    elif clubName == "Gallos Blancos de Querétaro" or clubName == "Club Querétaro":
        clubName = "Querétaro"
    elif "Necaxa" in clubName:
        clubName = "Necaxa"
    elif clubName == "Fútbol Club Juárez":
        clubName = "Juárez"
    elif clubName == "León":
        clubName = "Club León"
    #%%
    elif clubName == "Seattle Sounders FC":
        clubName = "Seattle Sounders"
    elif clubName == "Los Angeles FC":
        clubName = "Los Angeles FC"
    elif clubName == "New York City":
        clubName = "NY City"
    elif clubName == "Dallas":
        clubName = "FC Dallas"
    elif clubName == "New England":
        clubName = "NE Revolution"
    elif clubName == "Orlando City Soccer Club":
        clubName = "Orlando City"
    elif clubName == "Inter Miami CF":
        clubName = "Inter Miami"
    elif clubName == "D.C. United":
        clubName = "DC United"
    elif clubName == "Toronto":
        clubName = "Toronto FC"
    elif clubName == "Vancouver Whitecaps FC":
        clubName = "Vancouver Whitecaps"
    elif clubName == "New York RB":
        clubName = "NY Red Bulls"
    elif clubName == "Minnesota United FC":
        clubName = "Minnesota United"
    elif clubName == "Club de Foot Montréal":
        clubName = "Club Montréal"
    elif clubName == "Nashville SC":
        clubName = "Nashville"
    elif clubName == "Chicago Fire Football Club":
        clubName = "Chicago Fire"
    elif clubName == "Sporting KC":
        clubName = "Sporting Kansas City"
    elif clubName == "Austin":
        clubName = "Austin FC"
    elif clubName == "Charlotte":
        clubName = "Charlotte FC"
    elif clubName == "Philadelphia":
        clubName = "Philadelphia Union"
    elif clubName == "CF Montréal":
        clubName = "Montreal Impact"
    

    elif "Saprissa" in clubName:
        clubName = "Saprissa"
    elif "Alajuelense" in clubName:
        clubName = "Alajuelense"
    elif clubName == "CD Olimpia":
        clubName = "Olimpia-HON"
    ###################################################
    ###################################################
    ###################################################
    #%%
    elif clubName == "Shanghai Port":
        clubName = "Shanghai Port"
    elif clubName == "Guangzhou":
        clubName = "Ghuangzhou"
    elif clubName == "Shandong Taishan":
        clubName = "Shandong Taishan"
    elif clubName == "Shanghai Shenhua FC":
        clubName = "Shanghai Shenhua"

    elif clubName == "Jeonbuk Motors":
        clubName = "Jeonbuk Hyundai"
    elif clubName == "Suwon Samsung Bluewings":
        clubName = "Suwon Samsung"
    elif clubName == "Incheon United FC":
        clubName = "Incheon United"
    elif clubName == "Seoul":
        clubName = "FC Seoul"
    elif "Ulsan" in clubName:
        clubName = "Ulsan Hyundai"

    elif clubName == "FC Goa":
        clubName = "FC Goa"
    elif clubName == "Mumbai City FC":
        clubName = "Mumbai City"
    #%%
    elif clubName == "Al Ain":
        clubName = "Al Ain-EAU"
    elif clubName == "Al Sadd SC":
        clubName = "Al Sadd"
    elif clubName == "Al Hilal SC":
        clubName = "Al Hilal"
    elif clubName == "Al Ahli Jeddah":
        clubName = "Al Ahli"
    elif clubName == "Al Duhail SC":
        clubName = "Al Duhail"
    elif clubName == "Al-Gharafa SC":
        clubName = "Al Gharafa"
    elif clubName == "Qatar SC":
        clubName = "Qatar"
    elif clubName == "Al Rayyan":
        clubName = "Al Rayyan"

    elif clubName == "Al-Shorta SC":
        clubName = "Al Shorta"
    elif clubName == "Al-Zawraa SC":
        clubName = "Al Zawraa"
    #%%
    elif "Zamalek" in clubName:
        clubName = "Zamalek"
    elif clubName == "Wydad AC":
        clubName = "Wydad Casablanca"
    elif clubName == "ES Sétif":
        clubName = "ES Sétif"
    elif "Belouizdad" in clubName:
        clubName = "CR Belouizdad"
    elif "Constantine" in clubName:
        clubName = "CS Constantine"
    elif "Club Africain" in clubName:
        clubName = "Club Africain"
    elif clubName == "Etoile Sportive du Sahel":
        clubName = "Etoile du Sahel"
    elif "Sfaxien" in clubName:
        clubName = "Sfaxien"
    elif "Omdurman" in clubName:
        clubName = "Al-Hilal Omdurman"

    elif clubName == "CD 1º de Agosto":
        clubName = "Primeiro de Agosto"
    elif clubName == "CA Petróleos Luanda":
        clubName = "Petro de Luanda"
    elif clubName == "Petro Atlético":
        clubName = "Petro de Luanda"
    elif clubName == "Coton Sport FC de Garoua":
        clubName = "Cotonsport"
    elif "Mazembe" in clubName:
        clubName = "Mazembe"
    elif clubName == "AS Vita Club Kinshasa":
        clubName = "AS Vita"
    elif "Enyimba" in clubName:
        clubName = "Enyimba"
    elif clubName == "Simba SC":
        clubName = "Simba"
    #%%
    elif clubName == "Melbourne City FC":
        clubName = "Melbourne City"
    elif clubName == "Sydney":
        clubName = "Sydney FC"
    elif clubName == "Auckland City FC":
        clubName = "Auckland City"

    return clubName
