# Generated by Django 3.2 on 2021-05-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.TextField(max_length=50),
        ),
    ]
