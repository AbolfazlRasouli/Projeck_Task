# Generated by Django 4.2.7 on 2023-11-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_remove_tag_task_task_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(null=True, to='task.tag'),
        ),
    ]
