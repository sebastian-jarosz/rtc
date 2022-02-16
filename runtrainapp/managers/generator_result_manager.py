from runtrainapp.models import *
from runtrainapp.utils.generator_constants import *
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

    # key question, value question id
    for key, value in Q_GENERATOR_INPUT.items():
        main_form_gen_input_values.append(main_form_dict[key])
        first_improved_gen_input_values.append(first_improved_form_dict[key])
        second_improved_gen_input_values.append(second_improved_form_dict[key])

    input_df_data = {
        "": Q_GENERATOR_INPUT.values(),
        "Obecne treningi": main_form_gen_input_values,
        "Propozycja poprawnienia treningów o 10%": first_improved_gen_input_values,
        "Propozycja poprawnienia treningów o 30%": second_improved_gen_input_values
    }

    input_df = pd.DataFrame(input_df_data)

    return input_df


# Get input data from forms:
# main form
# first improved form (10%)
# second improved form (30%)
def get_generator_output_df(main_form_dict, first_improved_form_dict, second_improved_form_dict):
    main_form_gen_output_values = []
    first_improved_gen_output_values = []
    second_improved_gen_output_values = []

    # key question, value question id
    for key, value in Q_GENERATOR_OUTPUT.items():
        main_form_gen_output_values.append(main_form_dict[key])
        first_improved_gen_output_values.append(first_improved_form_dict[key])
        second_improved_gen_output_values.append(second_improved_form_dict[key])

    output_df_data = {
        "": Q_GENERATOR_OUTPUT.values(),
        "Obecne rezultaty": main_form_gen_output_values,
        "Rezultaty po poprawieniu treningów o 10%": first_improved_gen_output_values,
        "Rezultaty po poprawieniu treningów o 30%": second_improved_gen_output_values
    }

    output_df = pd.DataFrame(output_df_data)

    return output_df
