import django_tables2 as tables
from django_tables2 import A

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


class FormResponsesTable(tables.Table):
    response = tables.TemplateColumn('{{ record }}', order_by="id")
    show_details = tables.LinkColumn('response', args=[A('id')], order_by="id", text='Show details')

    class Meta:
        sequence = ('response', 'show_details')
        template_name = "tables/responsive-table.html"


class GeneratedResultInputTable(tables.Table):
    # No name for this column
    dsc = tables.Column(verbose_name="", orderable=False)
    main = tables.Column(verbose_name="Obecne treningi", orderable=False)
    first = tables.Column(verbose_name="Propozycja poprawnienia treningów o ~10%", orderable=False)
    second = tables.Column(verbose_name="Propozycja poprawnienia treningów o ~30%", orderable=False)

    class Meta:
        template_name = "tables/responsive-table.html"


class GeneratedResultOutputTable(tables.Table):
    # No name for this column
    dsc = tables.Column(verbose_name="", orderable=False)
    main = tables.Column(verbose_name="Obecne rezultaty", orderable=False)
    first = tables.Column(verbose_name="Rezultaty po poprawieniu treningów o ~10%", orderable=False)
    second = tables.Column(verbose_name="Rezultaty po poprawieniu treningów o ~30%", orderable=False)

    class Meta:
        template_name = "tables/responsive-table.html"