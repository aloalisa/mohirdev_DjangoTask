# Generated by Django 5.0.1 on 2024-02-20 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0004_news_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='view_count',
        ),
    ]
