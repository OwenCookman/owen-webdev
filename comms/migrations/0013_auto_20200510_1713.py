# Generated by Django 3.0.4 on 2020-05-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comms', '0012_auto_20200510_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='If you already have a website, please add the URL here'),
        ),
    ]
