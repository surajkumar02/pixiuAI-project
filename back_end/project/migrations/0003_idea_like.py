# Generated by Django 3.2.9 on 2021-11-14 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_remove_idea_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='like',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]