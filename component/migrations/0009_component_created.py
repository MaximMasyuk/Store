# Generated by Django 2.2.7 on 2019-11-30 17:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0008_component_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]