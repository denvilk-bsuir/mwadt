# Generated by Django 4.2.1 on 2023-09-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
