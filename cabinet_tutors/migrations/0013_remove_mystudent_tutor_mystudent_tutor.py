# Generated by Django 4.1.5 on 2023-01-18 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cabinet_tutors', '0012_mystudent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mystudent',
            name='tutor',
        ),
        migrations.AddField(
            model_name='mystudent',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutors', to=settings.AUTH_USER_MODEL, verbose_name='Репетитор'),
        ),
    ]
