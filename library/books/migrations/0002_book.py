# Generated by Django 4.0.5 on 2022-07-11 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=120, verbose_name='book_title')),
                ('description', models.TextField(null=True, verbose_name='description')),
                ('authot_name', models.CharField(max_length=120, verbose_name='authot_name')),
                ('number_of_pages', models.IntegerField(verbose_name='number_of_pages')),
                ('number_of_copies', models.IntegerField(verbose_name='number_of_copies')),
                ('publication_year', models.IntegerField(verbose_name='publication_year')),
                ('img_id', models.IntegerField(verbose_name='img_id')),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.category')),
                ('lang_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.language')),
            ],
        ),
    ]
