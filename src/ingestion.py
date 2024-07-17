#!/usr/bin/env python

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://codetest:password@database/codetest')

places = pd.read_csv('/data/places.csv')
people = pd.read_csv('/data/people.csv')

people.to_sql('people', engine, if_exists='replace', index=False)
places.to_sql('places', engine, if_exists='replace', index=False)
