# Generated by Django 4.1.4 on 2022-12-08 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0002_sendmssg_c_date_alter_sendmssg_open_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendmssg',
            name='open_date_d',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sendmssg',
            name='open_date_m',
            field=models.IntegerField(default=1),
        ),
    ]
