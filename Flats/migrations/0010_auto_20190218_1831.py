# Generated by Django 2.1.7 on 2019-02-18 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flats', '0009_auto_20190218_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatdetails',
            name='date_of_posting',
            field=models.DateField(auto_now=True),
        ),
    ]
