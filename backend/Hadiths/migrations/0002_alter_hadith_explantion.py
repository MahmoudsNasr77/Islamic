# Generated by Django 5.1.2 on 2024-10-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hadiths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hadith',
            name='explantion',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]