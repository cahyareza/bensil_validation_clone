# Generated by Django 3.2.19 on 2023-05-19 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_add_new_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productunique',
            name='unique',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
