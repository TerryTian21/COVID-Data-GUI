"""CSC110 Fall 2021 Final Project: read_data
============================================
This Python module reads data from all the files in the raw_data_files folder and processes them.
The data is added to a countries dict that maps the name of countries to a Country Object
"""

import pandas as pd
import BackEnd.country_data as cd


def read_data(countries_dict: dict, data_file: pd.DataFrame, data_type: str) -> None:
    """Takes in a DataFrame and a data type as a string and adds the respective data for a country
       into the country object

    Preconditions:
        - data_type in ['cancellation_of_public_events',
                        'public_gathering_rules',
                        'face_coverings',
                        'mobility_trends',
                        'income_support',
                        'debt_relief',
                        'internal_movement',
                        'international_travel',
                        'public_transport',
                        'public_campaigns',
                        'school_closures',
                        'workplace_closures',
                        'stay_at_home_restrictions',
                        'containment_and_health_index',
                        'stringency_index',
                        'testing_policy',
                        'contact_tracing',
                        'vaccination_policy']
    """

    # iterates through the DataFrame
    for _, r in data_file.iterrows():
        if r[0] not in countries_dict:
            countries_dict[r[0]] = cd.Country(r[0], r[1], cd.Data([]), cd.Data([]), cd.Data([]),
                                              cd.Data([]), cd.Data([]), cd.Data([]),
                                              cd.Data([]), cd.Data([]), cd.Data([]),
                                              cd.Data([]), cd.Data([]), cd.Data([]),
                                              cd.Data([]), cd.Data([]), cd.Data([]),
                                              cd.Data([]), cd.Data([]), cd.Data([]),
                                              cd.Data([]), cd.Data([]), cd.Data([]),
                                              cd.Data([]), cd.Data([]), cd.Data([]),
                                              cd.Data([]), cd.Data([]), cd.Data([]), )

        # add a pair of [date, value] to the respective Data object in the current Country object
        getattr(countries_dict.get(r[0]), data_type).time_to_index.append([r[2], r[3]])


