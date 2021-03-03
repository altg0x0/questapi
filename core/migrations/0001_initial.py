# Generated by Django 3.1.7 on 2021-03-02 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDateTime', models.DateTimeField(auto_now_add=True)),
                ('endDateTime', models.DateTimeField()),
                ('title', models.CharField(default='Unnamed questionnaire', max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['startDateTime'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionText', models.TextField()),
                ('questionType', models.CharField(choices=[('TEXT_ANSWER', 'Text answer'), ('MULTIPLE_CHOICE', 'Multiple choice'), ('MULTIPLE_RESPONSE', 'Multiple response')], max_length=100)),
                ('orderNumber', models.IntegerField(unique=True)),
                ('answer', models.TextField(max_length=10000)),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.questionnaire')),
            ],
            options={
                'ordering': ['questionText'],
            },
        ),
    ]