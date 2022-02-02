"""CSC110 Fall 2021 Final Project: Country and Date Classes
===========================================================
This Python module contains two classes that are used to hold information about each country
in the data files.
The data class holds information about each date-index pair
The Country class holds information about a country, such as its name, its country code
as well as every covid-19 policy such as face coverings and survivability data such as new cases.
"""


class Data:
    """Information about the value of a given policy rating and the corresponding date
    for a set of days.

    Attributes:
        - time_to_index: list of data in the format of date(year, month, day)
                         and index represented as an int

    Representation Invariants:

    """

    time_to_index: [[str, int]]

    def __init__(self, time_to_index: list) -> None:
        self.time_to_index = time_to_index


class Country:
    """A Country which has implemented various kinds of policies to fight against COVID-19
    and has data recorded for the different policies.

    Attributes:
        - name: name of the country
        - country_code: the country code of the country
        - cancellation_of_public_events: cancellation of public events index from 0 to 2
        - public_gathering_rules: restrictions on public gathering index from 0 to 4
        - face_coverings: face covering index from 0 to 4
        - mobility_trends: mobility trend index from 1 to 6
        - income_support: income support index from 0 to 2
        - debt_relief: debt relief index from 0 to 2
        - internal_movement: restrictions on internal movement index from 0 to 2
        - international_travel: restrictions international travel index from 0 to 4
        - public_transport: close public transport index from 0 to 2
        - public_campaigns: public campaign information from o to 2
        - school_closures: school closure index from 0 to 3
        - workplace_closures: workplace closure index from 0 to 3
        - stay_at_home_restrictions: stay at home index from 0 to 3
        - containment_and_health_index: containment and health index from 0 to 100
        - stringency_index: stringency index from o to 100
        - testing_policy: testing policy index from 0 to 3
        - contact_tracing: contact tracing index from 0 to 2
        - vaccination_policy: vaccination policy index from 0 to 5
        - total_cases: number of total COVID cases in a country
        - total_deaths: number of total deaths in a country
        - total_testing: number of total testings done in a country
        - total_vaccinations: number of total vaccinations in a country
        - new_cases: number of total new COVID cases in a country per day
        - new_deaths: number of total new deaths in a country per day
        - new_testing: number of total new testings done in a country per day
        - new_vaccinations: number of new vaccinations done in a country per day
        - population: number of total population in a country

    Representation Invariants:
        - name != ''
        - country_code != ''
    """
    name: str
    country_code: str
    cancellation_of_public_events: Data
    public_gathering_rules: Data
    face_coverings: Data
    mobility_trends: Data
    income_support: Data
    debt_relief: Data
    internal_movement: Data
    international_travel: Data
    public_transport: Data
    public_campaigns: Data
    school_closures: Data
    workplace_closures: Data
    stay_at_home_restrictions: Data
    containment_and_health_index: Data
    stringency_index: Data
    testing_policy: Data
    contact_tracing: Data
    vaccination_policy: Data
    total_cases: Data
    total_deaths: Data
    total_testing: Data
    total_vaccinations: Data
    new_cases: Data
    new_deaths: Data
    new_testing: Data
    new_vaccinations: Data
    population: Data

    def __init__(self, name: str, country_code: str,
                 cancellation_of_public_events: Data,
                 public_gathering_rules: Data,
                 face_coverings: Data,
                 mobility_trends: Data,
                 income_support: Data,
                 debt_relief: Data,
                 internal_movement: Data,
                 international_travel: Data,
                 public_transport: Data,
                 public_campaigns: Data,
                 school_closures: Data,
                 workplace_closures: Data,
                 stay_at_home_restrictions: Data,
                 containment_and_health_index: Data,
                 stringency_index: Data,
                 testing_policy: Data,
                 contact_tracing: Data,
                 vaccination_policy: Data,
                 total_cases: Data,
                 total_deaths: Data,
                 total_testing: Data,
                 total_vaccinations: Data,
                 new_cases: Data,
                 new_deaths: Data,
                 new_testing: Data,
                 new_vaccinations: Data,
                 population: Data,) -> None:

        self.name = name
        self.country_code = country_code
        self.cancellation_of_public_events = cancellation_of_public_events
        self.public_gathering_rules = public_gathering_rules
        self.face_coverings = face_coverings
        self.mobility_trends = mobility_trends
        self.income_support = income_support
        self.debt_relief = debt_relief
        self.internal_movement = internal_movement
        self.international_travel = international_travel
        self.public_transport = public_transport
        self.public_campaigns = public_campaigns
        self.school_closures = school_closures
        self.workplace_closures = workplace_closures
        self.stay_at_home_restrictions = stay_at_home_restrictions
        self.containment_and_health_index = containment_and_health_index
        self.stringency_index = stringency_index
        self.testing_policy = testing_policy
        self.contact_tracing = contact_tracing
        self.vaccination_policy = vaccination_policy
        self.total_cases = total_cases
        self.total_deaths = total_deaths
        self.total_testing = total_testing
        self.total_vaccinations = total_vaccinations
        self.new_cases = new_cases
        self.new_deaths = new_deaths
        self.new_testing = new_testing
        self.new_vaccinations = new_vaccinations
        self.population = population
