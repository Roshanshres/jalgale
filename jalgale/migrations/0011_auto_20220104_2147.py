# Generated by Django 3.2.7 on 2022-01-04 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jalgale', '0010_auto_20220104_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
