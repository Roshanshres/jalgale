# Generated by Django 3.2.7 on 2022-01-06 07:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jalgale', '0002_auto_20220106_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='know_more',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
