# Generated by Django 4.1 on 2022-08-08 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id',
                 models.BigAutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID',
                     ),
                 ),
                ('content', models.CharField(max_length=255)),
            ],
        ),
    ]