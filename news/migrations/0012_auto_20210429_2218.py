# Generated by Django 3.2 on 2021-04-29 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20210425_1930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at', 'pk'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
    ]
