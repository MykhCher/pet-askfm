# Generated by Django 4.1 on 2022-08-14 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_alter_answer_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]