# Generated by Django 3.0.1 on 2020-05-21 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20200522_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='galleryImage',
        ),
    ]
