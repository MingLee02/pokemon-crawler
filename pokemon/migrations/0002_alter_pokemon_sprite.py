# Generated by Django 3.2.6 on 2021-08-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='sprite',
            field=models.ImageField(blank=True, upload_to='sprite/'),
        ),
    ]
