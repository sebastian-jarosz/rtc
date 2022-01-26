# Create response context from provided args
from django_tables2 import Table, RequestConfig

from runtrainapp.models import *
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
        elif isinstance(arg, Table):
            add_table_to_context(arg, context)
        elif isinstance(arg, Training):
            add_training_to_context(arg, context)

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