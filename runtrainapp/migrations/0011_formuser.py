# Generated by Django 3.1.5 on 2022-02-13 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('runtrainapp', '0010_auto_20220213_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField()),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runtrainapp.formresponse')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
