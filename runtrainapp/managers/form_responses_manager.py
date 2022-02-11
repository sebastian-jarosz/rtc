import pandas as pd
import os

from runtrainapp.utils.form_parser import *


def process_csv(path=None):
    if path is None:
        current_path = os.getcwd()
        # Default path
        path = current_path + '/form_data/Ankieta dla biegaczy.csv'

    df = pd.read_csv(path)

    # Replace nan values with None
    formatted_df = df.where(pd.notnull(df), None)

    for i, row in formatted_df.iterrows():
        print('Parsing %i from %i rows' % (i, len(formatted_df)))
        data = parse_response_row(row)
        create_form_response_and_related_data_by_dict(data)


def produce_csv(path=None):
    if path is None:
        current_path = os.getcwd()
        # Default path
        path = current_path + '/form_data/Mapped - Ankieta dla biegaczy.csv'

    form_responses = get_all_form_responses()

    df = pd.DataFrame(list(form_responses.values()))

    # Convert values from bool to int
    df['other_trainings'] = df['other_trainings'].astype(int)
    df['wellness'] = df['wellness'].astype(int)

    print('Saving mapped from data to: ' + path)
    df.to_csv(path)
