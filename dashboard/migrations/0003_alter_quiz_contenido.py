# Generated by Django 4.1 on 2022-12-05 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_quiz_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='contenido',
            field=models.CharField(max_length=20000),
        ),
    ]
