# Generated by Django 3.2.7 on 2022-01-04 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jalgale', '0008_alter_contactus_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100)),
                ('title', models.EmailField(max_length=200)),
                ('sub_description', models.TextField()),
                ('description', models.TextField()),
            ],
        )
    ]