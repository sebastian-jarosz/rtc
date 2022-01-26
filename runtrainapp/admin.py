from django.contrib import admin

from .models import *

admin.site.register(TrainingProvider)
admin.site.register(RunningTrainingType)
admin.site.register(TrainingType)
admin.site.register(WellnessType)
admin.site.register(WarmupFrequency)
admin.site.register(OneKmTiming)
admin.site.register(FiveKmTiming)
admin.site.register(TenKmTiming)
admin.site.register(HalfMarathonTiming)
admin.site.register(MarathonTiming)
admin.site.register(TrainingTiming)
admin.site.register(Training)
admin.site.register(RunningTraining)
