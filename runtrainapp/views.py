from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from runtrainapp.forms import *
from runtrainapp.managers.generator_manager import generate_predictions
from runtrainapp.managers.strava_api_manager import *
from runtrainapp.managers.context_manager import *
from runtrainapp.managers.form_responses_manager import *
from runtrainapp.managers.learn_manager import *
from runtrainapp.tables import *


def index(request):
    return render(request, 'index.html')


def page_not_found(request, exception):
    return render(request, 'admin/404.html')


def profile(request):
    context_args = []

    try:
        result = get_list_of_running_activities(request.user)
    except Exception as e:
        context_args.append(e)

    context = create_response_context(*context_args)

    return render(request, 'account/profile.html', context)


# List all trainings
def list_all_trainings(request):
    all_trainings = Training.objects.all()
    training_table = TrainingTable(all_trainings)

    configure_table(request, training_table)
    context = create_response_context(training_table)

    return render(request, 'training/list_training.html', context)


# List all user trainings
def list_all_user_trainings(request):
    all_user_trainings = Training.objects.filter(user=request.user)
    training_table = TrainingTable(all_user_trainings)

    configure_table(request, training_table)
    context = create_response_context(training_table)

    return render(request, 'training/list_training.html', context)


# Show specified training
def training(request, training_id):
    training_obj = get_object_or_404(Training, pk=training_id)

    context = create_response_context(training_obj)

    return render(request, 'training/training.html', context)


def add_training(request):
    context_args = []
    if request.method == 'POST':
        try:
            training_obj = parse_training_request(request)
            context_args.append(training_obj)
        except Exception as e:
            # Add exception in case of failure
            context_args.append(e)

    # If request.method = GET
    users = get_user_list(request.user, request.user.is_staff)
    form = AddTrainingForm(get_training_types_description_list(), users, request.user.is_staff)
    context_args.append(form)

    context = create_response_context(*context_args)

    return render(request, 'training/add_training.html', context)


def add_running_training(request):
    context_args = []
    if request.method == 'POST':
        try:
            running_training_obj = parse_running_training_request(request)
            context_args.append(running_training_obj)
        except Exception as e:
            # Add exception in case of failure
            context_args.append(e)

    # If request.method = GET
    users = get_user_list(request.user, request.user.is_staff)
    form = AddRunningTrainingForm(users, get_running_training_types_description_list(), request.user.is_staff)
    context_args.append(form)

    context = create_response_context(*context_args)

    return render(request, 'training/add_running_training.html', context)


# List all running trainings
def list_all_running_trainings(request):
    all_running_trainings = RunningTraining.objects.all()
    running_training_table = RunningTrainingTable(all_running_trainings)

    configure_table(request, running_training_table)
    context = create_response_context(running_training_table)

    return render(request, 'training/list_running_training.html', context)


# List all user running trainings
def list_all_user_running_trainings(request):
    all_running_trainings = RunningTraining.objects.filter(training__user=request.user)
    running_training_table = RunningTrainingTable(all_running_trainings)

    configure_table(request, running_training_table)
    context = create_response_context(running_training_table)

    return render(request, 'training/list_running_training.html', context)


def form_management(request):
    form_responses_count = get_all_form_responses_count()
    context = {
        'form_responses_count': form_responses_count
    }
    return render(request, 'admin/form_management.html', context)


def form_responses(request):
    all_form_responses = get_all_form_responses()
    form_responses_table = FormResponsesTable(all_form_responses)

    configure_table(request, form_responses_table)
    context = create_response_context(form_responses_table)

    return render(request, 'admin/list_form_response.html', context)


def response(request, form_response_id):
    response_obj = get_object_or_404(FormResponse, pk=form_response_id)

    context = create_response_context(response_obj)

    return render(request, 'admin/form_response.html', context)


def parse_responses(request):
    if request.method == 'POST':
        responses_file = request.FILES.get('files')
        process_csv(responses_file)

    return HttpResponse("parse_responses invoked")


def write_responses(request):
    produce_csv(None)
    return HttpResponse("parse_responses invoked")


def learn_management(request):
    form_responses_count = get_all_form_responses_count()
    context = {
        'form_responses_count': form_responses_count
    }
    return render(request, 'admin/learn_management.html')


def teach(request):
    if request.method == 'POST':
        do_not_map_data = request.POST.get('doNotMapData')

        if do_not_map_data == 'false':
            # Produce CSV mapped file for learning process
            produce_csv()
            learn_model()

    return HttpResponse("teach invoked")


def generate_training(request):
    context_args = []
    if request.method == 'POST':
        try:
            # Form user obj created from UI data
            form_user = parse_generate_training_request(request)
            generate_predictions(form_user)

            context_args.append(form_user)
        except Exception as e:
            # Add exception in case of failure
            context_args.append(e)

    # Generate Training Form Init
    form = GenerateTrainingForm()
    context_args.append(form)

    context = create_response_context(*context_args)

    return render(request, 'training/generate_training.html', context)
