# Generated by Django 4.1.5 on 2023-02-01 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_person_name_menu_item_name_menu_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='price',
            new_name='priceofitem',
        ),
    ]
