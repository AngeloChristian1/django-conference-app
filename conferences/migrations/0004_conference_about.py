# Generated by Django 4.2.2 on 2023-06-25 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0003_remove_conference_category_conference_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='about',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]
