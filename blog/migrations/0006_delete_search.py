# Generated by Django 3.2 on 2021-10-30 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Search',
        ),
    ]
