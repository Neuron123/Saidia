# Generated by Django 3.1.7 on 2021-04-20 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientticket',
            name='current_uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
