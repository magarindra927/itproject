# Generated by Django 4.1.7 on 2023-07-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variety',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]