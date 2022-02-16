from runtrainapp.models import *
from runtrainapp.utils.generator_constants import *
from runtrainapp.managers.data_manager import *
import pandas as pd


def get_main_and_improved_forms_dicts(main_form):
    # get_improved_forms
    # query should return only 2 objects - improved form by 0.1 and 0.3 (see generate_predictions)
    improved_form = FormUser.objects.filter(user=main_form.user, id__gt=main_form.id).order_by('id')
    improved_form = list(improved_form)

    # main form as list
    main_form_dict = main_form.response.__dict__

    # form improved by 0.1
    first_improved_form = improved_form[0]
    first_improved_form_dict = first_improved_form.response.__dict__

    # form improved by 0.3
    second_improved_form = improved_form[1]
    second_improved_form_dict = second_improved_form.response.__dict__

    return main_form_dict, first_improved_form_dict, second_improved_form_dict


# Get input data from forms:
# main form
# first improved form (10%)
# second improved form (30%)
def get_generator_input_df(main_form_dict, first_improved_form_dict, second_improved_form_dict):
    main_form_gen_input_values = []
    first_improved_gen_input_values = []
    second_improved_gen_input_values = []

    # key - column, value - question
    for column, question in Q_GENERATOR_INPUT.items():
        # if column is marked as a training reference one, get reference value description
        if column in GENERATOR_INPUT_TRN_REF_COLUMNS:
            main_form_gen_input_values.append(get_training_timing_description_by_id(main_form_dict[column]))
            first_improved_gen_input_values.append(get_training_timing_description_by_id(first_improved_form_dict[column]))
            second_improved_gen_input_values.append(get_training_timing_description_by_id(second_improved_form_dict[column]))
        # if column is warmup frequency ref
        elif column == COL_WARMUP:
            main_form_gen_input_values.append(get_warmup_freq_description_by_id(main_form_dict[column]))
            first_improved_gen_input_values.append(get_warmup_freq_description_by_id(first_improved_form_dict[column]))
            second_improved_gen_input_values.append(get_warmup_freq_description_by_id(second_improved_form_dict[column]))
        # if column doesn't contain reference value - pass value itself
        else:
            main_form_gen_input_values.append(main_form_dict[column])
            first_improved_gen_input_values.append(first_improved_form_dict[column])
            second_improved_gen_input_values.append(second_improved_form_dict[column])

    input_df_data = {
        "dsc": Q_GENERATOR_INPUT.values(),
        "main": main_form_gen_input_values,
        "first": first_improved_gen_input_values,
        "second": second_improved_gen_input_values
    }

    input_df = pd.DataFrame(input_df_data)

    # Replace boolean with desc
    input_df = input_df.astype(str).replace({'False': 'Nie', 'True': 'Tak'})

    return input_df


# Get input data from forms:
# main form
# first improved form (10%)
# second improved form (30%)
def get_generator_output_df(main_form_dict, first_improved_form_dict, second_improved_form_dict):
    main_form_gen_output_values = []
    first_improved_gen_output_values = []
    second_improved_gen_output_values = []

    # key - column, value - question
    for column, question in Q_GENERATOR_OUTPUT.items():
        main_dsc = get_distance_timing_desc_by_col_name_and_id(column, main_form_dict[column])
        main_form_gen_output_values.append(main_dsc)
        first_dsc = get_distance_timing_desc_by_col_name_and_id(column, first_improved_form_dict[column])
        first_improved_gen_output_values.append(first_dsc)
        second_dsc = get_distance_timing_desc_by_col_name_and_id(column, second_improved_form_dict[column])
        second_improved_gen_output_values.append(second_dsc)

    output_df_data = {
        "dsc": Q_GENERATOR_OUTPUT.values(),
        "main": main_form_gen_output_values,
        "first": first_improved_gen_output_values,
        "second": second_improved_gen_output_values
    }

    output_df = pd.DataFrame(output_df_data)

    # Replace boolean with desc
    output_df = output_df.astype(str).replace({'False': 'Nie', 'True': 'Tak'})

    return output_df


# Get specific distance timing basing on column name and ref id
# column_name - value used to match proper model
# id - reference id
def get_distance_timing_desc_by_col_name_and_id(col_name, timing_id):
    if col_name == COL_TIME_1KM:
        description = get_timing_by_model_and_id(OneKmTiming, timing_id).description
    elif col_name == COL_TIME_5KM:
        description = get_timing_by_model_and_id(FiveKmTiming, timing_id).description
    elif col_name == COL_TIME_10KM:
        description = get_timing_by_model_and_id(TenKmTiming, timing_id).description
    elif col_name == COL_TIME_21KM:
        description = get_timing_by_model_and_id(HalfMarathonTiming, timing_id).description
    elif col_name == COL_TIME_42KM:
        description = get_timing_by_model_and_id(MarathonTiming, timing_id).description

    return description

