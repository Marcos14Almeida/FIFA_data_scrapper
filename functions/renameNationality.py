# -*- coding: utf-8 -*-
"""
Created on Sun May  1 14:07:40 2022

@author: marcos
"""


def renameNationality(nationality):
    # Do site soccerwiki em PT para ingçes
    if nationality == "Brasil":
        nationality = "Brazil"
    elif nationality == "Albânia":
        nationality = "Albania"
    elif nationality == "Áustria":
        nationality = "Austria"
    elif nationality == "Azerbaijão":
        nationality = "Azerbaijan"
    elif nationality == "Alemanha":
        nationality = "Germany"
    elif nationality == "Algéria":
        nationality = "Algeria"
    elif nationality == "África do Sul":
        nationality = "South Africa"
    elif nationality == "Arábia Saudita":
        nationality = "South Arabia"
    elif nationality == "Saudi Arabia":
        nationality = "South Arabia"
    elif nationality == "Austrália":
        nationality = "Australia"
    elif nationality == "Armênia":
        nationality = "Armenia"
    elif nationality == "Barém":
        nationality = "Bahrein"
    elif nationality == "Bélgica":
        nationality = "Belgium"
    elif nationality == "Benim":
        nationality = "Benin"
    elif nationality == "Bielorrússia":
        nationality = "Belarus"
    elif nationality == "Bolívia":
        nationality = "Bolivia"
    elif nationality == "Bósnia e Herzegovina":
        nationality = "Bosnia"
    elif nationality == "Bosnia and Herzegovina":
        nationality = "Bosnia"
    elif nationality == "Bulgária":
        nationality = "Bulgaria"
    elif nationality == "Cabo Verde":
        nationality = "Cape Verde"
    elif nationality == "Cape Verde Islands":
        nationality = "Cape Verde"
    elif nationality == "Camarões":
        nationality = "Cameroon"
    elif nationality == "Catar":
        nationality = "Qatar"
    elif nationality == "Côte d'Ivoire":
        nationality = "Ivory Coast"
    elif nationality == "Canadá":
        nationality = "Canada"
    elif "China" in nationality:
        nationality = "China"
    elif nationality == "Chipre":
        nationality = "Cyprus"
    elif nationality == "Cazaquistão":
        nationality = "Kazakhstan"
    elif nationality == "Colômbia":
        nationality = "Colombia"
    elif nationality == "República da Coreia":
        nationality = "South Korea"
    elif nationality == "Korea Republic":
        nationality = "South Korea"
    elif nationality == "Costa do Marfim":
        nationality = "Ivory Coast"
    elif nationality == "Congo DR":
        nationality = "Democratic Republic Congo"
    elif nationality == "Croácia":
        nationality = "Croatia"
    elif nationality == "Dinamarca":
        nationality = "Denmark"
    elif nationality == "Egito":
        nationality = "Egypt"
    elif nationality == "Equador":
        nationality = "Ecuador"
    elif nationality == "Emirados Árabes Unidos":
        nationality = "United Arab Emirates"
    elif nationality == "Escócia":
        nationality = "Scotland"
    elif nationality == "Eslováquia":
        nationality = "Slovakia"
    elif nationality == "Eslovênia":
        nationality = "Slovenia"
    elif nationality == "Estados Unidos":
        nationality = "United States"
    elif nationality == "Espanha":
        nationality = "Spain"
    elif nationality == "Gabão":
        nationality = "Gabon"
    elif nationality == "Gâmbia":
        nationality = "Gambia"
    elif nationality == "Gana":
        nationality = "Ghana"
    elif nationality == "Geórgia":
        nationality = "Georgia"
    elif nationality == "Grécia":
        nationality = "Greece"
    elif nationality == "Guiné Equatorial":
        nationality = "Equatorial Guinea"
    elif nationality == "Guine Bissau":
        nationality = "Guinea Bissau"
    elif nationality == "Guine-Bissau":
        nationality = "Guinea Bissau"
    elif nationality == "Guinea Equatorial":
        nationality = "Equatorial Guinea"
    elif nationality == "Irã":
        nationality = "Iran"
    elif nationality == "Inglaterra":
        nationality = "England"
    elif nationality == "Irlanda":
        nationality = "Ireland"
    elif nationality == "Republic of Ireland":
        nationality = "Ireland"
    elif nationality == "Hungria":
        nationality = "Hungary"
    elif nationality == "Japão":
        nationality = "Japan"
    elif nationality == "Finlândia":
        nationality = "Finland"
    elif nationality == "França":
        nationality = "France"
    elif nationality == "Guiné":
        nationality = "Guinea"
    elif nationality == "Guiné Bissau":
        nationality = "Guinea Bissau"
    elif nationality == "Itália":
        nationality = "Italy"
    elif nationality == "Iraque":
        nationality = "Iraq"
    elif nationality == "Islândia":
        nationality = "Iceland"
    elif nationality == "Holanda":
        nationality = "Netherlands"
    elif nationality == "Lesoto":
        nationality = "Lesotho"
    elif nationality == "Líbano":
        nationality = "Lebanon"
    elif nationality == "Líbia":
        nationality = "Libya"
    elif nationality == "Luxemburgo":
        nationality = "Luxembourg"
    elif nationality == "Macedónia do Norte":
        nationality = "North Macedonia"
    elif nationality == "Maldivas":
        nationality = "Maldives"
    elif nationality == "Mauritânia":
        nationality = "Mauritania"
    elif nationality == "Marrocos":
        nationality = "Morocco"
    elif nationality == "Marocco":
        nationality = "Morocco"
    elif nationality == "México":
        nationality = "Mexico"
    elif nationality == "Montserrat":
        nationality = "England"
    elif nationality == "Moçambique":
        nationality = "Mozambique"
    elif nationality == "Moldávia":
        nationality = "Moldova"
    elif nationality == "Namíbia":
        nationality = "Namibia"
    elif nationality == "Níger":
        nationality = "Niger"
    elif nationality == "Nigéria":
        nationality = "Nigeria"
    elif nationality == "Nova Zelândia":
        nationality = "New Zealand"
    elif nationality == "Noruega":
        nationality = "Norway"
    elif nationality == "Omã":
        nationality = "Oman"
    elif nationality == "Quênia":
        nationality = "Kenya"
    elif nationality == "Panama":
        nationality = "Panama"
    elif nationality == "Paraguai":
        nationality = "Paraguay"
    elif nationality == "Perú":
        nationality = "Peru"
    elif nationality == "Polônia":
        nationality = "Poland"
    elif nationality == "Czech republic":
        nationality = "Czech Republic"
    elif nationality == "República Tcheca":
        nationality = "Czech Republic"
    elif nationality == "República Centro-Africana":
        nationality = "Central African Republic"
    elif nationality == "RD do Congo":
        nationality = "Democratic Republic Congo"
    elif nationality == "Romênia":
        nationality = "Romania"
    elif nationality == "Rússia":
        nationality = "Russia"
    elif nationality == "Saudi Arabia":
        nationality = "South Arabia"
    elif nationality == "Serra Leoa":
        nationality = "Sierra Leone"
    elif nationality == "Sérvia":
        nationality = "Serbia"
    elif nationality == "Síria":
        nationality = "Syria"
    elif nationality == "Suiça":
        nationality = "Switzerland"
    elif nationality == "Sudão":
        nationality = "Sudan"
    elif nationality == "Suíça":
        nationality = "Switzerland"
    elif nationality == "Suécia":
        nationality = "Sweden"
    elif nationality == "Tanzânia":
        nationality = "Tanzania"
    elif nationality == "Tailândia":
        nationality = "Thailand"
    elif nationality == "Trinidad e Tobago":
        nationality = "Trinidad and Tobago"
    elif nationality == "Turquia":
        nationality = "Turkey"
    elif nationality == "Tunísia":
        nationality = "Tunisia"
    elif nationality == "Uruguai":
        nationality = "Uruguay"
    elif nationality == "Ucrânia":
        nationality = "Ukraine"
    elif nationality == "Uzbequistão":
        nationality = "Uzbekistan"
    elif nationality == "Zâmbia":
        nationality = "Zambia"
    elif nationality == "Zimbábue":
        nationality = "Zimbabwe"

    return nationality
