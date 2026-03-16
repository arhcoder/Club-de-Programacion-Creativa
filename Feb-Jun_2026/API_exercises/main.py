# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: March 11th, 2026
# | Last update..: March 16th, 2026
# | WhatIs.......: Dog API (API connections exercise)  - Main
# +----------------------------------------------------------------------------++

# ------------ Resources / Documentation involved -------------
# Dog API documentation: https://dogapi.dog/docs/api-v2
# Star Wars API documentation: https://swapi.dev/documentation
# SpaceX query launches API documentation: https://github.com/r-spacex/SpaceX-API/blob/master/docs/launches/v5/query.md

# -------------------------- Imports --------------------------
from API_requester_class import API_Requester

# ------------------------- Variables -------------------------
DogAPI_endpoint_facts = "https://dogapi.dog/api/v2/facts/"
DogAPI_facts_breeds = {
     "limit": "3"
}

DogAPI_endpoint_breeds = "https://dogapi.dog/api/v2/breeds/"
DogAPI_parameters_breeds = {
     "page[number]": "1",
     "page[size]": 2
}

StarWars_endpoint_species = "https://swapi.dev/api/species/"
StarWars_parameters_species = {
     "search": "togruta"
}

StarWars_endpoint_planets = "https://swapi.dev/api/planets/"
StarWars_parameters_planets = {
     "search": "naboo"
}

SpaceX_endpoint_launches = "https://api.spacexdata.com/v5/launches/"
SpaceX_parameters_launches = {
     "query": {
          "upcoming": True
     },
     "options": {
          "limit": 1,
          "sort": {
               "flight_number": "asc"
          }
     }
}

# --------------------------- Code ----------------------------
"""
dog_facts = API_Requester(endpoint=DogAPI_endpoint_facts, parameters=DogAPI_facts_breeds)
dog_facts.fetch_data(show_url=True, show_status_code=True, show_json=True)

dog_breeds = API_Requester(endpoint=DogAPI_endpoint_breeds, parameters=DogAPI_parameters_breeds)
dog_breeds.fetch_data(show_url=True, show_json=True)
"""

"""
starwars_species_facts = API_Requester(endpoint=StarWars_endpoint_species, parameters=StarWars_parameters_species)
starwars_species_facts.fetch_data(show_url=True, show_status_code=True, show_json=True)

starwars_planets_facts = API_Requester(endpoint=StarWars_endpoint_planets, parameters=StarWars_parameters_planets)
starwars_planets_facts.fetch_data(show_url=True, show_status_code=True, show_json=True)
"""

SpaceX_launches = API_Requester(endpoint=SpaceX_endpoint_launches, parameters=SpaceX_parameters_launches)
launch_data = SpaceX_launches.fetch_data(show_url=True, show_status_code=True, show_json=False)

for i in range(0, 4):
     print(f"""\nMission data #{i}
Success: {launch_data[i]['success']}
Detail: {launch_data[i]['details']}
Article: {launch_data[i]['links']['article']}""")