# Generated by Django 4.0.4 on 2022-07-18 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]