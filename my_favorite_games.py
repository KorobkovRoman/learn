my_favorite_games= [
    {
        'Beast game series': ['Witcher 3', 'God of War', 'GTA', 'Horizon zero dawn', 'Borderlands' ,'Spyro', 'Need for speed', 'Assassin`s Creed'],
        'time_killer': {
            'Online game': ['Fall guys', 'Legue of legends', 'Overwatch', 'battlefield' 'Counter strike', 'Wot'],
            'Offline game': ['Snowrunner', 'minecraft', 'Portal', 'terraria', 'Mudrunner']
            }
    },
    {
        'name': 'Witcher 3 wild hunt',
        'genre': 'Action-adventure',
        'release': '18 may 2015 year',
        'similar games': ['God of war', 'Witcher 2', 'GreedFall', 'Assassin`s Creed Odyssey', 'Middle-Earth: shadow of war'],
        'platform': 'PC',
        'carrier': 'Steam'      
    },
    {

        'name': 'Spyro a hero`s tail',
        'genre': 'platformer',
        'release date': '9 november 2004 year',
        'similar games': ['Spyro the trilogy', 'Ratchet and clank'],
        'platform': 'PS 2',
        'carrier': 'disk'  
    },
    {
        'name': 'Red dead redemption 2',
        'genre': 'Action-adventure',
        'release date': '26 oktober 2018 year',
        'similar games': ['GTA 5', 'Witcher 3', 'Assassin`s Creed Odyssey'],
        'platform': 'PC',
        'carrier': 'Epic stor' 
    },
    {
        'name': 'Dying light',
        'genre': ' survival horror and action-adventure',
        'release date': '26 january 2015 year',
        'similar games': ['Dying light 2', 'Middle-Earth: shadow of war',],
        'platform': 'PC',
        'carrier': 'Steam' 
    },
    {
        'name': 'Rise of Nations: Rise of Legends',
        'genre': 'science fantasy real-time strategy',
        'release date': '9 may 2006 year',
        'similar games': ['Edge of empiries', 'Warhammer 40k', 'Warcraft 3'],
        'platform': 'PC',
        'carrier': 'Steam' 
    },
    {
        'name': 'Need for Speed Most Wanted',
        'genre': 'racing',
        'release date': '11 november 2005 year',
        'similar games': ['Forza horizon', 'Need for Speed Carbon', 'Need for Speed Heat'],
        'platform': 'PC',
        'carrier': 'disk' 
    },
    {
        'name': 'God of war',
        'genre': 'action-adventure',
        'release date': '20 april 2018 year',
        'similar games': ['Witcher 3', 'Horizon zero dawn', 'God of war Ragnarok', 'Borderlands', 'Control'],
        'platform': 'PS 5',
        'carrier': 'disk' 
    }
]
#print(my_favorite_games['time_killer'])
my_favorite_games_write_to_txt= open('my_favorite_games.txt', 'w')
for strng in my_favorite_games:
    my_favorite_games_write_to_txt.write(f'{strng}\n')
my_favorite_games_write_to_txt.close()
