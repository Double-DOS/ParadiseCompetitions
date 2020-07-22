# Generated by Django 3.0.7 on 2020-07-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paradise', '0015_auto_20200722_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='ticket_number_end',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='ticket_number_start',
        ),
        migrations.AddField(
            model_name='competition',
            name='tickets_per_letter',
            field=models.CharField(choices=[('100', '100'), ('200', '200'), ('300', '300'), ('400', '400'), ('500', '500'), ('600', '600')], default='100', max_length=3),
        ),
    ]