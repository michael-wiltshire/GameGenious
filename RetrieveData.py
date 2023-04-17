import requests
import time

# Enter your Riot Games API key here
API_KEY = 'RGAPI-3eeb3239-f247-450e-9d9e-43ad1cc62b81'

# Enter the name of the summoner you want to check
summoner_id = 'ZNcgr9WQxPZsCxCc4OPWWk2A9P2_Cds_UmSx9xUs0xUWL3A'

# Make a request to the Riot Games API to get the summoner's current game information
url = f'https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summoner_id}?api_key={API_KEY}'

# If the request was successful, print the champion being played by the player and the champions being played by the player's team
while(True):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for participant in data['participants']:
            if participant['summonerName'] == summoner_name:
                print(f"You are playing as {participant['championName']}")
                print("Your team consists of:")
                for teammate in data['participants']:
                    if teammate['teamId'] == participant['teamId']:
                        print(teammate['championName'])
    else:
        print(f"Error: {response.status_code}")
    time.sleep(5)


#1)Need to test Spectatev4 api and get info from request
#2)get open ai bot working
#3)plug them together
#4)create ui/gui environment to run program