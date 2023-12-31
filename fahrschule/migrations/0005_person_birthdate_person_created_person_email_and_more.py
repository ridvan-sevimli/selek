# Generated by Django 4.2.4 on 2023-08-28 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fahrschule', '0004_remove_person_birthdate_remove_person_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birthDate',
            field=models.DateTimeField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='created',
            field=models.DateTimeField(null=True, verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='faberNumber',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='ort',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='phoneNumber',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='plz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='street',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
