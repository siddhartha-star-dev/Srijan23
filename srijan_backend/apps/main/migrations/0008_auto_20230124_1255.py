# Generated by Django 3.2.8 on 2023-01-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_sponsor_sponsor_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='sponsor_category',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='sponsor_type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]