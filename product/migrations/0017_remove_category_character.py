# Generated by Django 4.0.4 on 2022-07-18 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_rename_slig_category_character_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='character',
        ),
    ]