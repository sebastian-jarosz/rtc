# Generated by Django 3.1.5 on 2022-02-13 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('runtrainapp', '0011_formuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formresponse',
            name='time_10km',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='runtrainapp.tenkmtiming'),
        ),
        migrations.AlterField(
            model_name='formresponse',
            name='time_1km',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='runtrainapp.onekmtiming'),
        ),
        migrations.AlterField(
            model_name='formresponse',
            name='time_21km',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='runtrainapp.halfmarathontiming'),
        ),
        migrations.AlterField(
            model_name='formresponse',
            name='time_42km',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='runtrainapp.marathontiming'),
        ),
        migrations.AlterField(
            model_name='formresponse',
            name='time_5km',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='runtrainapp.fivekmtiming'),
        ),
    ]
