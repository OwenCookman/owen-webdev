# Generated by Django 3.0.4 on 2020-04-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comms', '0003_auto_20200425_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deposit_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='final_paid',
            field=models.BooleanField(default=False),
        ),
    ]
