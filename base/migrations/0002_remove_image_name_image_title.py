# Generated by Django 4.2.4 on 2023-08-24 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
