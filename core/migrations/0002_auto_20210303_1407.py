# Generated by Django 3.1.7 on 2021-03-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='startDateTime',
            field=models.DateTimeField(editable=False),
        ),
    ]