def load_files() -> dict:
    """Reads all data files, processes them into a dictionary mapping name of country to the
    respective country object

    Preconditions:

    """
    countries = {}  # a dictionary mapping the name of countries to their respective country objects

    ###############################################################################################
    #                                   Loading the policy Data Files                             #
    ###############################################################################################

    cancellation_of_public_events = pd.read_csv("../raw_data_files/public-events-covid.csv")
    public_gathering_rules = pd.read_csv("../raw_data_files/public-gathering-rules-covid.csv")
    face_coverings = pd.read_csv("../raw_data_files/face-covering-policies-covid.csv")
    debt_relief = pd.read_csv("../raw_data_files/debt-relief-covid.csv")
    income_support = pd.read_csv("../raw_data_files/income-support-covid.csv")
    internal_movement = pd.read_csv("../raw_data_files/internal-movement-covid.csv")
    international_travel = pd.read_csv("../raw_data_files/international-travel-covid.csv")
    public_transport = pd.read_csv("../raw_data_files/public-transport-covid.csv")
    public_campaigns = pd.read_csv("../raw_data_files/public-campaigns-covid.csv")
    school_closures = pd.read_csv("../raw_data_files/school-closures-covid.csv")
    workplace_closures = pd.read_csv("../raw_data_files/workplace-closures-covid.csv")
    stay_at_home_restrictions = pd.read_csv("../raw_data_files/stay-at-home-covid.csv")
    containment_and_health_index = pd.read_csv("../raw_data_files/"
                                               "covid-containment-and-health-index.csv")
    stringency_index = pd.read_csv("../raw_data_files/covid-stringency-index.csv")
    testing_policy = pd.read_csv("../raw_data_files/covid-19-testing-policy.csv")
    contact_tracing = pd.read_csv("../raw_data_files/covid-contact-tracing.csv")
    survivability_data = pd.read_csv("../raw_data_files/survivability.csv")

    ###############################################################################################
    #                                    Reading the policy Data Files                            #
    ###############################################################################################

    print("...reading policy data...")
    print("...reading file 1/16...")
    read_data(countries, cancellation_of_public_events, "cancellation_of_public_events")
    print("...reading file 2/16...")
    read_data(countries, public_gathering_rules, "public_gathering_rules")
    print("...reading file 3/16...")
    read_data(countries, face_coverings, "face_coverings")
    print("...reading file 4/16...")
    read_data(countries, income_support, "income_support")
    print("...reading file 5/16...")
    read_data(countries, debt_relief, "debt_relief")
    print("...reading file 6/16...")
    read_data(countries, internal_movement, "internal_movement")
    print("...reading file 7/16...")
    read_data(countries, international_travel, "internal_movement")
    print("...reading file 8/16...")
    read_data(countries, public_transport, "public_transport")
    print("...reading file 9/16...")
    read_data(countries, public_campaigns, "public_campaigns")
    print("...reading file 10/16...")
    read_data(countries, school_closures, "school_closures")
    print("...reading file 11/16...")
    read_data(countries, workplace_closures, "workplace_closures")
    print("...reading file 12/16...")
    read_data(countries, stay_at_home_restrictions, "stay_at_home_restrictions")
    print("...reading file 13/16...")
    read_data(countries, containment_and_health_index, "containment_and_health_index")
    print("...reading file 14/16...")
    read_data(countries, stringency_index, "stringency_index")
    print("...reading file 15/16...")
    read_data(countries, testing_policy, "testing_policy")
    print("...reading file 16/16...")
    read_data(countries, contact_tracing, "contact_tracing")
    print("...Policy data successfully Loaded...")
    print("...reading survivability data...")

    ###############################################################################################
    #                                Loading the survivability Data Files                         #
    ###############################################################################################

    # similar to the read_data function, this for loop processes the data from the survivability.csv
    # file as the file is formatted differently from the rest of the files and cannot be processed
    # using the read_data function. This loop isn't made into a function as it is only used once.
    for index, row in survivability_data.iterrows():
        if row["location"] not in countries:
            countries[row["location"]] = cd.Country(row["location"], row["iso_code"],
                                                    cd.Data([]), cd.Data([]), cd.Data([]),
                                                    cd.Data([]), cd.Data([]), cd.Data([]),
                                                    cd.Data([]), cd.Data([]), cd.Data([]),
                                                    cd.Data([]), cd.Data([]), cd.Data([]),
                                                    cd.Data([]), cd.Data([]), cd.Data([]),
                                                    cd.Data([]), cd.Data([]), cd.Data([]),
                                                    cd.Data([]), cd.Data([]), cd.Data([]),
                                                    cd.Data([]), cd.Data([]), cd.Data([]),
                                                    cd.Data([]), cd.Data([]), cd.Data([]),
                                                    )
        getattr(countries.get(row["location"]), "total_cases"). \
            time_to_index.append([row["date"], row["total_cases"]])
        getattr(countries.get(row["location"]), "total_deaths"). \
            time_to_index.append([row["date"], row["total_deaths"]])
        getattr(countries.get(row["location"]), "total_testing"). \
            time_to_index.append([row["date"], row["total_tests"]])
        getattr(countries.get(row["location"]), "total_vaccinations"). \
            time_to_index.append([row["date"], row["total_vaccinations"]])
        getattr(countries.get(row["location"]), "new_cases"). \
            time_to_index.append([row["date"], row["new_cases"]])
        getattr(countries.get(row["location"]), "new_deaths"). \
            time_to_index.append([row["date"], row["new_deaths"]])
        getattr(countries.get(row["location"]), "new_testing"). \
            time_to_index.append([row["date"], row["new_tests"]])
        getattr(countries.get(row["location"]), "new_vaccinations"). \
            time_to_index.append([row["date"], row["new_vaccinations"]])
        getattr(countries.get(row["location"]), "population"). \
            time_to_index.append([row["date"], row["population"]])
    print("...Survivability data successfully read...")
    print("...Now displaying window...")
    return countries
