# Generated by Django 3.0.7 on 2020-06-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200621_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_blog',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
