# Generated by Django 2.1 on 2018-08-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dateCreation',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='datePublic',
            field=models.DateTimeField(),
        ),
    ]
