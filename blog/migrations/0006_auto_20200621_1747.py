# Generated by Django 3.0.7 on 2020-06-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200621_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_blog',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project_blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
