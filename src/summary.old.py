#!/usr/bin/env python

import json
import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('postgresql://codetest:password@database/codetest')
people = pd.read_sql('SELECT * FROM people', engine)

size_by_place_of_birth = people.groupby('place_of_birth').size().to_dict()

with open('/data/people_size_by_pob.json', 'w') as f:
    json.dump(size_by_place_of_birth, f)

first_by_place_of_birth = people.groupby('place_of_birth').first().to_dict()

with open('/data/first_by_place_of_birth.json', 'w') as f:
    json.dump(first_by_place_of_birth, f)

places = pd.read_sql('SELECT * FROM places', engine)

places_size_per_country = places.groupby('country').size().to_dict()

with open('/data/places_size_per_country.json', 'w') as f:
    json.dump(places_size_per_country, f)

first_per_country = places.groupby('country').first().to_dict()

with open('/data/first_per_country.json', 'w') as f:
    json.dump(first_per_country, f)

places_grouped = people.groupby('place_of_birth').size()
places_with_more_than_100_people = places_grouped[places_grouped > 100].to_dict()

with open('/data/places_with_more_than_100_people.json', 'w') as f:
    json.dump(places_with_more_than_100_people, f)