# Generated by Django 3.1.7 on 2021-04-21 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientticket', '0003_remove_clientticket_ticket_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientticket',
            name='current_uid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]