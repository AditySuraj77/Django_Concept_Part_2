# Generated by Django 4.2.1 on 2023-06-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='t_file',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='team/'),
        ),
    ]
