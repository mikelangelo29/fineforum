# Generated by Django 4.2.3 on 2023-07-25 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_remove_post_inserisci_immagine'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussione',
            name='inserisci_immagine',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
