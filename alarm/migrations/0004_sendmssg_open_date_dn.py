# Generated by Django 4.1.4 on 2022-12-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0003_sendmssg_open_date_d_sendmssg_open_date_m'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendmssg',
            name='open_date_dn',
            field=models.IntegerField(default=1),
        ),
    ]
