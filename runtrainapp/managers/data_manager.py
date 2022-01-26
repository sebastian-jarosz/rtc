from runtrainapp.models import *


def get_training_provider_by_name(provider_name):
    return TrainingProvider.objects.get(description__iexact=provider_name)


def get_training_type_by_id(type_id):
    return TrainingType.objects.get(id=type_id)


def get_running_training_type_by_id(type_id):
    return RunningTrainingType.objects.get(id=type_id)


def get_trainings_amount_by_provider_and_user(provider, user):
    return Training.objects.filter(user=user, provider=provider).count()


# Create Training object and save into DB or return existing object
def create_training(user, provider, training_type, start_date, elapsed_time, external_code):
    obj, created = Training.objects.get_or_create(
        user=user,
        type=training_type,
        start_date=start_date,
        time=elapsed_time,
        provider=provider,
        external_code=external_code
    )

    if created:
        print("Training created\t- User: %s\t Provider: %s\t External_code: %s" % (user.username, provider.description, external_code))
    else:
        print("Training exists\t- User: %s\t Provider: %s\t External_code: %s" % (user.username, provider.description, external_code))

    return obj


# Create Training object and save into DB or return existing object
def create_running_training(training, distance, avg_speed, running_training_type, segments=1):
    # This syntax checking only if Running Training for specific training is unique
    obj, created = RunningTraining.objects.get_or_create(
        training=training,
        defaults={
            'type': running_training_type,
            'distance': distance,
            'avg_speed': avg_speed,
            'segments_amount': segments
        }

    )

    if created:
        print("Running Training created\t- Training ID: %i\t Distance: %f\t Avg Speed: %f" % (training.id, distance, avg_speed))
    else:
        print("Running Training exists\t- Training ID: %i\t Distance: %f\t Avg Speed: %f" % (training.id, distance, avg_speed))

    return obj