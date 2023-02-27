import requests

# Define the API URL and parameters
url = 'https://www.nrl.com/draw//data'
params = {'competition': '111', 'round': '1', 'season': '2023'}

# Make a GET request to the API and get the response data
response = requests.get(url, params=params)
data = response.json()

# Parse the response data and print the fixtures

game_count = 0
for fixture in data['fixtures']:
    game_count = game_count + 1
    home_team = fixture['homeTeam']['nickName']
    away_team = fixture['awayTeam']['nickName']
    venue = fixture['venue']
    date_time = fixture['clock']['kickOffTimeLong']
    image_home = 'https://www.nrl.com/.theme/'+ home_team.lower() +'/badge.svg?bust=202302142313'
    image_away = 'https://www.nrl.com/.theme/'+ away_team.lower() +'/badge.svg?bust=202302142313'
    print(image_home)
    print(f"{home_team} vs {away_team} at {venue} on {date_time}")

print(game_count)