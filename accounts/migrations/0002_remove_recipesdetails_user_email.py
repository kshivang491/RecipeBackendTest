# Generated by Django 4.2.3 on 2024-05-10 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipesdetails',
            name='user_email',
        ),
    ]
