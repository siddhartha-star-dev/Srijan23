# Generated by Django 3.2.8 on 2023-01-13 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_developers_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='to_publish',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
