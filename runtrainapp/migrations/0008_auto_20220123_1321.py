# Generated by Django 3.1.5 on 2022-01-23 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('runtrainapp', '0007_auto_20220123_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runningtraining',
            name='training',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='runtrainapp.training'),
        ),
    ]
