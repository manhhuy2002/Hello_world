# Generated by Django 4.0.5 on 2022-09-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='book',
            field=models.ManyToManyField(blank=True, null=True, to='book_web.book'),
        ),
    ]
