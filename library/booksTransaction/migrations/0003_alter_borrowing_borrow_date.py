# Generated by Django 4.0.5 on 2022-08-05 05:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksTransaction', '0002_alter_borrowing_borrow_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowing',
            name='borrow_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 5, 5, 48, 14, 854029)),
        ),
    ]
