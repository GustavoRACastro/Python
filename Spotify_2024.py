import pandas as pd
import matplotlib.pyplot as plt

Spotify_2024 = "https://github.com/GustavoRACastro/Python/blob/main/Spotify_2024_Global_Streaming_Data.csv"
Spotify.pd.read_csv(Spotify_2024)
Spotify.info()
Spotify.describe()
Spotify.head(10)

## Top 10 Artists
Top_Artists = Spotify.groupby('Artist')['Total Streams (Millions)'].sum().sort_values(ascending=False).head(10)
print(Top_Artists)

plt.figure(figsize=(15,6))
plt.barplot(x=Top_Artists.index, y=Top_Artists.values)

for i, v in enumerate(Top_Artists.values):
    plt.text(i, v + 0.5, f'{v:.2f}', ha='center', va='bottom')

plt.xlabel('Artist')
plt.ylabel('Total Streams')
plt.title('Top 10 Artists: Numb. Streams')
plt.show()

## Top 7 Albuns
Top_Albuns = Spotify.groupby('Album')['Total Hours Streamed (Millions)'].sum().sort_values(ascending=False).head(7)
print(Top_Albuns)

plt.figure(figsize=(18,6))
plt.barplot(x=Top_Albuns.index, y=Top_Albuns.values)

for i, v in enumerate(Top_Albuns.values):
    plt.text(i, v + 0.5, f'{v:.2f}', ha='center', va='bottom')

plt.xlabel('Album')
plt.ylabel('Total Stream Hours')
plt.title('Top 10 Albuns: Hours Streaming')
plt.show()

## Top 5 Genres last 30 Days
Top_Genres = Spotify.groupby('Genre')['Streams Last 30 Days (Millions)'].sum().sort_values(ascending=False).head(5)
print(Top_Genres)

plt.figure(figsize=(10,6))
plt.barplot(x=Top_Genres.index, y=Top_Genres.values)

for i, v in enumerate(Top_Genres.values):
    plt.text(i, v + 0.5, f'{v:.2f}', ha='center', va='bottom')

plt.xlabel('Genre')
plt.ylabel('Streams')
plt.title('Top 5 Genres: Last 30 Days Streams')
plt.show()

## Top Genres Brazil
Brazil_Plays = Spotify[Spotify['Country'] == 'Brazil']  # Filtrando somente o Brasil
Brazil_Plays = Brazil_Plays.groupby('Genre').size().sort_values(ascending=False)  # Agrupando por gênero e contando
print(Brazil_Plays)

plt.figure(figsize=(6,6))
plt.pie(Brazil_Plays, labels=Brazil_Plays.index, autopct='%1.1f%%', startangle=90)
plt.title('Brazilian: Top Genres')
plt.show()

## Free x Premium Users
Users_Time = Spotify.groupby('Platform Type')['Total Hours Streamed (Millions)'].sum().sort_values(ascending=False)
print(Users_Time)

plt.figure(figsize=(6,6))
plt.pie(Users_Time, labels=Users_Time.index, autopct='%1.1f%%', startangle=90)
plt.title('Users: Free x Premium')
plt.show()