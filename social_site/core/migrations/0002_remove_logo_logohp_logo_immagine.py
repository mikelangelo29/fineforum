# Generated by Django 4.2.1 on 2023-06-12 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logo',
            name='logohp',
        ),
        migrations.AddField(
            model_name='logo',
            name='immagine',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
