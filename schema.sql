drop table if exists people;

drop table if exists places;

create table places
(
    id   serial
        constraint places_pk
            primary key,
    city varchar,
    county varchar,
    country varchar
);

create table people
(
    id   serial
        constraint people_pk
            primary key,
    given_name varchar,
    family_name  varchar,
    date_of_birth date,
    place_of_birth varchar,
    city_id integer
        constraint people_places_fk
            references places
);
