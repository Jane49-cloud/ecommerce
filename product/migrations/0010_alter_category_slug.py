# Generated by Django 4.0.4 on 2022-07-18 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name=2181372848944),
        ),
    ]
