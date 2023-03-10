# Generated by Django 4.1.5 on 2023-02-01 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_name_menu_person_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='person_name',
            new_name='item_name',
        ),
        migrations.AddField(
            model_name='menu',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
