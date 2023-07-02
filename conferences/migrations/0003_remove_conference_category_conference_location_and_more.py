# Generated by Django 4.2.2 on 2023-06-24 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0002_category_conference_date_conference_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='category',
        ),
        migrations.AddField(
            model_name='conference',
            name='location',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='conference',
            name='organiser',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.AddField(
            model_name='conference',
            name='time',
            field=models.CharField(blank=True, default='Unknown', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='date',
            field=models.CharField(blank=True, default='Unknown', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='title',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]