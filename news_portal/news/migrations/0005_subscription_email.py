# Generated by Django 3.2.8 on 2021-11-03 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20211103_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
