# Generated by Django 2.2.7 on 2019-12-13 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0010_component_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='image',
            field=models.ImageField(null=True, upload_to='user_flowers'),
        ),
    ]