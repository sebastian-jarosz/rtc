import pandas as pd

from runtrainapp.utils.form_parser import *


def process_csv(path):
    df = pd.read_csv('Ankieta dla biegaczy.csv')

    # Replace nan values with None
    formatted_df = df.where(pd.notnull(df), None)

    for i, row in formatted_df.iterrows():
        data = parse_response_row(row)
        create_form_response_and_related_data_by_dict(data)


def produce_csv(path):
    form_responses = get_all_form_responses()

    df = pd.DataFrame(list(form_responses.values()))

    # Convert values from bool to int
    df['other_trainings'] = df['other_trainings'].astype(int)
    df['wellness'] = df['wellness'].astype(int)

    df.to_csv('Mapped - Ankieta dla biegaczy.csv')