# Generated by Django 5.1.2 on 2024-10-21 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hadith',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narrator', models.CharField(choices=[('البخاري', 'البخاري'), ('مسلم', 'مسلم'), ('الترمذي', 'الترمذي')], max_length=250)),
                ('text', models.TextField(max_length=5000)),
                ('explantion', models.TextField(max_length=5000)),
            ],
        ),
    ]
