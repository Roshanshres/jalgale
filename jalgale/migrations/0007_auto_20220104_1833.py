# Generated by Django 3.2.7 on 2022-01-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jalgale', '0006_contact_us'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact_Us',
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(verbose_name=''),
        ),
    ]