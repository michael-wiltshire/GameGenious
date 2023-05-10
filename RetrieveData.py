import requests
import time


all_champion_id = {
        1: 'Annie',
        2: 'Olaf',
        3: 'Galio',
        4: 'Twisted Fate',
        5: 'Xin Zhao',
        6: 'Urgot',
        7: 'LeBlanc',
        8: 'Vladimir',
        9: 'Fiddlesticks',
        10: 'Kayle',
        11: 'Master Yi',
        12: 'Alistar',
        13: 'Ryze',
        14: 'Sion',
        15: 'Sivir',
        16: 'Soraka',
        17: 'Teemo',
        18: 'Tristana',
        19: 'Warwick',
        20: 'Nunu & Willump',
        21: 'Miss Fortune',
        22: 'Ashe',
        23: 'Tryndamere',
        24: 'Jax',
        25: 'Morgana',
        26: 'Zilean',
        27: 'Singed',
        28: 'Evelynn',
        29: 'Twitch',
        30: 'Karthus',
        31: "Cho'Gath",
        32: 'Amumu',
        33: 'Rammus',
        34: 'Anivia',
        35: 'Shaco',
        36: 'Dr.Mundo',
        37: 'Sona',
        38: 'Kassadin',
        39: 'Irelia',
        40: 'Janna',
        41: 'Gangplank',
        42: 'Corki',
        43: 'Karma',
        44: 'Taric',
        45: 'Veigar',
        48: 'Trundle',
        50: 'Swain',
        51: 'Caitlyn',
        53: 'Blitzcrank',
        54: 'Malphite',
        55: 'Katarina',
        56: 'Nocturne',
        57: 'Maokai',
        58: 'Renekton',
        59: 'JarvanIV',
        60: 'Elise',
        61: 'Orianna',
        62: 'Wukong',
        63: 'Brand',
        64: 'LeeSin',
        67: 'Vayne',
        68: 'Rumble',
        69: 'Cassiopeia',
        72: 'Skarner',
        74: 'Heimerdinger',
        75: 'Nasus',
        76: 'Nidalee',
        77: 'Udyr',
        78: 'Poppy',
        79: 'Gragas',
        80: 'Pantheon',
        81: 'Ezreal',
        82: 'Mordekaiser',
        83: 'Yorick',
        84: 'Akali',
        85: 'Kennen',
        86: 'Garen',
        89: 'Leona',
        90: 'Malzahar',
        91: 'Talon',
        92: 'Riven',
        96: "Kog'Maw",
        98: 'Shen',
        99: 'Lux',
        101: 'Xerath',
        102: 'Shyvana',
        103: 'Ahri',
        104: 'Graves',
        105: 'Fizz',
        106: 'Volibear',
        107: 'Rengar',
        110: 'Varus',
        111: 'Nautilus',
        112: 'Viktor',
        113: 'Sejuani',
        114: 'Fiora',
        115: 'Ziggs',
        117: 'Lulu',
        119: 'Draven',
        120: 'Hecarim',
        121: "Kha'Zix",
        122: 'Darius',
        126: 'Jayce',
        127: 'Lissandra',
        131: 'Diana',
        133: 'Quinn',
        134: 'Syndra',
        136: 'AurelionSol',
        141: 'Kayn',
        142: 'Zoe',
        143: 'Zyra',
        145: "Kai'sa",
        147: "Seraphine",
        150: 'Gnar',
        154: 'Zac',
        157: 'Yasuo',
        161: "Vel'Koz",
        163: 'Taliyah',
        166: "Akshan",
        164: 'Camille',
        201: 'Braum',
        202: 'Jhin',
        203: 'Kindred',
        222: 'Jinx',
        223: 'TahmKench',
        234: 'Viego',
        235: 'Senna',
        236: 'Lucian',
        238: 'Zed',
        240: 'Kled',
        245: 'Ekko',
        246: 'Qiyana',
        254: 'Vi',
        266: 'Aatrox',
        267: 'Nami',
        268: 'Azir',
        350: 'Yuumi',
        360: 'Samira',
        412: 'Thresh',
        420: 'Illaoi',
        421: "Rek'Sai",
        427: 'Ivern',
        429: 'Kalista',
        432: 'Bard',
        497: 'Rakan',
        498: 'Xayah',
        516: 'Ornn',
        517: 'Sylas',
        526: 'Rell',
        518: 'Neeko',
        523: 'Aphelios',
        555: 'Pyke',
        875: "Sett",
        711: "Vex",
        777: "Yone",
        887: "Gwen",
        876: "Lillia",
        895: "Nilah",
        360: "Samira",
        147: "Seraphine",
        526: "Rell",
        234: "Viego",
        887: "Gwen",
        221: "Zeri",
        888: "Renata Glasc",
        902: "Milio",
        897: "K'Sante",
        200: "Bel'Veth",
        711: "Vex",
        166: "Akshan"
    }
# Enter your Riot Games API key here
API_KEY = 'RGAPI-b987331b-62ed-4c16-891b-0e25c4576f3d'

# Enter the name of the summoner you want to check
summoner_name = 'Ignitos'


# Grab summoner_id
url1 = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={API_KEY}'
response = requests.get(url1)
if response.status_code == 200:
    data = response.json()
    summoner_id = data['id']
else:
    print(f"Error: {response.status_code}")

#Make a request to the Riot Games API to get the summoner's current game information
url = f'https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summoner_id}?api_key={API_KEY}'
OpeningString = "As a challenger ranked coach, please provide three\
 short tips for a player in a League of Legends game, considering the\
  specific team compositions:\n\n"

# If the request was successful, print the champion being played by the player and the champions being played by the player's team
enemyList = []
teamList = []
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    #get player and team they are on
    for participant in data['participants']:
        if participant['summonerName'] == summoner_name:
            teamID = participant['teamId']
            OpeningString+=(f"Their Champion: {all_champion_id[participant['championId']]}\n")
    
    for player in data['participants']:
        if player['teamId'] == teamID:
            teamList.append(all_champion_id[player['championId']])
        else:
            enemyList.append(all_champion_id[player['championId']])

endingString = "\n\nPlease provide short tips on:\n\
1) How they can best play around her team's composition strengths\n\
2) How they can help cover the weaknesses of her team's composition\n\
3) How they can exploit the vulnerabilities of the enemy team's composition"

print(OpeningString,'Ally team: ', teamList, '\n', 'Enemy team: ', enemyList, endingString)

#1)Need to test Spectatev4 api and get info from request DONE
#2)get open ai bot working
#3)plug them together
#4)create ui/gui environment to run program