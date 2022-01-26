from django.shortcuts import render, get_object_or_404
from runtrainapp.managers.strava_api_manager import *
from runtrainapp.managers.context_manager import *
from runtrainapp.tables import *


def index(request):
    return render(request, 'admin/index.html')


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


def parse_responses(request):
    return render(request, 'admin/index.html')