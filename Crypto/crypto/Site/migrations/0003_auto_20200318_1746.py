# Generated by Django 3.0.4 on 2020-03-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0002_auto_20200318_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='privateKey',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='group',
            name='publicKey',
            field=models.CharField(max_length=10000),
        ),
    ]
