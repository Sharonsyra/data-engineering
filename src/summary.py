#!/usr/bin/env python

import json
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://codetest:password@database/codetest')

people = pd.read_sql('SELECT * FROM people', engine)


size_by_place_of_birth = people.groupby('place_of_birth').size().to_dict()

with open('/data/summary_by_pob.json', 'w') as f:
    json.dump(size_by_place_of_birth, f)

summary_by_date_of_birth = people.groupby('place_of_birth').first().to_dict()

with open('/data/summary_by_dob.json', 'w') as f:
    json.dump(summary_by_date_of_birth, f)