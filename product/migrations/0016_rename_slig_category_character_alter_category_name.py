# Generated by Django 4.0.4 on 2022-07-18 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_rename_slug_category_slig'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slig',
            new_name='character',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
