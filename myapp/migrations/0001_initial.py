# Generated by Django 4.0.2 on 2022-07-01 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=10000)),
                ('selectedText', models.CharField(max_length=10000)),
                ('sentiment', models.CharField(max_length=10000)),
            ],
        ),
    ]