# Generated by Django 4.0.5 on 2022-08-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='town',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
