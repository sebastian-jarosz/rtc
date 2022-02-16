import django_tables2 as tables
from django_tables2 import A

from .models import *


class TrainingTable(tables.Table):
    user = tables.Column(verbose_name="Użytkownik")
    type = tables.Column(verbose_name="Typ")
    start_date = tables.TemplateColumn('{{ record.get_formatted_start_date }}', verbose_name="Czas rozpoczęcia")
    time = tables.TemplateColumn('{{ record.get_formatted_time }}', verbose_name="Długość treningu (w minutach)")
    provider = tables.Column(verbose_name="Sposób dodania")
    external_code = tables.Column(verbose_name="Zewnętrzne ID")

    class Meta:
        model = Training
        template_name = "tables/responsive-table.html"


class RunningTrainingTable(tables.Table):
    training = tables.LinkColumn('training', args=[A('training.id')], verbose_name="Trening")
    type = tables.Column(verbose_name="Typ")

    # Columns from Training Model
    user = tables.TemplateColumn('{{ record.training.user }}', verbose_name="Użytkownik")
    start_date = tables.TemplateColumn('{{ record.training.get_formatted_start_date }}', verbose_name="Czas rozpoczęcia")
    time = tables.TemplateColumn('{{ record.training.get_formatted_time }}', verbose_name="Długość treningu")
    provider = tables.TemplateColumn('{{ record.training.provider }}', verbose_name="Sposób dodania")
    external_code = tables.TemplateColumn('{{ record.training.external_code }}', verbose_name="Zewnętrzne ID")

    # Columns from RunningTraining model
    distance = tables.TemplateColumn('{{ record.get_distance_km }}', verbose_name='Dystans w km')
    avg_speed = tables.TemplateColumn('{{ record.get_avg_speed_km_per_h }}', verbose_name='Prędkość w km/h')
    segments_amount = tables.TemplateColumn('{{ record.segments_amount }}', verbose_name='Ilość segmentów')

    class Meta:
        model = RunningTraining
        template_name = "tables/responsive-table.html"


class FormResponsesTable(tables.Table):
    response = tables.TemplateColumn('{{ record }}', order_by="id")
    show_details = tables.LinkColumn('response', args=[A('id')], order_by="id", text='Więcej informacji')

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