# Generated by Django 2.2.5 on 2019-10-24 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='project',
            name='sort_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
