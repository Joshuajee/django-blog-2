# Generated by Django 5.0.3 on 2024-04-15 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 15, 9, 42, 2, 219073)),
        ),
    ]