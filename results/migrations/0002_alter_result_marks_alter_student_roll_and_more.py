# Generated by Django 5.0.6 on 2024-05-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='marks',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='code',
            field=models.IntegerField(unique=True),
        ),
    ]
