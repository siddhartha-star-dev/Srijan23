# Generated by Django 3.2.8 on 2023-01-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_developers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developers',
            name='image',
            field=models.ImageField(upload_to='developers_images'),
        ),
    ]
