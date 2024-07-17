#!/usr/bin/env python

import json
from abc import abstractmethod, ABC

import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine


def query_data():
    engine = create_engine('postgresql://codetest:password@database/codetest')
    places = pd.read_sql('SELECT * FROM places', engine)
    people = pd.read_sql('SELECT * FROM people', engine)
    return people, places


class Summary(ABC):
    def __init__(self, places, people):
        self.places = places
        self.people = people

    def process(self):
        results = self.query()
        self.output(results)

    @abstractmethod
    def query(self) -> DataFrame:
        pass

    @property
    @abstractmethod
    def output_file(self):
        pass

    def output(self, results: DataFrame):
        # results.to_dict()
        with open(f'/data/{self.output_file}', 'w') as f:
            json.dump(results.to_dict(), f)


class PeopleCountByPlaceOfBirth(Summary):
    output_file = "people_size_by_pob.json"

    def query(self):
        return people.groupby('place_of_birth').size()


class FirstPersonByPlaceOfBirth(Summary):
    output_file = "first_by_place_of_birth.json"

    def query(self):
        return people.groupby('place_of_birth').first()


class PlacesCountByCountry(Summary):
    output_file = "places_size_per_country.json"

    def query(self):
        return places.groupby('country').size()


class FirstPlaceByCountry(Summary):
    output_file = "first_per_country.json"

    def query(self):
        return places.groupby('country').first()


class PlacesWithMoreThan100People(Summary):
    output_file = "places_with_more_than_100_people.json"

    def query(self):
        places_grouped = people.groupby('place_of_birth').size()
        return places_grouped[places_grouped > 100]


summaries = [
    PeopleCountByPlaceOfBirth,
    FirstPersonByPlaceOfBirth,
    PlacesCountByCountry,
    FirstPlaceByCountry,
    PlacesWithMoreThan100People
]

if __name__ == '__main__':
    people, places = query_data()
    for summary in summaries:
        summary(people, places).process()
