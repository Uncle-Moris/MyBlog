# Generated by Django 4.0.4 on 2022-08-01 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_alter_tag_name_alter_tag_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('-name',)},
        ),
    ]
