# Generated by Django 4.1.5 on 2023-02-01 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='category_name', to='myapp.menucategory'),
        ),
    ]
