# Generated by Django 3.2.8 on 2023-01-18 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_event_to_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='sponsor_type',
            field=models.CharField(choices=[('title', 'Title'), ('decoration', 'Decoration'), ('associate', 'Associate'), ('strategic', 'Strategic'), ('prize', 'Prize'), ('logistics', 'Logistics'), ('style', 'Style'), ('health', 'Health'), ('beverage', 'Beverage'), ('online', 'Online')], default='Title', max_length=20),
            preserve_default=False,
        ),
    ]
