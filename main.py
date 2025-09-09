import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


BASEURL = "https://www.thesportsdb.com/api/v1/json/123"

payload = {}
headers = {}


def fetch_all_leagues():
    url = f'{BASEURL}/all_leagues.php'
    response = requests.get(url)
    data = response.json()

    with open('All_leagues.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        fields = ['idLeague', 'strLeague', 'strSport', 'strGender', 'strCountry', 'strWebsite']
        writer.writerow(fields)  # header

        for league in data['leagues']:
            row = [league.get(k, '') for k in fields]
            writer.writerow(row)

def fetch_upcoming_events(league_id):
    url = f'{BASEURL}/lookupleague.php?id={league_id}'
    response = requests.get(url)
    data = response.json()

    #### USING DICTWRITER

    with open('Upcoming-League.csv','w',newline='') as file:
        fields = [
            'idLeague', 'strLeague', 'strSport', 'strGender', 'strCountry', 
            'strWebsite', 'strFacebook', 'strTwitter', 'strDescriptionEN'
        ]
        rows = [{k: league.get(k, '') for k in fields}  for league in data['leagues']]

        # fields = data['leagues'][0].keys() #if you want all fields

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader() 
        writer.writerows(rows)


#########################   Build dashboards / analytics  ###################

df = pd.read_csv('All_leagues.csv')

# Group and summarize
sport_counts = df['strSport'].value_counts()
country_counts = df['strCountry'].value_counts()

######################### Visualize the insights #################
# Bar chart of leagues per sport

sport_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Leagues per Sport')
plt.xlabel('Sport')
plt.ylabel('Number of Leagues')
# plt.savefig("my_plot.png") 
plt.show()

summary = df.groupby('strSport').size().reset_index(name='league_count')
summary.to_csv('league_summary.csv', index=False)
print(summary)