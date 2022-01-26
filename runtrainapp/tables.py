import django_tables2 as tables
from .models import *


class TrainingTable(tables.Table):
    time = tables.TemplateColumn('{{ record.get_formatted_time }}')
    start_date = tables.TemplateColumn('{{ record.get_formatted_start_date }}')

    class Meta:
        model = Training
        template_name = "tables/responsive-table.html"


class RunningTrainingTable(tables.Table):
    # Columns from Training Model
    user = tables.TemplateColumn('{{ record.training.user }}')
    start_date = tables.TemplateColumn('{{ record.training.get_formatted_start_date }}')
    time = tables.TemplateColumn('{{ record.training.get_formatted_time }}')
    provider = tables.TemplateColumn('{{ record.training.provider }}')
    external_code = tables.TemplateColumn('{{ record.training.external_code }}')

    # Columns from RunningTraining model
    distance = tables.TemplateColumn('{{ record.get_distance_km }}', verbose_name='Distance in km')
    avg_speed = tables.TemplateColumn('{{ record.get_avg_speed_km_per_h }}', verbose_name='Avg Speed in km/h')

    class Meta:
        model = RunningTraining
        template_name = "tables/responsive-table.html"
