# Create response context from provided args
from django_tables2 import Table, RequestConfig
from runtrainapp.forms import *
from runtrainapp.tables import *
from runtrainapp.utils.exceptions import *
from runtrainapp.utils.constants import *


# Configure table behavior
def configure_table(request, table):
    RequestConfig(request, paginate={"per_page": 20}).configure(table)


def create_response_context(*args):
    context = {}
    for arg in args:
        if isinstance(arg, AuthException):
            add_auth_exception_to_context(arg, context)
        elif isinstance(arg, HttpException):
            add_http_exception_to_context(arg, context)
        elif isinstance(arg, GeneratedResultInputTable):
            add_result_input_table_to_context(arg, context)
        elif isinstance(arg, GeneratedResultOutputTable):
            add_result_output_table_to_context(arg, context)
        elif isinstance(arg, Table):
            add_table_to_context(arg, context)
        elif isinstance(arg, Training):
            add_training_to_context(arg, context)
        elif isinstance(arg, RunningTraining):
            add_running_training_to_context(arg, context)
        elif isinstance(arg, FormResponse):
            add_form_response_to_context(arg, context)
        elif isinstance(arg, FormUser):
            add_form_user_to_context(arg, context)
        elif isinstance(arg, AddTrainingForm):
            add_training_form_to_context(arg, context)
        elif isinstance(arg, AddRunningTrainingForm):
            add_running_training_form_to_context(arg, context)
        elif isinstance(arg, GenerateTrainingForm):
            add_generate_training_form_to_context(arg, context)
        elif isinstance(arg, ShowTrainingForm):
            add_show_training_form_to_context(arg, context)
        elif isinstance(arg, ShowFormResponse):
            add_show_form_response_to_context(arg, context)
        elif isinstance(arg, Exception):
            add_general_exception_to_context(arg, context)

    return context


# Add Auth Exception to the context
def add_auth_exception_to_context(auth_exception, context):
    context[CONTEXT_AUTH_EXCEPTION] = auth_exception


# Add Auth Exception to the context
def add_http_exception_to_context(http_exception, context):
    context[CONTEXT_HTTP_EXCEPTION] = http_exception


# Add Table to the context
def add_table_to_context(table, context):
    context[CONTEXT_TABLE] = table


# Add Training to the context
def add_training_to_context(training, context):
    context[CONTEXT_TRAINING] = training


# Add Training to the context
def add_running_training_to_context(running_training, context):
    context[CONTEXT_RUNNING_TRAINING] = running_training


# Add Form Response to the context
def add_form_response_to_context(form_response, context):
    context[CONTEXT_FORM_RESPONSE] = form_response


# Add Form Response to the context
def add_form_user_to_context(form_user, context):
    context[CONTEXT_FORM_USER] = form_user


# Add Training Form to the context
def add_training_form_to_context(add_training_form, context):
    context[CONTEXT_ADD_TRAINING_FORM] = add_training_form


# Add Running Training Form to the context
def add_running_training_form_to_context(add_running_training_form, context):
    context[CONTEXT_ADD_RUNNING_TRAINING_FORM] = add_running_training_form


# Add Running Training Form to the context
def add_generate_training_form_to_context(generate_training_form, context):
    context[CONTEXT_GENERATE_TRAINING_FORM] = generate_training_form


# Add Show Training Form to the context
def add_show_training_form_to_context(show_training_form, context):
    context[CONTEXT_SHOW_TRAINING_FORM] = show_training_form


# Add Show Form Response to the context
def add_show_form_response_to_context(show_form_response, context):
    context[CONTEXT_SHOW_FORM_RESPONSE] = show_form_response


def add_general_exception_to_context(exception, context):
    context[CONTEXT_EXCEPTION] = str(exception)


def add_result_input_table_to_context(result_input_table, context):
    context[CONTEXT_RESULT_INPUT_TABLE] = result_input_table


def add_result_output_table_to_context(result_output_table, context):
    context[CONTEXT_RESULT_OUTPUT_TABLE] = result_output_table

