# Generated by Django 3.0.4 on 2020-03-18 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0005_message_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.BinaryField(),
        ),
    ]
