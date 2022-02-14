import pandas as pd
import os

from runtrainapp.utils.form_parser import *


def process_csv(file=None):
    if file is None:
        current_path = os.getcwd()
        # Default path
        file = current_path + '/form_data/Ankieta dla biegaczy.csv'

    df = pd.read_csv(file)

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

    df = create_df_from_form_responses_obj_list(list(form_responses.values()))

    print('Saving mapped from data to: ' + path)
    df.to_csv(path)


def create_df_from_form_responses_obj_list(form_responses_obj_list):
    df = pd.DataFrame(form_responses_obj_list)

    # Convert values from bool to int
    df['other_trainings'] = df['other_trainings'].astype(int)
    df['wellness'] = df['wellness'].astype(int)

    # Drop id column if exists
    df = df.drop(labels=['id'], axis=1, errors='ignore')

    return df
